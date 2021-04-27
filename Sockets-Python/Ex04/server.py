import threading
import socket

port = 9003
host = "0.0.0.0"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serve:
    def config_client_server(c):
        while True:
            command = input("Entre com um comando: ")
            if command == "sair":
                c.sendall(command.encode())
                c.close()
                break
            c.sendall(command.encode())
            print("Comando enviado com sucesso!")

        c.close()

    try:
        serve.bind((host, port))
        serve.listen(5)
        print(f"Escutando em {host}:{port}...")

        while True:
            client, address = serve.accept()
            th = threading.Thread(target=config_client_server, args=(client,))
            th.start()

    except socket.error as msg:
        print(msg)

    finally:
        serve.close()
