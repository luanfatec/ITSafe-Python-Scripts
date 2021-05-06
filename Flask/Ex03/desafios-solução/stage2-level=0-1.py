import pytesseract
import requests


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
url = "https://desafios.cysource.com.br/PYTHON/"
session = requests.session()

def puxar_captcha():
    path_img = ""
    r = session.get(url + "/stage2.php?level=1", stream=True) # Pode resolver o nivel 0 e 1 do stage2.
    for line in r.iter_lines():
        linha = str(line)
        if 'captcha_image' in linha:
            path_img = linha[linha.rfind('img'):linha.find("png")+3]

    r = session.get(url + path_img)
    with open("a.png", "wb") as file:
        file.write(r.content)
    return pytesseract.image_to_string("a.png").replace("\n", "")[:-1]


def enviar_code():
    heads = {"Content-Type": "application/x-www-form-urlencoded"}
    r = session.post(url + "api.php", data="captcha={0}&chal=stage2&level=0".format(puxar_captcha()), headers=heads)
    if "You did" in r.text:
        print(r.text)
        return True
    else:
        return False

cont = 0
while True:
    cont += 1
    if enviar_code():
        break


print(f"Tentativas: {cont}")