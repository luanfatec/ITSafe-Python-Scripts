import pytesseract
from PIL import Image
import string
import requests

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
url = "https://desafios.cysource.com.br/PYTHON/"
session = requests.session()



# text = pytesseract.image_to_string(Image.open('captcha2s.png'))
# return "".join(map(lambda data: data if data in string.ascii_letters or data in string.digits else "", text))

def puxar_captcha():
    path_img = ""
    r = session.get(url + "/stage2.php?level=2", stream=True) # Pode resolver o nivel 0 e 1 do stage2.

    for line in r.iter_lines():
        linha = str(line)
        if 'captcha_image' in linha:
            path_img = linha[linha.rfind('img'):linha.find("png")+3]

    r = session.get(url + path_img)
    with open("a.png", "wb") as file:
        file.write(r.content)

    with Image.open('a.png') as captcha_file:
        width, height = captcha_file.size

        for i in range(height):
            for k in range(width):
                if captcha_file.getpixel((k, i)) == (255, 255, 255):
                    captcha_file.putpixel((k, i), (0, 0, 0))
                else:
                    captcha_file.putpixel((k, i), (255, 255, 255))

        captcha_file.save("captcha2.png")
        captcha_file.close()

    text = pytesseract.image_to_string("captcha2.png").replace("\n", "")[:-1]
    return "".join(map(lambda data: data if data in string.ascii_letters or data in string.digits else "", text))



def enviar_code():
    heads = {"Content-Type": "application/x-www-form-urlencoded"}
    r = session.post(url + "api.php", data="captcha={0}&chal=stage2&level=2".format(puxar_captcha()), headers=heads)
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
print(f"Tentativas: {cont}")