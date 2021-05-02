import eel
# import random

# @eel.expose
# def escolher_numero():
#     return random.randint(1, 1000)

def usuario_input():
    eel.esperar()()
    while True:
        try:
            carregar = int(input("Escolha -> Carregar 1, fechar 0: "))
        except:
            print("Digitou algo errado!")

        if carregar == 1:
            eel.js_carregar()
        elif carregar == 0:
            eel.js_fechar()
        else:
            print('Nada aconteceu!')
            pass


eel.spawn(usuario_input)

eel.init('web')

try:
    eel.start('index.html', size=(850,600), port=1000)   # python will select free ephemeral ports.
except (SystemExit, MemoryError, KeyboardInterrupt):
    print("Program Exit, Save Logs if Needed")