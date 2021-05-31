import json

import eel
from sholib import *

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


try:
    eel.start('index.html', size=(950,800), port=0)   #python will select free ephemeral ports.
except (SystemExit, MemoryError, KeyboardInterrupt):
    print ("Program Exit, Save Logs if Needed")