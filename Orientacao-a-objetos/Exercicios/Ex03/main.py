import random


class PDT(object):
    def __init__(self):
        self.pc = 0
        self.tentativas = 0
        self.eu = 0
        self.jogadas = 0

    def play(self):
        while True:
            sort_p = random.choice(["pedra", "papel", "tesoura"])
            palavra = input("Escolha entre Pedra, Papel e Tesoura ou sair: ")

            if palavra == "sair":
                if self.eu == self.pc:
                    print(f"\nO jogo ficou empatado em {self.pc} para a maquina e {self.eu} para você!!!")
                elif self.pc > self.eu:
                    print(f"\nO jogo terminou em {self.pc} para a maquina e {self.eu} para você, que pena, você perdeu!!!")
                elif self.eu > self.pc:
                    print(f"\nO jogo terminou em {self.pc} para a maquina e {self.eu} para você, você ganhou!!!")
                break

            elif sort_p == "pedra" and palavra == "papel":
                self.jogadas += 1
                self.tentativas += 1
                self.eu += 1
                print(f"Você acertou após {self.tentativas} tentativas!!!\n")
                self.tentativas = 0

            elif sort_p == "papel" and palavra == "tesoura":
                self.jogadas += 1
                self.tentativas += 1
                self.eu += 1
                print(f"Você acertou após {self.tentativas} tentativas!!!\n")
                self.tentativas = 0

            elif sort_p == "tesoura" and palavra == "pedra":
                self.jogadas += 1
                self.tentativas += 1
                self.eu += 1
                print(f"Você acertou após {self.tentativas} tentativas!!!\n")
                self.tentativas = 0


            elif sort_p == "tesoura" and palavra == "tesoura":
                self.jogadas += 1
                self.tentativas += 1
                print(f"Epa, deu empate!!!\n")
                self.tentativas = 0

            elif sort_p == "papel" and palavra == "papel":
                self.jogadas += 1
                self.tentativas += 1
                print(f"Epa, deu empate!!!\n")
                self.tentativas = 0

            elif sort_p == "pedra" and palavra == "pedra":
                self.jogadas += 1
                self.tentativas += 1
                print(f"Epa, deu empate!!!\n")
                self.tentativas = 0


            elif sort_p == "papel" and palavra == "pedra":
                self.jogadas += 1
                self.tentativas += 1
                self.pc += 1
                print(f"Pc ganhou!!!\nQue pena, tente novamente, vai que você ganha!\n")

            elif sort_p == "tesoura" and palavra == "papel":
                self.jogadas += 1
                self.tentativas += 1
                self.pc += 1
                print(f"Pc ganhou!!!\nQue pena, tente novamente, vai que você ganha!\n")

            elif sort_p == "pedra" and palavra == "tesoura":
                self.jogadas += 1
                self.tentativas += 1
                self.pc += 1
                print(f"Pc ganhou!!!Que pena, tente novamente, vai que você ganha!\n")

        print(f"""\nVocê jogou {self.jogadas} vezes!""")
        exit()


PDT().play()
