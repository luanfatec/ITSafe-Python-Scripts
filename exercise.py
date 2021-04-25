# Exercícios

# Init Minha solução
exer_error = """
Error: Inválid argument. 
Use: 
    n1  Receive value number 1.
    n2  Receive value number 2.
    action  Receive the type of operation.

    Example: 
    exercise(n2=10, n1=20, action="+")
"""

"""def exercise(number1, number2, action):
    if number1 == "" or number2 == "" or action == "" or action == int or action == bool:
        print(exer_error)
    elif action == "+":
        print(f"Result: {number1 + number2}")
    elif action == "-":
        print(f"Result: {number1 - number2}")
    elif action == "/":
        if number1 == 0 or number2 == 0:
            print("0 cannot be divided by any other number!")
        else:
            print(f"Result: {number1 / number2}")
    elif action == "*":
        print(f"Result: {number1 * number2}")
    else:
        print(exer_error)


exercise(number1=5, number2=5, action="*")"""


# End Minha solução

# Init Solução aula
def calculadora(operador, num1, num2):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "/":
        if num1 == 0 or num2 == 0:
            print("Erro: Não pode dividir por 0.")
        else:
            return num1 / num2
    elif operador == "*":
        return num1 * num2
    else:
        return exer_error

while True:
    num1 = int(input("Insira um numero: "))
    operator = input("Insira um operador (+,-,*,/) ou 'sair': ")
    if operator == "sair":
        break
    num2 = int(input("Insira outro numero: "))
    resultado = calculadora(operator, num1, num2)
    print(resultado)

# End Solução aula
