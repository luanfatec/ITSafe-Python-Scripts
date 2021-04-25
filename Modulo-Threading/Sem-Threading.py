import os
import time

start_time = time.time()

urls = [
    "www.google.com", "www.facebook.com", "www.youtube.com"
]

for url in urls:
    os.system(f"ping {url}")

print(time.time() - start_time)