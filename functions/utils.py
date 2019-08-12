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
            updated += 1
            variable.updater.bot.deleteMessage(chat_id=message['group_id'],
                                               message_id=message['message_id'])
    if updated > 0:  # array is changed and so we need to update the file
        with open("data/to_delete.json", 'w', encoding="utf-8") as file_to_write:
            json.dump(messages_list_to_delete, file_to_write)

    variable.lock_to_delete.release()


class DeleteMessageThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            DeleteMessageThread2()
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
    if text is None or text == "":
        return True

    t = text.split(" ")
    for word in t:
        if (str(word)).lower() in blacklist_words.blacklist_words:
            return False
    return True


def mute_and_delete(message):
    chat = message.chat
    user = message.from_user.id
    variable.updater.bot.restrict_chat_member(chat.id,
                                              user,
                                              until_date=int(datetime.datetime.now().timestamp()) + 900)
    variable.updater.bot.delete_message(chat_id=chat.id, message_id=message.message_id)


def has_spam_links(text):
    t = text.split(" ")
    for word in t:
        for banned_site in blacklist_words.blacklist_sites:
            if word.find(banned_site) >= 0:
                return True

    return False


def has_spam_mention(text):
    t = text.split(" ")
    for word in t:
        if word.startswith("@") and word not in blacklist_words.allowed_tags:
            try:
                chat = variable.updater.bot.get_chat(word)
                if chat.type != "private":
                    return True
            except Exception as e:
                pass

    return False


def is_spam(text):
    if text is None or text == "":
        return False

    text = str(text).lower()

    has_link = text.find("http")
    if has_link >= 0:
        is_spam_link = has_spam_links(text)
        if is_spam_link:
            return True

    has_mention = text.find("@")
    if has_mention >= 0:
        is_spam_mention = has_spam_mention(text)
        if is_spam_mention:
            return True

    return False


def leave_chat(chat):
    text = "Solo gli amministratori di @PoliNetwork possono aggiungermi ai gruppi!" \
           " Sono uscito dal gruppo. Contatta gli amministratori."
    variable.updater.bot.send_message(chat.id, text)
    variable.updater.bot.leave_chat(chat.id)
