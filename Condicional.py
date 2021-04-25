# n = int(input("Insert your number: "))
"""
if n > 5:
    print("O número %d é maior que 5." % n)
elif n == 5:
    print("O número %d é igual a 5" % n)
else:
    print("O número %d não é maior que 5" % n) """

"""" ------------------- Exercício -------------------------"""

# impar or par
# if n%2 == 0:
#     print("O número %d é par!" % n)
# else:
#     print("O número %d é impar!" % n)

# Linguagem preferida
"""lg = str(input("\033[94mEntre com sua linguagem preferida: \033[0m"))
if lg == "python" or lg == "Python":
    print("\033[92mQue legal, então você fala minha lingua!\033[0m")
else:
    print("\033[91mDesculpe, houve um erro ao tentar compreender você, pois sua linguem não é python!\033[0m'")"""

# Somando um terceiro numero com o resultado anterior e comparando o com a soma dos dois anteriores.
n1 = int(input("Entre com um numero: "))
n2 = int(input("Entre com outro numero: "))
s1 = n1 + n2
n3 = int(input("Entre com mais numero: "))

if n3 < s1:
    print("Muito bom!!!")
else:
    print("Por favor digite um numero menor!")