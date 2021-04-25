# ------------- Formas de apresentação de dados ------------- #
luan = {
    "name":"Luan Santos",
    "idade":20
}
print("Meu nome é "+luan['name']+" e tenho "+str(luan['idade'])+" de idade.")
print("Meu nome é {0} e tenho {1} de idade.".format(luan['name'], str(luan['idade'])))
print(f"Meu nome é {luan['name']} e tenho {str(luan['idade'])} de idade.") # mais recente