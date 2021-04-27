import socket
import threading

port = 2222
host = "127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    def read_message(cl):
        while True:
            data_server = cl.recv(2048).decode()
            print(data_server)

    try:
        client.connect((host, port))
        print("Conectado ao servidor!")

        th = threading.Thread(target=read_message, args=(client,))
        th.start()

        while True:
            message = input("Enviar: ")
            client.sendall(message.encode())
            if message == "sair":
                break

    except socket.error as msg:
        print(msg)

    except Exception as msg:
        print(msg)

    finally:
        client.close()
