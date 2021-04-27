import socket
import threading


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    clientes = []

    def conexao(servidor):
        while True:
            client, address = servidor.accept()
            clientes.append(client)

    try:
        server.bind(("0.0.0.0", 8000))
        server.listen(5)

        th = threading.Thread(target=conexao, args=(server,))
        th.start()

        while True:
            command = input("Entre com um comando para o cliente: ")
            if clientes:
                for cliente in clientes:
                    cliente.sendall(command.encode())
                    retorno = cliente.recv(2048).decode()
                    print(retorno)

    except Exception as msg:
        print(msg)

    finally:
        server.close()