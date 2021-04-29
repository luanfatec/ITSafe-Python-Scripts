class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_pessoa(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} de idade.")

    def __str__(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} de idade."

    def __call__(self, *args, **kwargs):
        print("Isso é importante!")

    # Deletar
    def __del__(self):
        print("Terminando!")


pessoa1 = Pessoa("Luan", 20)
pessoa2 = Pessoa("Gaby", 19)

pessoa1.mostrar_pessoa()
pessoa2.mostrar_pessoa()

print(pessoa1)
print(pessoa2)
pessoa1()