import socket
from socket import *

def talk_messages():
    while True:
        datas = input("Entre com alguma mensagem para o servidor: ")
        client.send(datas.encode())
        if datas == "sair":
            client.close()
            break
        datas = client.recv(2048).decode()
        print(datas)

try:
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("127.0.0.1", 8081))
    talk_messages()
except Exception as msg:
    print(f"Error: {msg}")
finally:
    client.close()
    print("Connection finished!")
