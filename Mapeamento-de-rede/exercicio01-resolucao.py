from main import *
import threading

my_ip = getioreso()[1]
network = my_ip[:my_ip.rfind(".")+1]
clientes = []
threads = []
lock = threading.Lock()

for oct in range(1, 255):
    netw = network + str(oct)
    th = threading.Thread(target=scanner, args=(netw, clientes, lock,))
    th.start()
    threads.append(th)

for thred in threads:
    thred.join()

print(clientes)