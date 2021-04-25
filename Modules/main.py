import os

"""
# os.system("ipconfig")
# print(os.system("ipconfig") # Ao final do resoltado é exibido uma flag 0 indicando que deu certo o camando.
# print(os.popen("ipconfig").read()) # a saída desse comando é retornada, podendo guardar uma uma variável apenas ou imprimir com print.
"""

"""
# os.system("dir") # Retorna o diretório atual, onde está o arquivo python.
#os.chdir("C:\\") # Configura um diretódio para trabalho (Localidade onde deve ser executado o comando).
# os.system("dir") # Após configurar o diretório de trabalho, irá trabalhar no diretório onde foi configurado acima sendo ele o C:\\.
"""

# print(os.listdir("c:\\"))
# print(os.getcwd()) Busca o diretório atual onde está o script.
# os.remove("remove.txt") # Remove determinado arquivo.
"""
if os.path.isfile("testes.txt"):
    print("Arquivo existente!")
else:
    print("Arquivo não existente!")
"""

print(os.path.getsize("teste.txt")) # Exibe o tamanho do arquivo.