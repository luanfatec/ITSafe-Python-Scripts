from socket import *

host = "0.0.0.0"
port = 3000

# Create socket type TCP/IPv4.
serve = socket(AF_INET, SOCK_STREAM)

try:
    # Create bind.
    serve.bind((host, port))
    serve.listen(5)
    print(f"Escutando em {host}:{port}...")
    client, addresses = serve.accept()
    print(f"Cliente {addresses[0]} conectado!")

    while True:
        data_client = client.recv(2048).decode()
        print(data_client)
        if data_client == "sair":
            client.sendall("Até mais amigo!".encode())
            break
        message = input("Enviar: ")
        client.send(message.encode())


except Exception as msg:
    print(msg)
finally:
    print("Conexão finalizada")
    serve.close()
