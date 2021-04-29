class Funcionario(object):
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def mostrar_salario(self):
        print(self.salario)


class Chefe(Funcionario):
    def mostrar_salario(self):
        print("Informação confidêncial!")

    def mostre_chefe(self):
        print("Eu sou chefe!")

emp = Chefe("Luan", "Cyber", 20000)
fun = Funcionario("Julia", "Cyber", 25000)

emp.mostrar_salario()
fun.mostrar_salario()