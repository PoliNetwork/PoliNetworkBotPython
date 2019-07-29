import datetime
import json
import time
from json import JSONDecodeError
from threading import Thread

from telegram.error import Unauthorized

import bot


try:
    file = open("data/to_delete.json", encoding="utf-8")
    messages_list = json.load(file)
except (JSONDecodeError, IOError):
    messages_list = []


def escape(html):
    """Returns the given HTML with ampersands, quotes and carets encoded."""
    html = str(html)
    return html.replace('&', '&amp;').replace('<', '&lt;') \
        .replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')


def send_in_private_or_in_group(text, group_id, user):
    success = True
    user_id = user.id

    try:
        bot.updater.bot.send_message(user_id, text)
    except Unauthorized as e:
        success = False

    if success is True:
        return

    if user.username is not None and user.username != "":
        message_to = "@" + user.username
    else:
        nome = user['first_name']
        if user['last_name'] is not None and user['last_name'] != "":
            nome = nome + " " + user["last_name"]

        nome = str(escape(nome))
        message_to = "<a href='tg://user?id=" + str(user_id) + "'>" + nome + "</a>"

    text = "[Messaggio per " + message_to + "]\n\n" + text

    done2 = bot.updater.bot.send_message(group_id, text, parse_mode="HTML")

    j5on = {
        "group_id" : group_id,
        "message_id" : done2.message_id,
        "datetime" : str(datetime.datetime.now().timestamp())
    }

    messages_list.append(j5on)
    with open("data/to_delete.json", 'w', encoding="utf-8") as file:
        json.dump(messages_list, file)


class DeleteMessageThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            try:
                file = open("data/to_delete.json", encoding="utf-8")
                messages_list = json.load(file)
            except (JSONDecodeError, IOError):
                messages_list = []
                return

            for message in messages_list:
                difference = float(message['datetime']) - datetime.datetime.now().timestamp()
                if ((abs(difference)/60) > 5):
                    messages_list.remove(message)
                    bot.updater.bot.deleteMessage(chat_id=message['group_id'],
                                      message_id=message['message_id'])

            with open("data/to_delete.json", 'w', encoding="utf-8") as file:
                json.dump(messages_list, file)
            time.sleep(5)
