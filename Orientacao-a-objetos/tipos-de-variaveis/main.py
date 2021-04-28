class Numeros(object):
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.soma = 0

    def somar_com_outro_numero(self, numero3):
        self.soma = numero3 + self.numero1 + self.numero2

    def mostrar_soma(self):
        print(self.soma)

    def mostrar_numero1(self):
        print(self.numero1)

    def mostrar_numero2(self):
        print(self.numero2)


teste = Numeros(10, 5)
teste.somar_com_outro_numero(4)
teste.mostrar_soma()
teste.mostrar_numero1()
teste.mostrar_numero2()