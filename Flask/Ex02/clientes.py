import time
import requests
from twilio.rest import Client


url = "http://127.0.0.1:1337/index.html"
site_antigo = ""
r = requests.get(url)
site_antigo = r.text

while True:
    time.sleep(1)
    r = requests.get(url)
    if site_antigo != r.text:
        account_sid = "AC871cd6aa83f6f08519baa151b038be3d"
        auth_token = "cb12a570fc539a796e80a19c24816e56"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Olá professor, não resistir, sou apenas um aluno seu!!!",
            from_='+12069666162',
            to='+972528966884'
        )

        print(message.sid)
        break