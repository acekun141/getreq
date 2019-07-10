import requests
import time
import json
import bot
from bot import telegram_bot


with open('config.json') as config_file:
    data = json.load(config_file)

list_urls = [
    {
        'link':'http://127.0.0.1:8000/Page1',
        'name':'Page1'
    },
    {
        'link':'http://127.0.0.1:8000',
        'name':'HomePage'
    }
]

def start():
    print("Running...")
    new_bot = telegram_bot(data['bot_token'],data['bot_chatID'])
    # offset = new_bot.get_update()[-1]['update_id']
    while True:
        # list_data_bot = new_bot.get_update_with_offset(offset)
        # if len(list_data_bot) > 1:
        #     offset += 1
        #     list_data_bot = new_bot.get_update_with_offset(offset)
        #     for data_bot in list_data_bot:
        #         if data_bot['message']['chat']['id'] == new_bot.groupID:
        #             offset = data_bot['update_id']
        #             if new_bot.check_message(data_bot['message']['text']):
        #                 if data_bot['message']['text'][5:] == 'show':
        #                     for i in range(len(list_urls)):
        #                         msg = '{}. Link: {} - Name: {}'.format(i+1,list_urls[i]['link'],list_urls[i]['name'])
        #                         new_bot.send_message(msg)
        for url in list_urls:
            try:
                req = requests.get(url['link'])
                if req.status_code != 200:
                    new_bot.send_message('Warning: Status code of {} is {}'.format(url['name'],req.status_code))
                    pass
            except Exception as value:
                new_bot.send_message('Exception: {}'.format(value))
                pass
        time.sleep(10)
if __name__ == "__main__":
    try:
        start()
    except Exception as value:
        print(value)