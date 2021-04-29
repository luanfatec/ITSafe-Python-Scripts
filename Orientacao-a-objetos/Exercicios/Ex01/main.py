import random

class AdvinheNumero(object):
    def __init__(self):
        self.pc = 0

    def sort_num(self):
        return random.randint(1, 5)

    def verificar_escolha(self, num):
        sr = self.sort_num()
        if sr > num:
            print("O numero soteado é maior que o numero digitado!\n")
            self.pc += 1
        elif sr < num:
            print("O numero soteado é menor que o numero digitado!\n")
            self.pc += 1
        elif sr == num:
            self.pc += 1
            print(f"Acertou, depois de {self.pc} tentativas!!!\n")
            self.pc = 0


player = AdvinheNumero()
while True:
    try:
        num = int(input("Entre com um numero de 1 a 1000 ou -1 para sair: "))
        player.verificar_escolha(num)
    except Exception:
        print(
            "Você digitou algo diferente de um numero inteiro, devido a isso, estamos parando a execução desse codigo!\n")
        continue
