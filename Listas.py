lista = [3306, 8443, 21, 23, 80, 443] # Lista simples
print(lista)
lista.append(8080)
print(lista)
lista.sort()
print(lista)
print(lista.index(80))
print(lista[4])
print(lista[1:4])
lista.pop(4)
print(lista)
lista.remove(8080)
print(lista)
del lista[2]
print(lista)
print(len(lista))
lista2 = [53, 8092, 3000]
lista.extend(lista2)
print(lista)
lista.insert(1, 25)
print(lista)

if 23 in lista:
    print("Existe!")
else:
    print("Não existe!")

if 54 not in lista:
    print("Não existe!")