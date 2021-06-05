# ----
import shodan
import requests
import json
from messages import *
import datetime


class ManipuleShodan(object):

    def __init__(self):
        self.agent = requests.session()
        self.API_KEY = ''
        self.NAME_PROJECT = ''
        self.SHODAN = ''
        self.SHODAN_API_LINK = ''

    # Função destinada a salvar os erros da aplicação
    def save_logs(self, msg, file, type_error):
        logs_global = ""
        with open(f"config/logs/{file}.log", "r") as f_logs:
            try:
                logs_file = f_logs.readlines()
                logs_file.append(f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}] | {type_error}: {msg}\n")
                logs_global = logs_file
            except Exception as msg:
                pass
            finally:
                f_logs.close()
        with open(f"config/logs/{file}.log", "w") as logs:
            try:
                logs.writelines(logs_global)
            except Exception as msg:
                pass
            finally:
                logs.close()

    # Carregando as urações do arquivo .json...
    def run_variables(self):
        user_data = {}
        with open("config/config.json", "r", encoding='utf8') as config:
            try:
                conf = json.load(config)
                for conf_v in conf['config']:
                    self.API_KEY = conf_v['API_KEY']
                    self.NAME_PROJECT = conf_v['NAME_PROJECT']
                    self.SHODAN = conf_v['SHODAN']
                    self.SHODAN_API_LINK = conf_v['SHODAN_API_LINK']
                    user_data['NAME_PROJECT'] = conf_v['NAME_PROJECT']
                    user_data['NAME'] = conf_v['NAME']
                    user_data['USERNAME'] = conf_v['USERNAME']
                    user_data['EMAIL'] = conf_v['EMAIL']
                    user_data['API_KEY'] = conf_v['API_KEY']
                    user_data['SHODAN_API_LINK'] = conf_v['SHODAN_API_LINK']
                    user_data['SHODAN'] = conf_v['SHODAN']
                    user_data['LINK_PROFILE'] = conf_v['LINK_PROFILE']
            except Exception as msg:
                return json.dumps({ "error": msg})

            finally:
                config.close()

        return json.dumps(user_data)

    # Atualização dos dados de configuração...
    def update_file_config(self, data_settings):
        config_datas = json.dumps(data_settings)
        save_confirm = True

        for data in data_settings['config']:
            print("73 Estou no for")
            if "@" not in data["EMAIL"]:
                print("75 estou no primeiro if")
                save_confirm = False
                self.save_logs(MessagesLogs().error_update_file_config_email, "errors", "Error updated")
                return json.dumps({"error": MessagesLogs().error_update_file_config_email})

            elif data["EMAIL"] == "" or len(data["EMAIL"]) == 0 or len(data["EMAIL"].split('@')[1]) < 7 or len(data["EMAIL"].split('@')[0]) == 0 or len(data["EMAIL"].split('@')[1]) == 0:
                print("79 estou no primeiro elif")
                save_confirm = False
                self.save_logs(MessagesLogs().error_update_file_config_email, "errors", "Error updated")
                return json.dumps({"error": MessagesLogs().error_update_file_config_email})

            else:
                with open("config/config.json", "w", encoding='utf8') as config:
                    print("70 Estou no with")
                    try:
                        if save_confirm:
                            print("84 Estou aqui no confirme")
                            config.write(str(config_datas))
                            self.save_logs(MessagesLogs().success_update_file_config, "success", "Success updated")
                            return json.dumps({"success": MessagesLogs().success_update_file_config})

                        else:
                            print("91 Estou aqui no else...")
                            return json.dumps({"error": MessagesLogs().error_update_file_config_email})

                    except Exception as msg:
                        print("95 Estou aqui no exception")
                        self.save_logs(msg, "errors", "Error exception")
                        return json.dumps({"error": MessagesLogs().error_update_file_config})

                    finally:
                        config.close()


    # Retornar todas as informações de crédito na conta do Shodan...
    def get_api_information(self):
        self.run_variables()
        info = self.agent.get(url=f"{self.SHODAN_API_LINK}/api-info?key={self.API_KEY}").text.strip()
        return info

    # Realiza uma pesquisa baseada em um CDIR.
    def get_net(self, search):
        if "/" in search:
            try:
                self.run_variables()
                shodanOBJ = shodan.Shodan(self.API_KEY)
                return shodanOBJ.search(search)
            except Exception as msg:
                self.save_logs(msg, "errors", "Search error")
                return {"error": MessagesLogs().search_error}
        else:
            return { "error": MessagesLogs().search_error }

    # Realiza uma busca e um ip determinado, retornando informações inportantes sobre o host.
    def get_info_ip(self, ip):
        try:
            self.run_variables()
            info = self.agent.get(url=f"{self.SHODAN_API_LINK}/shodan/host/{ip}?key={self.API_KEY}").text
            return info
        except Exception as msg:
            return { "error": msg }

    # Retornar uma lista de protocolo com informações sobre..
    def get_info_protocols(self):
        try:
            self.run_variables()
            info = self.agent.get(f"{self.SHODAN_API_LINK}/shodan/protocols?key={self.API_KEY}").text
            return info
        except Exception as msg:
            return { "error": msg }

    # Realiza uma reversão de ip para DNS.
    def reverse_dns(self, apis):
        try:
            self.run_variables()
            info = self.agent.get(f"{self.SHODAN_API_LINK}/dns/reverse?ips={apis}&key={self.API_KEY}").text
            return info
        except Exception as msg:
            return { "error": msg }

    # Realiza uma conversão de host para ip.
    def resolve_dns(self, hostnames):
        try:
            self.run_variables()
            info = self.agent.get(f"{self.SHODAN_API_LINK}/dns/resolve?hostnames={hostnames}&key={self.API_KEY}").text
            return info
        except Exception as msg:
            return { "error": msg }

    # Retorna uma lista de subdomios de determinado hostname.
    def get_subdomais(self, hostname):
        try:
            self.run_variables()
            info = self.agent.get(f"{self.SHODAN_API_LINK}/dns/domain/{hostname}?key={self.API_KEY}").text
            return info
        except Exception as msg:
            return { "error": msg }



if __name__=="__main__":
    test = ManipuleShodan()
    test.update_file_config({'NAME_PROJECT': 'Croshift Search', 'NAME': 'Nome do Usuário', 'EMAIL': 'email@example.com', 'USERNAME': 'username', 'SHODAN': 'https://www.shodan.io', 'SHODAN_API_LINK': 'https://api.shodan.io', 'LINK_PROFILE': 'https://avatars.githubusercontent.com/u/44438249?v=4', 'API_KEY': 'XyVljbUhatZ0Q4ejdXZgAEjOfn8PxQxk'})
    test.run_variables()