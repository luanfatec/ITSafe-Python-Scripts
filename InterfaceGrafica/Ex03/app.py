import eel
import random

palavra = []
resolucao = []
tentativas = 0

@eel.expose
def iniciar_jogo():
    global palavra
    palavra = list(random.choice(["paiva", "sinta", "mouse", "marte", "morta"]))
    for traco in range(0, len(palavra)):
        resolucao.append("_")
    return " . ".join(resolucao)

@eel.expose
def advinhar_letra(letra):
    global tentativas
    tentativas += 1
    if palavra.count(letra):
        for index, data in enumerate(palavra):
            if letra == data:
                resolucao[index] = data

    if resolucao.count("_") == 0:
        return f"Você acertou em {tentativas} tentativas. A palavra era '{''.join(palavra)}'."

    return resolucao


eel.init('web')

try:
    eel.start('index.html', size=(850,400), port=0)   #python will select free ephemeral ports.
except (SystemExit, MemoryError, KeyboardInterrupt):
    print ("Program Exit, Save Logs if Needed")