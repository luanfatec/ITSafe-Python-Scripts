import socket

port = 2222
host = "127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    try:
        cliente.connect((host, port))

        while True:
            dados = input("Enviar: ")
            cliente.sendall(dados.encode())

            if dados == "sair":
                break

            dados = cliente.recv(2048).decode()
            print(dados)

    except socket.error as msg:
        print(msg)

    finally:
        cliente.close()
