# Desenvolvimento com o módulo multiprocessing e mecanismos de sincronização entre ações paralelas (threading) : semaphore e lock

import multiprocessing
import threading

"""
def contador(num):
    for i in range(num):
        print(i)


if __name__ == "__main__":
    for i in range(5):
        p = multiprocessing.Process(target=contador, args=(100000,))
        p.start()
"""


# def contador(s): # Semaphore
#     for i in range(100000):
#         with s:
#             print(i)
def contador(l): # Lock
    for i in range(100000):
        with l:
            print(i)

# semaphore = threading.Semaphore(1)
lock = threading.Lock()
for valor in range(5):
    t = threading.Thread(target=contador, args=(lock, ))
    t.start()