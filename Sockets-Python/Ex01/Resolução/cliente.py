import socket

port = 5000
host = "127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((host, port))

    while True:
        dados = input("Enviar: ")
        cliente.sendall(dados.encode())

        if dados == "sair":
            cliente.close()
            break

        dados = cliente.recv(2048).decode()
        print(dados)
