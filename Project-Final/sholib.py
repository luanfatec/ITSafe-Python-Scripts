# ----
import shodan
import requests
import json


class ManipuleShodan(object):

    def __init__(self):
        self.agent = requests.session()
        self.API_KEY = ""
        self.NAME_PROJECT = ""
        self.SHODAN = ""
        self.SHODAN_API_LINK = ""

    # Carregando as urações do arquivo .json...
    def _variables(self):
        with open("config/config.json", "r+", encoding='utf8') as config:
            conf = json.load(config)
            for conf_v in conf['config']:
                self.API_KEY = conf_v['API_KEY']
                self.NAME_PROJECT = conf_v['NAME_PROJECT']
                self.SHODAN = conf_v['SHODAN']
                self.SHODAN_API_LINK = conf_v['SHODAN_API_LINK']
            config.close()

    # Retornar todas as informações de crédito na conta do Shodan...
    def get_api_information(self):
        self._variables()
        info = self.agent.get(url=f"{self.SHODAN_API_LINK}/api-info?key={self.API_KEY}").text.strip()
        return info

    # Realiza uma pesquisa baseada em um CDIR.
    def get_net(self, search):
        self._variables()
        shodanOBJ = shodan.Shodan(self.API_KEY)
        return shodanOBJ.search(search)

    # Realiza uma busca e um ip determinado, retornando informações inportantes sobre o host.
    def get_info_ip(self, ip):
        self._variables()
        info = self.agent.get(url=f"{self.SHODAN_API_LINK}/shodan/host/{ip}?key={self.API_KEY}").text
        return info

    # Retornar uma lista de protocolo com informações sobre..
    def get_info_protocols(self):
        self._variables()
        info = self.agent.get(f"{self.SHODAN_API_LINK}/shodan/protocols?key={self.API_KEY}").text
        return info

    # Realiza uma reversão de ip para DNS.
    def reverse_dns(self, apis):
        self._variables()
        info = self.agent.get(f"{self.SHODAN_API_LINK}/dns/reverse?ips={apis}&key={self.API_KEY}").text
        return info

    # Realiza uma conversão de host para ip.
    def resolve_dns(self, hostnames):
        self._variables()
        info = self.agent.get(f"{self.SHODAN_API_LINK}/dns/resolve?hostnames={hostnames}&key={self.API_KEY}").text
        return info

    # Retorna uma lista de subdomios de determinado hostname.
    def get_subdomais(self, hostname):
        self._variables()
        info = self.agent.get(f"{self.SHODAN_API_LINK}/dns/domain/{hostname}?key={self.API_KEY}").text
        return info



if __name__=="__main__":
    test = ManipuleShodan()
    print(test.get_api_information())