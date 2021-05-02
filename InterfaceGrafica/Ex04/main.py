import os
from scapy import *

def get_ip():
    ipcnf = os.popen("ipconfig").readlines()
    apis = []
    for item in ipcnf:
        if "Endereço IPv4." in item or "Endere‡o IPv4" in item:
            apis.append(item[49:])

    return apis


def scanner(network, clientes, lock):
    response_popen = os.popen(f"ping {network} -n 1 ").read()
    if "TTL" in response_popen:
        with lock:
            clientes.append(network)


def armazena(clients):
    with open('db.txt', 'w+') as file:
        try:
            for ip in clients:
                file.write(f"{ip}\n")

        except Exception as msg:
            return False

        finally:
            file.close()

        return True
