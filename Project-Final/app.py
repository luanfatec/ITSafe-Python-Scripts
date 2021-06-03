import json

import eel
from sholib import *
import json

eel.init('web')

@eel.expose
def get_api_information():
    return ManipuleShodan().get_api_information()

@eel.expose
def get_net(rede):
    return ManipuleShodan().get_net(f"net:{rede}")

@eel.expose
def get_info_ip(ip):
    return ManipuleShodan().get_info_ip(f"{ip}")

@eel.expose
def get_info_protocols():
    return ManipuleShodan().get_info_protocols()

@eel.expose
def reverse_dns(apis):
    return ManipuleShodan().reverse_dns(f"{apis}")

@eel.expose
def resolve_dns(hostname):
    return ManipuleShodan().resolve_dns(f"{hostname}")

@eel.expose
def get_subdomais(hostname):
    return ManipuleShodan().get_subdomais(f"{hostname}")

# Routa para carregamento das informações de usuário
@eel.expose
def load_config_user():
    return ManipuleShodan().run_variables()

# Rota de atualização de configurações
@eel.expose
def update_settings_user(data_config):
    ManipuleShodan().update_file_config({
        "config": [
            data_config
        ]
    })

if __name__ == "__main__":
    update_settings_user({"teste": "teste"})

if __name__ != "__main":
    try:
        eel.start('index.html', size=(950,800), port=0)   #python will select free ephemeral ports.
    except (SystemExit, MemoryError, KeyboardInterrupt):
        print ("Program Exit, Save Logs if Needed")

