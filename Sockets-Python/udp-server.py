import socket


# SOCK_DGRAM -> Utilizado para protocolo de comunicação UDP.
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as serve:

    try:
        serve.bind(("0.0.0.0", 2222))

        while True:
            print("Esperando uma conexão!")
            dados, client = serve.recvfrom(2048)
            print(dados.decode())

            if dados == "sair":
                break

            dado = input("Enviar: ")
            serve.sendto(dado.encode(), client)

    except Exception as msg:
        print(msg)

    finally:
        serve.close()
