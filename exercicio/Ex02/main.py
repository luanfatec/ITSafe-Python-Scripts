import random

tot_play = 0

while True:
    sort_num = random.randint(1, 1000)
    try:
        num = int(input("Entre com um numero de 1 a 1000 ou -1 para sair: "))
    except Exception:
        print(
            "Você digitou algo diferente de um numero inteiro, devido a isso, estamos parando a execução desse codigo!")
        break

    if num == -1:
        break

    if sort_num > num:
        print("O numero soteado é maior que o numero digitado!")
    elif sort_num < num:
        print("O numero soteado é menor que o numero digitado!")
    elif sort_num == num:
        print("Acertou!")

    tot_play += 1

