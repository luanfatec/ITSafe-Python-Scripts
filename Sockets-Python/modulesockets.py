import socket


def primary_sock():
    # AF_INET - Tipo de endereço para ipv4.
    # SOCK_STREAM - Define tipo para TCP.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("0.0.0.0", 1234))
    server.listen(5) # Até 5 clientes que podem se conectar ao servidor...

    input("Enter: ")


def my_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", 8081))
        server.listen(5)
        client, address = server.accept()
        client.send("Welcome in my server!".encode())

        while True:
            datas = client.recv(2048).decode()
            print(f"Received client data:\n{datas}")
            if datas == "sair":
                client.close()
                break
            client.sendall("Thanks!".encode())
        server.close()
    except Exception as msg:
        print(f"Error: {msg}")