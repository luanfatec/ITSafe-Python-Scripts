import os


def get_ip():
    ip = os.popen("ipconfig").read()
    for line in ip:
        if "Endere‡o IPv4" in line or "Endereço IPv4." in line:
            init = line.find(":")
            _exit = line[init + 2:-1]


def scanner(network, clientes, lock):
    response_popen = os.popen(f"ping {network} -n 1 ").read()
    if "TTL" in response_popen:
        with lock:
            clientes.append(network)
            print(network)


def menu():
    print("""
    GERENCIADOR DE REDE
    ----------------------
    1) Mostrar clientes
    2) Executar comando
    3) Desconectar cliente
    4) Sair
    """)


def mostrar_clients(clients):
    cont = 0
    for client in clients:
        print(f"{cont} = {client[1][0]}")
        cont += 1

def commands(clients):
    mostrar_clients(clients)
    id_client = int(input("Escolha um cliente: "))
    sock_client = clients[id_client][0]
    command = input("Comando a ser executado: ")
    sock_client.sendall(command.encode())
    print(sock_client.recv(2048).decode())

def command_exit(clients):
    mostrar_clients(clients)
    id_client = int(input("Escolha um cliente: "))
    sock_client = clients[id_client][0]
    sock_client.close()
    clients.remove(clients[id_client])
    print("Cliente removido com sucesso!")