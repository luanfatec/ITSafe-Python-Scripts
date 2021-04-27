import socket
import threading as th

port = 3380
host = "0.0.0.0"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serve:

    def config_clients(c):
        while True:
            data_client = c.recv(2048).decode()
            if data_client == "Olá":
                print(data_client)
                c.send(f"Olá {address[0]}, seja bem vindo ao meu servidor!".encode())
            elif "nome" in data_client:
                print(data_client)
                c.send("Que legal, aprendi seu nome!".encode())
            elif "sair" == data_client or "sair" == data_client.lower() \
                    or "sair" == data_client.upper() or "sair" == data_client.capitalize():
                print(data_client.capitalize())
                c.send("sair".encode())
                c.close()
                break
            else:
                print(data_client)
                c.send("""
                        Desculpe-me, não compreendi o que está querendo dizer!
                        Se quiser, pode tentar novamente ou fechar a conexão!
                        """.encode())
        c.close()

    try:
        serve.bind((host, port))
        serve.listen(5)

        while True:
            client, address = serve.accept()
            print(f"Conexão recebida de {address[0]}...")

            _thr = th.Thread(target=config_clients, args=(client,))
            _thr.start()



    except Exception as msg:
        print(msg)

    finally:
        serve.close()
        client.close()
