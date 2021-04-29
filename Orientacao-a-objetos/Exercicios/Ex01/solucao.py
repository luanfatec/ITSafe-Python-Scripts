import random


class AdivinheONumero(object):
    contador = 0

    def __init__(self):
        AdivinheONumero.contador += 1
        self.numero = random.randint(1, 2)
        self.tentativas = 0

    def __call__(self, *args, **kwargs):
        numero = kwargs["numero"]
        if numero > self.numero:
            print("Seu numero é maior.")
            self.tentativas += 1
            return False

        if numero < self.numero:
            print("Seu numero é menor.")
            self.tentativas += 1
            return False

        else:
            return True

while True:
    numero = int(input("Adivinheo o numero ou -1 para sair: "))

    if numero == -1:
        break

    jogo = AdivinheONumero()

    while not jogo(numero=numero):
        numero = int(input("Adivinheo o numero: "))

    else:
        print(f"Você acertou em {jogo.tentativas}")

print(f"Jogo terminou em {jogo.contador}")
