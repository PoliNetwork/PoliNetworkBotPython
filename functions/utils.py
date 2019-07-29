import datetime
import json
import time
from json import JSONDecodeError
from threading import Thread, Lock

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


lock = Lock()


def add_message_to_delete(group_id, done2):
    global lock
    global messages_list

    j5on = {
        "group_id": group_id,
        "message_id": done2.message_id,
        "datetime": str(datetime.datetime.now().timestamp())
    }
    lock.acquire()
    messages_list.append(j5on)
    with open("data/to_delete.json", 'w', encoding="utf-8") as file_to_write:
        json.dump(messages_list, file_to_write)
    lock.release()


def send_in_private_or_in_group(text, group_id, user):
    success = True
    user_id = user.id

    try:
        bot.updater.bot.send_message(user_id, text)
    except Unauthorized as e:
        success = False

    if success is True:
        return

    message_to = get_user_mention(user)

    text = "[Messaggio per " + message_to + "]\n\n" + text

    done2 = bot.updater.bot.send_message(group_id, text, parse_mode="HTML")
    add_message_to_delete(group_id, done2)


class DeleteMessageThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global messages_list
        global lock
        while True:

            lock.acquire()
            for message in messages_list:
                difference = float(message['datetime']) - datetime.datetime.now().timestamp()
                if (abs(difference) / 60) > 5:
                    messages_list.remove(message)
                    bot.updater.bot.deleteMessage(chat_id=message['group_id'],
                                                  message_id=message['message_id'])

            with open("data/to_delete.json", 'w', encoding="utf-8") as file_to_write:
                json.dump(messages_list, file_to_write)
            lock.release()

            time.sleep(5)


def get_user_mention(user):
    if user.username is not None and user.username != "":
        return "@" + user.username
    else:
        nome = user['first_name']
        if user['last_name'] is not None and user['last_name'] != "":
            nome = nome + " " + user["last_name"]

        nome = str(escape(nome))
        return "<a href='tg://user?id=" + str(user.id) + "'>" + nome + "</a>"


def send_file_in_private_or_warning_in_group(user, document, group_id):
    success = True
    user_id = user.id

    try:
        bot.updater.bot.send_document(user_id, document)
    except Unauthorized as e:
        success = False

    if success is True:
        return

    message_to = get_user_mention(user)

    text = message_to + ", devi prima scrivermi in privato per ricevere ciò che hai chiesto!"

    done2 = bot.updater.bot.send_message(group_id, text, parse_mode="HTML")
    add_message_to_delete(group_id, done2)
