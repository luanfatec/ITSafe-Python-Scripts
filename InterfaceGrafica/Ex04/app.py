import eel
from main import *
import threading


@eel.expose
def apresenta_dados():
    ips = []
    with open("db.txt", "r+") as file:
        try:
            for ip in file.readlines():
                ips.append(ip.rstrip())

        except Exception as msg:
            pass

        finally:
            file.close()

    return ips


@eel.expose
def scanner_main():
    my_ip = get_ip()[1]
    network = my_ip[:my_ip.rfind(".") + 1]
    threads = []
    clientes = []
    lock = threading.Lock()

    for oct in range(1, 255):
        netw = network + str(oct)
        th = threading.Thread(target=scanner, args=(netw, clientes, lock,))
        th.start()
        threads.append(th)

    for thred in threads:
        thred.join()

    return armazena(clientes)


eel.init('web')

try:
    eel.start('index.html', port=0)   #python will select free ephemeral ports.
except (SystemExit, MemoryError, KeyboardInterrupt):
    print ("Program Exit, Save Logs if Needed")