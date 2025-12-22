import time
import requests

url = "https://speed-test-blond.vercel.app/page/10"
start_time = time.perf_counter()
response = requests.get(url)
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Status code: {response.status_code}")
print(f"Total time: {elapsed_time:.4f}s")
