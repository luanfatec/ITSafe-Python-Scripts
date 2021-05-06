import requests
import json

session = requests.session()
header = {
    "content-type": "application/json"
}
dados = {
    "palpite": 0
}
r_comecar = requests.get("http://localhost:8081/api/comecar_jogo")

if r_comecar.json()["success"]:
    while True:
        dados["palpite"] = input("Adivinhe um numero: ")
        r_comecar = session.post("http://localhost:8081/api/adivinhe_o_numero", data=json.dumps(dados), headers=header)
        print(r_comecar.json())

else:
    print("Sem permissão para jogar")