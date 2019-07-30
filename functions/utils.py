import datetime
import json
import time
from json import JSONDecodeError
from threading import Thread

from telegram.error import Unauthorized

import variable
from config import blacklist_words

try:
    file = open("data/to_delete.json", encoding="utf-8")
    messages_list_to_delete = json.load(file)
except (JSONDecodeError, IOError):
    messages_list_to_delete = []


def escape(html):
    """Returns the given HTML with ampersands, quotes and carets encoded."""
    html = str(html)
    return html.replace('&', '&amp;').replace('<', '&lt;') \
        .replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')


def add_message_to_delete(group_id, done2):
    global messages_list_to_delete

    j5on = {
        "group_id": group_id,
        "message_id": done2.message_id,
        "datetime": str(datetime.datetime.now().timestamp())
    }
    variable.lock_to_delete.acquire()
    messages_list_to_delete.append(j5on)
    with open("data/to_delete.json", 'w', encoding="utf-8") as file_to_write:
        json.dump(messages_list_to_delete, file_to_write)
    variable.lock_to_delete.release()


def send_in_private_or_in_group(text, group_id, user):
    success = True
    user_id = user.id

    try:
        variable.updater.bot.send_message(user_id, text)
    except Unauthorized as e:
        success = False

    if success is True:
        return

    message_to = get_user_mention(user)

    text = "[Messaggio per " + message_to + "]\n\n" + text

    done2 = variable.updater.bot.send_message(group_id, text, parse_mode="HTML")
    add_message_to_delete(group_id, done2)


def DeleteMessageThread2():
    global messages_list_to_delete

    variable.lock_to_delete.acquire()

    updated = 0
    for message in messages_list_to_delete:
        difference = float(message['datetime']) - datetime.datetime.now().timestamp()
        if (abs(difference) / 60) > 5:
            messages_list_to_delete.remove(message)
            updated = updated + 1
            variable.updater.bot.deleteMessage(chat_id=message['group_id'],
                                               message_id=message['message_id'])
    if updated > 0:  # array is changed and so we need to update the file
        with open("data/to_delete.json", 'w', encoding="utf-8") as file_to_write:
            json.dump(messages_list_to_delete, file_to_write)

    variable.lock_to_delete.release()

    time.sleep(5)


class DeleteMessageThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            DeleteMessageThread2()


def get_user_mention(user):
    if user.username is not None and user.username != "":
        return "@" + user.username
    else:
        nome = user['first_name']
        if user['last_name'] is not None and user['last_name'] != "":
            nome = nome + " " + user["last_name"]

        nome = str(escape(nome))
        return "<a href='tg://user?id=" + str(user.id) + "'>" + nome + "</a>"


def send_file_in_private_or_warning_in_group(user, document, group_id, title):
    success = True
    user_id = user.id

    if title is None or title == "":
        title = "[No title]"

    caption = escape("Review: " + title)
    try:
        variable.updater.bot.send_document(chat_id=user_id, document=document, caption=caption)
    except Unauthorized as e:
        success = False

    if success is True:
        return

    message_to = get_user_mention(user)

    text = message_to + ", devi prima scrivermi in privato per ricevere ciò che hai chiesto!"

    done2 = variable.updater.bot.send_message(group_id, text, parse_mode="HTML")
    add_message_to_delete(group_id, done2)


def is_valid(text):
    t = text.split(" ")
    for word in t:
        if (str(word)).lower() in blacklist_words.blacklist_words:
            return False
    return True
