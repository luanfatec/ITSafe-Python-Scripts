import socket

port = 9000
host = "127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((host, port))

    while True:
        data_send = input("Enviar: ")
        if data_send == "sair":
            break

        client.sendall(data_send.encode())
        data_recv = client.recv(2048).decode()
        print(data_recv)

except Exception as msg:
    print(msg)

finally:
    client.close()
