import socket
import threading

port = 2222
host = "0.0.0.0"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serve:
    def config_clients(c):
        while True:
            dado = c.recv(2048).decode()
            print(dado)

            if dado == "sair":
                break

            dado = input("Enviar para cliente: ")
            c.sendall(dado.encode())
        c.close()


    try:
        serve.bind((host, port))
        serve.listen(5)

        while True:
            cliente, addr = serve.accept()
            print(f"Bem vindo {addr[0]}:{addr[1]}")
            th = threading.Thread(target=config_clients, args=(cliente,))
            th.start()

    except socket.error as msg:
        print(msg)

    finally:
        serve.close()
