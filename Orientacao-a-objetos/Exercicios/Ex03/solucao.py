import random


class PedraPapelTesoura(object):
    def __init__(self):
        self.computador = 0
        self.usuario = 0

    def __str__(self):
        if self.usuario == 5:
            return "Usuário Ganhou!!!"
        else:
            return "Computador ganhou!!!"

    def jogo(self, escolha_usuario):
        sort = random.choice(["pedra", "papel", "pesoura"])

        if sort == "pedra" and escolha_usuario == "tesoura":
            print("Computador pedra, usuário tesoura.")
            self.computador += 1

        elif sort == "pedra" and escolha_usuario == "papel":
            print("Computador pedra, usuário papel.")
            self.usuario += 1

        elif sort == "papel" and escolha_usuario == "pedra":
            print("Computador papel, usuário pedra.")
            self.computador += 1

        elif sort == "papel" and escolha_usuario == "tesoura":
            print("Computador papel, usuário tesoura.")
            self.usuario += 1

        elif sort == "tesoura" and escolha_usuario == "papel":
            print("Computador tesoura, usuário papel.")
            self.computador += 1

        elif sort == "tesoura" and escolha_usuario == "pedra":
            print("Computador tesoura, usuário pedra.")
            self.usuario += 1


    def termino(self):
        if self.computador == 5 or self.usuario == 5:
            return True
        else:
            return False

class PedraPapelTesoura2(PedraPapelTesoura):
    def termino(self):
        if self.computador == 5 or self.usuario == 2:
            return True
        else:
            return False

    def __str__(self):
        if self.usuario == 2:
            return "Usuário Ganhou!!!"
        else:
            return "Computador ganhou!!!"


ppt = PedraPapelTesoura2()
while not ppt.termino():
    ppt.jogo(input("Pedra, papel ou tesoura: "))
else:
    print(ppt())
