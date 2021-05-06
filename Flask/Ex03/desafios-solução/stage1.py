import requests
import numexpr


url_d = "https://desafios.cysource.com.br/PYTHON/stage1.php"
session = requests.session()

def get_equal():
    r = session.get(url_d, stream=True)
    for line in r.iter_lines():
        linha = str(line)
        if '<h3 class="text-center">' in linha:
            return  linha[linha.rfind(" ")+1:linha.find("</h3>")]


def resolv_challenge(solucao, api_resolv):
    r = session.post(api_resolv, data=f"solution={solucao}&chal=stage1", stream=True, headers={"content-type":"application/x-www-form-urlencoded"})
    for line in r.iter_lines():
        linha = str(line)
        if 'resolvido:' in linha or "You" in linha:
            print(linha)


api_resolv = "https://desafios.cysource.com.br/PYTHON/api.php"

for i in range(6):
    try:
        desafio = get_equal()
        solucao = numexpr.evaluate(desafio)
        resolv_challenge(solucao, api_resolv)

    except:
        pass