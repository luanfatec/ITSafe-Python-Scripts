import socket


class ServidorSocket(object):
    def __init__(self, host, port):
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind((host, port))
        self.servidor.listen(100)
        self.fechado = False

    def aceitar(self):
        self.client, address = self.servidor.accept()

    def __call__(self, *args, **kwargs):
        self.client.sendall("Bem vindo!!!".encode())
        while True:
            dados = self.client.recv(2048).decode()
            print(f"Client: {dados}")

            if dados == "sair":
                self.client.close()
                self.servidor.close()
                self.fechado = True
                break

            dados = input("Enviar: ")
            self.client.sendall(dados.encode())

srv = ServidorSocket("", 1337)
srv.aceitar()
srv()