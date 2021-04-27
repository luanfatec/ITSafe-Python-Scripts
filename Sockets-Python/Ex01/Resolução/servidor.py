import socket

port = 5000
host = "0.0.0.0"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serve:
    try:
        serve.bind((host, port))
        serve.listen(5)

        cliente, addr = serve.accept()
        print(f"Bem vindo {addr[0]}:{addr[1]}")

        while True:
            dados = cliente.recv(2048).decode()
            print(dados)

            if dados == "sair":
                cliente.close()
                break

            dados = input("Enviar: ")
            cliente.sendall(dados.encode())

    except socket.error as msg:
        print(msg)

    finally:
        serve.close()