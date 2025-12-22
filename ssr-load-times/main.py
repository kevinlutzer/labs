import time
import csv
import random
import requests
from datetime import datetime

BASE_URL = "https://speed-test-blond.vercel.app/page"
CACHE_HIT_PAGE = 10
RUNS_PER_MODE = 10
CSV_FILE = "api_timing_results.csv"


def time_request(url):
    start = time.perf_counter()
    response = requests.get(url)
    end = time.perf_counter()
    return response.status_code, end - start


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
        status, elapsed = time_request(url)

        writer.writerow([
            run_counter,
            datetime.utcnow().isoformat(),
            url,
            status,
            round(elapsed, 6),
            True
        ])

        print(f"Run {run_counter} (cache-hit target): {elapsed:.4f}s")
        run_counter += 1

    # -----------------------------
    # Cache-miss–targeted runs
    # -----------------------------
    for _ in range(RUNS_PER_MODE):
        page = random.randint(100, 110)
        url = f"{BASE_URL}/{page}"
        status, elapsed = time_request(url)

        writer.writerow([
            run_counter,
            datetime.utcnow().isoformat(),
            url,
            status,
            round(elapsed, 6),
            False
        ])

        print(f"Run {run_counter} (cache-miss target, page {page}): {elapsed:.4f}s")
        run_counter += 1

print(f"\nResults saved to {CSV_FILE}")
