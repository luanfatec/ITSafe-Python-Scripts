import time
import requests


def get_num():
    req = requests.get("https://desafios.cysource.com.br/PYTHON/stage1.php")
    for line in req.text.split("<h3"):
        if 'class="text-center">' in line:
            cont = line.split("h3")[0].split("<")[0].split(">")[1]
            try:
                return eval(cont)
            except:
                print("error!")


def get_result(text):
    for line in text.split("<h4"):
        if "You did it!, go to stage2.php" in line:
            return line
        if "Vezes resolvido:" in line:
            return line.split(">")[1].split("<")[0]

count = 0
sessions = requests.session()

while True:
    time.sleep(2)
    data = { "chal":"stage1", "solution":f"{get_num()}"}
    resp = sessions.post("https://desafios.cysource.com.br/PYTHON/api.php", data=data)
    print(get_result(resp.text))

    count += 1
    if count == 5:
        break
