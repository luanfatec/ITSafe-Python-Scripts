#upla = (1, 2, 3, 4, 5, 5, 1, 1, 1, 3)
#print(len(tupla))
#print(max(tupla))
#print(min(tupla))
#print(tupla.count(1))
#print("-------------------------------")
#sets = {1, 2, 3, 4, 5, 2, 4, 2, 1, 6}
#print(sets)
#sets.add(5)
#print(sets)
#sets.add(10)
#print(sets)
#sets.remove(6)
#print(sets)
"""
    O remove não pode vim após o discard, pois ele precisa que exista
    determinado elemento para excluir, já p discard não necessita que exista, 
    pois ele irá remover se existir, caso não exista, ele continuará passando o 
    código sem nenhum erro de existência.
"""
#print(sets.discard(10))
#print(sets)
#print(sets.remove(6))
#print(sets)

# ------------------ Exercício ----------------------- #
lista = []
number = int(input("Entre com um numero entre 1 e 5: "))
if number > 5:
    print("Por favor, digite um numero de acordo com o solicitado!")
elif number <= 5:
    lista.append(number)
    print("Maravilha, seu numero foi adicionado em nossa lista.")
    print(lista)

number = int(input("Entre com um numero entre 1 e 5: "))
if number > 5:
    print("Por favor, digite um numero de acordo com o solicitado!")
elif number <= 5:
    lista.append(number)
    print("Maravilha, seu numero foi adicionado em nossa lista.")
    print(lista)

number = int(input("Entre com um numero entre 1 e 5: "))
if number > 5:
    print("Por favor, digite um numero de acordo com o solicitado!")
elif number <= 5:
    lista.append(number)
    print("Maravilha, seu numero foi adicionado em nossa lista.")
    print(lista)

number = int(input("Entre com um numero entre 1 e 5: "))
if number > 5:
    print("Por favor, digite um numero de acordo com o solicitado!")
elif number <= 5:
    lista.append(number)
    print("Maravilha, seu numero foi adicionado em nossa lista.")
    print(lista)

number = int(input("Entre com um numero entre 1 e 5: "))
if number > 5:
    print("Por favor, digite um numero de acordo com o solicitado!")
elif number <= 5:
    lista.append(number)
    print("Maravilha, seu numero foi adicionado em nossa lista.")
    print(lista)