import time
import requests
import json

with open('config.json') as config_file:
    data = json.load(config_file)

class telegram_bot:
    def __init__(self, token, groupID):
        self.token = token
        self.groupID = groupID

    def send_message(self,msg):
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + str(self.groupID) + '&parse_mode=Markdown&text=' + msg
        response = requests.get(send_text)
        return response.json()
    
    # def get_update(self):
    #     link_update = 'https://api.telegram.org/bot' + self.token + "/getUpdates"
    #     return json.loads(requests.get(link_update).text)['result']

    # def get_update_with_offset(self,offset):
    #     link_update = 'https://api.telegram.org/bot' + self.token + "/getUpdates" + "?offset=" + str(offset)
    #     return json.loads(requests.get(link_update).text)['result']

    # def get_height(self,data):
    #     return len(data['result'])
    
    # def check_message(self,msg,bot='bot->'):
    #     if bot == msg[:5]:
    #         return True
    #     else:
    #         return False
    
            
