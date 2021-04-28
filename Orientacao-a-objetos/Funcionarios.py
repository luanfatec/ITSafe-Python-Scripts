class Funcionario(object):
    num_fun = 0 # Variável Global
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        Funcionario.num_fun += 1

    def mostrar_salario(self):
        print(f"""O {self.nome} ganha {self.salario} com o cargo {self.cargo}""")

    def atualizar_salario(self, salario):
        self.salario = salario

    def num_funcs(self):
        print(Funcionario.num_fun)


func = Funcionario("Luan", "Auxiliar de Suporte Técnico", 1200)
func2 = Funcionario("Julia", "Suporte Técnico", 1400)
func3 = Funcionario("Julia", "Suporte Técnico", 1400)
func4 = Funcionario("Julia", "Suporte Técnico", 1400)
func5 = Funcionario("Julia", "Suporte Técnico", 1400)

func.num_funcs()
