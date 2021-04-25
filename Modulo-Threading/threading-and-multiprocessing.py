import threading
import time
import multiprocessing


# -------- Exercício --------- #
"""def return_num():
    for i in range(1, 100000):
        print(f"{i}\n")

start_time = time.time()

for i in range(5):
    thr = threading.Thread(target=return_num)
    thr.start()

print(time.time() - start_time)"""

"""# -------- Resolução aula --------- #
start_time = time.time()
threads = []
def contador(num):
    for i in range(num):
        print(i)

for valor in range(5):
    t = threading.Thread(target=contador, args=(100000, ))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print(time.time() - start_time)"""
