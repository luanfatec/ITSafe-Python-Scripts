import time
import string
from random import choice
from PIL import Image
from io import BytesIO
import pytesseract
import requests

""" !!!
    Com esse script, pode ser resolvido o nivel 0 e nivel 1 do stage2.
"""

def get_image_name(text_page):
    for line in text_page.split("<center>"):
        for line2 in line.split():
            if "src" in line2:
                if "</center" in line2:
                    return line2.split(">")[0].split('"')[1]

def write_image(text_image, name_image):
    try:
        with open(name_image, 'w') as img:
            img.write(text_image)
            return True
    except:
        return False

def get_code(url_path_image, id=0):
    page = session.get(f"{url_path_image}/stage2.php?level={id}")  # Get page content
    img_path = f"{url_path_image}/{get_image_name(page.text)}"  # Get url path image
    img = requests.get(url=img_path)  # Get image bytes.
    return pytesseract.image_to_string(Image.open(BytesIO(img.content))).strip()


def send_code(url_path_image="", str_code="", id=0, message=""):
        time.sleep(3)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        resp = session.post(f"{url_path_image}/api.php", data=f"captcha={str_code}&chal=stage2", headers=headers)
        print(f"{url_path_image}/stage2.php?level={id}")

        if message in resp.text:
            print(resp.content)
            return True



def gera_string(max=0):
    pwd = []
    for crt in range(max):
        pwd += choice(f"{string.ascii_lowercase}{string.ascii_uppercase}")

    return "".join(pwd)


session = requests.session()
# Configure url path site.
url_path = "https://desafios.cysource.com.br/PYTHON"
# Configure path pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if "__main__" == __name__ :
    while True:
        if send_code(url_path_image=url_path, str_code=get_code(url_path, id=1), id=1, message="to continue"):
            break
