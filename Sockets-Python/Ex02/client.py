import socket

port = 3380
host = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((host, port))
    print("Conectado ao servidor!")

    while True:
        message = input("Enviar: ")
        client.send(message.encode())
        if message == "sair":
            break
        data_server = client.recv(2048).decode()
        print(data_server)

except Exception as msg:
    print(msg)
finally:
    client.close()
