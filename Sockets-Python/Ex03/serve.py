import socket
import threading


def config_server(host, port):
    sock_count = 0
    serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def config_client_thread(c):
        while True:
            return_data = c.recv(2048).decode()
            if not return_data:
                print("Finalizada conexão com cliente!")
                break
            if return_data == "sair":
                print("Finalizada conexão pelo cliente!")
                break
            c.sendall(return_data.encode())
            print(return_data)
        c.close()

    try:
        serve.bind((host, port))
        serve.listen(5)
        print(f"Escutando em {host}:{port}...")

        while True:
            client, address = serve.accept()
            print(f"Recebida conexão de {address[0]}...")
            th = threading.Thread(target=config_client_thread, args=(client,))
            th.start()
            sock_count += 1
            print(sock_count)

    except Exception as msg:
        print(msg)

    finally:
        serve.close()


if __name__ == "__main__":
    config_server("0.0.0.0", 9000)
