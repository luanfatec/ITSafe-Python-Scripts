def funcionario(nome, cargo, salario):
    funcs = []
    funcs.append(nome)
    funcs.append(cargo)
    funcs.append(salario)
    return funcs


def mostrar_salario(func):
    print(f"""O {str(func[0])} ganha {str(func[2])} com o cargo {str(func[1])}""")


def atualizar_salario(func, salario):
    func[2] = salario


fun1 = funcionario("Luan", "Help Desk", 1500)
mostrar_salario(fun1)
atualizar_salario(fun1, 1700)
mostrar_salario(fun1)
atualizar_salario(fun1, 2400)
mostrar_salario(fun1)

fun2 = funcionario("Julia", "Financeiro", 1600)
mostrar_salario(fun2)
atualizar_salario(fun2, 1900)
mostrar_salario(fun2)
atualizar_salario(fun2, 2400)
mostrar_salario(fun2)
