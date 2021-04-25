from socket import *

# Create socket type TCP/IPv4.
client = socket(AF_INET, SOCK_STREAM)

try:
    client.connect(("127.0.0.1", 3000))
    print("Conectado ao servidor!")

    while True:
        message = input("Enviar: ")
        if message == "sair":
            client.send(message.encode())
            print("Até mais e volte sempre!")
            break
        client.send(message.encode())
        print(client.recv(2048).decode())


except Exception as msg:
    print(msg)

finally:
    client.close()
    print("Conexão finalizada com o servidor!")
