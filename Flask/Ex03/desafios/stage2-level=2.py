import requests
from io import BytesIO
from PIL import Image
import pytesseract


session = requests.session()
url_path = "https://desafios.cysource.com.br/PYTHON"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def get_image_name(text_page):
    for line in text_page.split("<center>"):
        for line2 in line.split():
            if "src" in line2:
                if "</center" in line2:
                    return line2.split(">")[0].split('"')[1]


def get_code(url_path_image="", id=0):
    page = session.get(f"{url_path_image}/stage2.php?level={id}")  # Get page content
    img_path = f"{url_path_image}/{get_image_name(page.text)}"  # Get url path image
    # img = requests.get(url=img_path)  # Get image bytes.
    # image_bytes = Image.open(BytesIO(img.text))
    # print(image_bytes.size())
    # print(pytesseract.image_to_string(Image.open(BytesIO(img.text))))


print(get_code(url_path_image=url_path, id=2))