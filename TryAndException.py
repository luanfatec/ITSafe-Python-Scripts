"""try:
    num = input("Entre com um numero: ")
    print(10/int(num))
except Exception as err:
    print("Error: Um numero não pode ser divido por 0")
    print(f"Error except: {err}")
    with open("Error.log", "a") as err_file:
        err_file.write(f"Error: {err}\n")

"""

try:
    num = input("Entre com um numero: ")
    print(10 / int(num))
except Exception as err:
    print(f"Error: {err}")
else:
    print("Else")
finally:
    print("Sempre será exibido!")

print("Final")