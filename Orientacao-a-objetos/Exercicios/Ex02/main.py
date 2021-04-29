from socket import *

class GenServer(object):
    port = 0
    host = ""

    def __init__(self, host, port):
        GenServer.host = host
        GenServer.port = port

    def recv_and_send_message(self, client):
        message = client.recv(2048).decode()
        client.sendall(message.encode())

    def create_connect(self, q_connect):
        with socket(AF_INET, SOCK_STREAM) as server:
            try:
                server.bind((GenServer.host, GenServer.port))
                server.listen(q_connect)
                print("Escutando...")

                client, addr = server.accept()
                print(f"Cliente {addr[0]} conectado!")

                while True:
                    self.recv_and_send_message(client)

            except Exception as msg:
                print(msg)

c = GenServer(host="0.0.0.0", port=8888)
c.create_connect(1)