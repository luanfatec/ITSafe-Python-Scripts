from socket import *

with socket(AF_INET, SOCK_DGRAM) as client:

    try:
        while True:
            dado = input("Enviar: ")

            if dado == "sair":
                dado_server, server = client.recvfrom(2048)
                break

            client.sendto(dado.encode(), ("127.0.0.1", 2222))
            dado_server, server = client.recvfrom(2048)
            print(dado_server.decode())

    except Exception as msg:
        print(msg)

    finally:
        client.close()