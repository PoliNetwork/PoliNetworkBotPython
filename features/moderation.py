import datetime

import variable
from config import creators, time_unit_values
from functions import utils


def mute_ban(update, context):
    bot = variable.updater.bot
    message = update.message
    command = message['text'].split(" ")[0].replace("/","")
    admins = bot.get_chat_administrators(message['chat']['id'])

    chat_id = message.chat_id

    admins = {admin["user"]['id']
              for admin in admins}

    sender = message.from_user['id']

    if not (sender in admins):
        utils.send_in_private_or_in_group("Comando vietato. Non sei admin.", chat_id, message.from_user)
        return


    if message.reply_to_message == None:
        utils.send_in_private_or_in_group("Devi rispondere al messaggio dell'utente che vuoi bannare per eseguire tale azione.", chat_id, message.from_user)
        return

    time = None

    receiver = message.reply_to_message.from_user['id']

    if len(message.text.split(" ")) > 1:
        time = float(datetime.datetime.now().timestamp()) + \
               time_unit_values.convert_time_in_seconds(" ".join(message.text.split(" ")[1:]))

    if command in "mute":
        bot.restrict_chat_member(chat_id, receiver, until_date = time)
    else:
        bot.kick_chat_member(chat_id, receiver, until_date = time)


def ban_all(update, context):
    message = update.message
    chat = message.chat
    if chat.id not in creators.owners:  # only owners can do this command
        return

    if message.reply_to_message == None:
        utils.send_in_private_or_in_group("Devi rispondere al messaggio dell'utente che vuoi bannare per eseguire tale azione.", chat_id, message.from_user)
        return

    receiver = message.reply_to_message.from_user['id']

    for group in variable.groups_list:
        variable.updater.bot.restrict_chat_member(chat.id, receiver)


