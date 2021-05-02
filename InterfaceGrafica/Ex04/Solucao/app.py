import eel
import os
import threading

eel.init('web')

@eel.expose
def comecar_scan(endereco_ip):
    my_ip = endereco_ip
    network = my_ip[:my_ip.rfind(".") + 1]

    for oct in range(1, 255):
        netw = network + str(oct)
        th = threading.Thread(target=scanner, args=(netw, lock,))
        th.start()
        threads.append(th)

    for thred in threads:
        thred.join()

    return clientes


def scanner(network, lock):
    response_popen = os.popen(f"ping {network} -n 1 ").read()
    if "TTL" in response_popen:
        with lock:
            clientes.append(network)

clientes = []
threads = []
lock = threading.Lock()


try:
    eel.start('index.html', size=(850,400), port=0)   #python will select free ephemeral ports.
except (SystemExit, MemoryError, KeyboardInterrupt):
    print ("Program Exit, Save Logs if Needed")