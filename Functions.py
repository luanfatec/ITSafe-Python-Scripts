import os
import re
import requests


def hello():
    text = input("Whats your name? ")
    print(f"Hello {text}!!!")


def soma(n1, n2, n3):
    result = n1 + n2 + n3
    print(f"A soma entre {n1},{n2},{n3} é: {result}")


#
# Funções avançadas com args e kwargs + exercício de funções
help_error = """
Error: Argument invalid! 
Plese use --print-args or --none.
See before you need help, type -h, --help.
"""


def test_args(arg_type, *args):
    if arg_type == "--print-args":
        if args is not None:
            for arg in args:
                print(arg)
    elif args == "--none":
        print("You have not entered any printable arguments!")

    elif arg_type is None:
        print(help_error)
    elif len(args) == 0:
        print("You have not entered any printable arguments!")

    else:
        print(help_error)


def test_kwargs(**kwargs):
    for ag in kwargs.values():
        print(ag)

    if "acao" in kwargs.keys():
        if kwargs["acao"] == "soma":
            print(kwargs["n1"] + kwargs["n2"])


def exec_actions():
    actions = []
    for idx in range(5):
        command = str(input(f"Entre com o comando {idx}: "))
        actions.append(command)

    for cmd in actions:
        print(os.popen(cmd).read())

def getip():
    ipcnf = os.popen("ipconfig").read()
    # print(re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", ipcnf)) # Trouxe todos os ips que encontrou na saida do ipconfig.
    for ips in re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", ipcnf): print(ips)

def getioreso():
    ipcnf = os.popen("ipconfig").readlines()
    for item in ipcnf:
        if "Endereço IPv4." in item or "Endere‡o IPv4" in item:
            print(item[49:])
            break

def get_mails():
    resp = requests.get("https://www.sanofi.com.br/pt/fale-conosco").text
    separe_tags = re.findall(r'<[liank] href=".+">', resp, flags=re.I)
    for item in separe_tags:
        separe_hrefs = re.findall(r'[http|https](.*)', item, flags=re.I)
        for item in separe_hrefs:
            print(item)

# Treinamento de Regex(Expressões regulares).
def tut_regex():
    # "| - Significa OU"
    # ". - Qualquer outro caractere(Com exceção de quebra de linha)"
    # "[] - Conjunto de caracteres"
    # "* - 0 ou N(Ilimitada as vezes)."
    # "+ - 0 ou N(Ilimitada as vezes)."
    # "? - 0 ou 1."
    # "{n} - Qualquer quantidade de vezes."
    # "{mim, max} - De inicio a fim."
    # "{10,} - 10 ou mais."
    # "{,10} - de 0 a 10."
    # "{10} - Especificamente 10."
    # "{5,10} - de 5 a 10."
    # "()+ [a-zA-Z0-9]+"
    # "() - Grupo(Engloba um grupo de determinada expressão)."
    # "^ - Começa com."
    # "$ - Termina com."
    # "[^a-z] - Negação."
    # "\w - engloba toda a expressão [a-zA-Z0-9Á-ú_] e muito mais."
    # "\w -> [a-zA-Z0-9Á-ú_] -> re.A ou re.ASCII."
    # "\W -> [^a-zA-Z0-9Á-ú_]"
    # "\d -> [0-9]"
    # "\D -> [^0-9]"
    # "\s -> [\r\n\f\t] - Qualquer tipo de espaço."
    # "\S -> [^\r\n\f\t] - Nega qualquer tipo de espaço."
    # "\b -> Borda."
    # "\B -> Não Borda."
    #
    # "re.A ou re.ASCII -> faz buscas utilizando a tabela ascii."
    # "re.I ou re.IGNORECASE"
    # "re.M ou re.MULTILINE -> aplicado em ^ e $"
    # "re.S -> Dotall -> \n."

    texto = '''
    João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
    Maria era o nome dela.
    Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
    maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
    domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
    pão de queijo.
    Não canso de ouvir a Maria:
    "Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
    '''

    # print(re.findall(r"João|Maria|mineira|Não|não", texto))
    # print(re.findall(r"o...r", texto))
    # print(re.findall(r"[Jj]oão|[Mm]aria", texto))
    # print(re.findall(r"[a-zA-Z]aria", texto))
    # print(re.findall(r"[a-zA-Z]arIa", texto, flags=re.IGNORECASE))
    # print(re.findall(r"[a-zA-Z]aria", texto))

    # print(re.findall(r"jO+ÃO+", texto, flags=re.IGNORECASE))
    # print(re.sub(r"jO{1,}ÃO{1,}", "Luan", texto, flags=re.IGNORECASE))
    # print(re.findall(r"ve{3}m{1,2}", texto, flags=re.IGNORECASE))
    # print(re.sub(r"jO{1,}ÃO{1,}", "Luan", texto, flags=re.IGNORECASE))

    """texto2 = "Luan ama ser amado"
    print(re.findall(r"ama[do]{2}", texto2, flags=re.IGNORECASE))
    print(re.findall(r"", texto2, flags=re.IGNORECASE))"""

    text03 = """
    <p>Minha frase 1</p> <p>Minha frase 2</p> <p>Minha frase 3</p> <div>Minha frase 4</div>
    """
    # print(re.findall(r"<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>", text03))
    # tags = re.findall(r"(<([dpiv]{1,3})>(.+?)<\/\2>)", text03)

    # for i in tags:
    #     um, dois, tres = i
    #     print(tres)

    # tags = re.findall(r"<([dpiv]{1,3})>(?:.+?)<\/\1>", text03)
    # tags = re.findall(r"<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>", text03) # Nomeando grupos de expressões.
    # print(tags)

    # print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1\3\4', text03))

    cpf = "145.758.856-95sasasas"
    # print(re.findall(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}", cpf))
    # print(re.findall(r"((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})", cpf)) # Multiplicando grupo de expressão.
    # print(re.findall(r"^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$", cpf))
    # print(re.findall(r"[^0-9a-zA-Z.-]+", cpf))


    # // Flags
    # print(re.findall(r"[a-z]+", texto, flags=re.IGNORECASE))
    # print(re.findall(r"[a-zA-Z0-9Á-ú]+", texto, flags=re.IGNORECASE))

    # print(re.findall(r"\w+", texto, flags=re.IGNORECASE)) # "\w" engloba toda a expressão "[a-zA-Z0-9Á-ú]".
    # print(re.findall(r"\W+", texto, flags=re.ASCII)) # Busca apenas o que está na tabela ASCII.

    # print(re.findall(r"\w+", texto, flags=re.I))
    # print(re.findall(r"\W+", texto, flags=re.I))

    # print(re.findall(r"\d+", texto, flags=re.I)) # Busca apenas numeros.
    # print(re.findall(r"\D+", texto, flags=re.I)) # Inverso do \d.

    # print(re.findall(r"\s+", texto, flags=re.I)) # Busca todo tipo de espaço incluindo quebra de linhas.
    # print(re.findall(r"\S+", texto, flags=re.I)) # Busca tudo que não é espaço.

    # print(re.findall(r"\bf\w+", texto, flags=re.I)) # Todas as palavras que começam com determinada regra.
    # print(re.findall(r"\w+te\b", texto, flags=re.I)) # Todas as palavras que terminam com determinada regra.
    # print(re.findall(r"\b\w{4}\b", texto, flags=re.I))
    # print(re.findall(r"flores\B", texto, flags=re.I))

    texto04 = '''
    131.768.460-53 ABC
    055.123.060-50 DEF
    955.123.060-90
    '''
    # print(re.findall(r"\d{3}.\d{3}.\d{3}-\d{2}", texto04))
    # print(re.findall(r"^\d{3}.\d{3}.\d{3}-\d{2}$", texto04, flags=re.M))

    # texto05 = "O Luan é demais e gosta muito de \n estudar programação"
    # print(re.findall(r"^o.*o$", texto05, flags=re.I | re.S))

    texto = '''
    ONLINE  192.168.0.1 GHIJK active
    OFFLINE  192.168.0.2 GHIJK inactive
    OFFLINE  192.168.0.3 GHIJK active
    ONLINE  192.168.0.4 GHIJK active
    ONLINE  192.168.0.5 GHIJK inactive
    OFFLINE  192.168.0.6 GHIJK active
    '''