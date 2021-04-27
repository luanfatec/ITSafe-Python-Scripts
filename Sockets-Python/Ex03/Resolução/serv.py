import socket
import threading

port = 2222
host = "0.0.0.0"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    clientes = []

    def config_clients(c):
        while True:
            dado = c.recv(2048).decode()

            if dado == "sair":
                clientes.remove(c)
                break

            for msg in clientes:
                msg.sendall(dado.encode())

        c.close()

    try:
        srv.bind((host, port))
        srv.listen(5)

        while True:
            client, address = srv.accept()
            clientes.append(client)
            th = threading.Thread(target=config_clients, args=(client,))
            th.start()

    except socket.error as msg:
        print(msg)

    except Exception as msg:
        print(msg)

    finally:
        srv.close()
