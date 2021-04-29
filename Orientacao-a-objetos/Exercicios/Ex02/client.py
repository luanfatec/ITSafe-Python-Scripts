import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    try:
        client.connect(("127.0.0.1", 1337))

        while True:
            datas = client.recv(2048).decode()
            print(f"Servidor: {datas}")

            dat = input("Enviar: ")
            if dat == "sair":
                break

            client.sendall(dat.encode())

    except Exception as msg:
        print(msg)

    finally:
        client.close()