import requests, json


"""r = requests.get("http://localhost:1337/api/visitas")
for item in range(10):
    cookie = {
        r.headers["set-cookie"].split()[0].split("=")[0]: r.headers["set-cookie"].split()[0].split("=")[1]
    }
    print(cookie)

    r = requests.get("http://localhost:1337/api/visitas", cookies=cookie)
    print(r.json())
    input(">>> ")"""


"""r = requests.get("http://localhost:1337/api/visitas")
# print(r.text)
# print(r.headers)
# print(r.url)
# print(r.json())
# print(r.content)
# print(r.status_code)"""


"""session = requests.session()
for item in range(10):
    response = session.get("http://localhost:1337/api/visitas")
    print(response.text)"""

def get_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("logo_new.png", 'wb') as f:
            f.write(response.content)

get_image("https://cysource.com.br/img/logo_new.png")
