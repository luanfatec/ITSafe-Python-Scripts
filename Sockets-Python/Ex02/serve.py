import socket
import threading as th

port = 3380
host = "0.0.0.0"

serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serve.bind((host, port))
    serve.listen(5)
    client, address = serve.accept()
    print(f"Conexão recebida de {address[0]}...")
    while True:
        data_client = client.recv(2048).decode()
        if data_client == "Olá":
            print(data_client)
            client.send(f"Olá {address[0]}, seja bem vindo ao meu servidor!".encode())
        elif "nome" in data_client:
            print(data_client)
            client.send("Que legal, aprendi seu nome!".encode())
        elif "sair" == data_client or "sair" == data_client.lower()\
                or "sair" == data_client.upper() or "sair" == data_client.capitalize():
            print(data_client.capitalize())
            client.send("""
            Vai sair? 
            Que pena, foi bom te conhecer!
            """.encode())
            client.close()
        else:
            print(data_client)
            client.send("""
            Desculpe-me, não compreendi o que está querendo dizer!
            Se quiser, pode tentar novamente ou fechar a conexão!
            """.encode())

except Exception as msg:
    print(msg)

finally:
    serve.close()
    client.close()
