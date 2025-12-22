import time
import csv
import random
import requests
from datetime import datetime

BASE_URL = "https://speed-test-blond.vercel.app/page"
CACHE_HIT_PAGE = 300
RUNS_PER_MODE = 300
CSV_FILE = "api_timing_results.csv"


def time_request(url):
    start = time.perf_counter()
    response = requests.get(url)
    end = time.perf_counter()
    return response.status_code, response.headers.get("X-Vercel-Cache", "") == "HIT", end - start

with open(CSV_FILE, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "run",
        "timestamp_utc",
        "url",
        "status_code",
        "elapsed_seconds",
        "cache_hit_target"
    ])

    run_counter = 1

    # -----------------------------
    # Cache-hit–targeted runs
    # -----------------------------
    for _ in range(RUNS_PER_MODE):
        url = f"{BASE_URL}/{CACHE_HIT_PAGE}"
        status, cache_hit, elapsed = time_request(url)

        writer.writerow([
            run_counter,
            datetime.utcnow().isoformat(),
            url,
            status,
            round(elapsed, 6),
            cache_hit
        ])

        print(f"Run {run_counter} (cache-miss target): {elapsed:.4f}s cache_hit={cache_hit=}")
        run_counter += 1

    # -----------------------------
    # Cache-miss–targeted runs
    # -----------------------------
    for _ in range(RUNS_PER_MODE):
        page = random.randint(0, 100000000000)
        url = f"{BASE_URL}/{page}"
        status, cache_hit, elapsed = time_request(url)

        writer.writerow([
            run_counter,
            datetime.utcnow().isoformat(),
            url,
            status,
            round(elapsed, 6),
            cache_hit
        ])

        print(f"Run {run_counter} (cache-miss target, page {page}): {elapsed:.4f}s cache_hit={cache_hit=}")
        run_counter += 1

print(f"\nResults saved to {CSV_FILE}")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV
df = pd.read_csv(CSV_FILE)

# Map cache hit to x positions
df["x"] = df["cache_hit_target"].map({True: 0, False: 1})

# Jitter to avoid overlap
jitter = np.random.normal(0, 0.04, size=len(df))

plt.figure(figsize=(8, 5))

# Scatter individual points
plt.scatter(
    df["x"] + jitter,
    df["elapsed_seconds"],
    alpha=0.35
)

# Compute medians
medians = (
    df.groupby("cache_hit_target")["elapsed_seconds"]
      .median()
      .reset_index()
)

medians["x"] = medians["cache_hit_target"].map({True: 0, False: 1})

# Plot median bubbles
plt.scatter(
    medians["x"],
    medians["elapsed_seconds"],
    s=400,
    edgecolors="black"
)

# Label the median values
for _, row in medians.iterrows():
    label = f"{row['elapsed_seconds']:.3f}s"
    plt.text(
        row["x"],
        row["elapsed_seconds"],
        label,
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

plt.xticks([0, 1], ["Cache Hit", "Cache Miss"])
plt.ylabel("Latency (seconds)")
plt.title("Latency Distribution with Median Labels")

plt.show()