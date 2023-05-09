import os
import threading
from multiprocessing import Process
from time import perf_counter

import requests


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    print(f"Processing file from {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    try:
        total_start = perf_counter()

        encryption_start = perf_counter()
        encryption_task = Process(target=encrypt_file, args=("rockyou.txt",))
        encryption_task.start()
        encryption_task.join()
        encryption_counter = perf_counter() - encryption_start

        download_start = perf_counter()
        download_task = threading.Thread(
            target=download_image, args=("https://picsum.photos/1000/1000",)
        )
        download_task.start()
        download_task.join()
        download_counter = perf_counter() - download_start

        total_counter = perf_counter() - total_start
        print(
            f"Time taken for encryption task: {encryption_counter}, "
            f"I/O-bound task: {download_counter}, "
            f"Total: {total_counter} seconds"
        )
    except Exception as e:
        print(f"Error occurred: {e}")
