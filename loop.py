"""soma = 0
numeros = []
qx = int(input("Quantas vezes deseja somar?\nEntre com uma quantidade: "))

for i in range(qx):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
    soma = soma + numero
print(soma)
print(numeros)"""

#  ------------- Type While ------------ #
"""qx = int(input("Quantas vezes deseja somar?\nEntre com uma quantidade de soma: "))
soma = 0
numeros = []
while qx > 0:
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
    soma += numero
    qx -= qx
print(soma)"""

"""soma = 0
while True:
    numero = int(input("Entre com um numero: "))
    if numero == -1:
        break
    soma += numero

print(soma)"""

#  ------------- Loop com pass e continue ------------ #

"""soma = 0
for i in range(4):
    numero = int(input("Entre com um numero: "))
    if 5 > numero or numero < 1:
        continue
    soma += numero

print(soma)"""

# soma = 0
# for i in range(4):
#     numero = int(input("Entre com um numero: "))
#     if 5 > numero or numero < 1:
#         pass
#         soma += numero
#     print("Continuando....")
#
# print(soma)



# Como trabalhar com loops e listas e acrescentar o else ao loop

# usuarios = {
#     "name":"Luan santos", "idade":20, "cidade":"Chavantes"
# }

# for chave_user in usuarios.keys():
#     print(chave_user)

for i in range(3):
    accept = input("Você concorda com os termos? (y/n)")
    if accept == "N" or accept == "n":
        break
else:
    print("O usuário concordou as 3 vezes com o termo, sendo assim, ele possui permissão.")
print("Teste")