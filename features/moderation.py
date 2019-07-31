import datetime

import variable
from config import creators, time_unit_values
from functions import utils


def is_a_number(s):
    try:
        return isinstance(int(s), int)
    except ValueError as e:
        return False


def mutes_bans_handler(update, context):
    bot = variable.updater.bot
    message = update.message
    command = message['text'].split(" ")[0].replace("/", "")
    admins = bot.get_chat_administrators(message['chat']['id'])

    chat_id = message.chat_id

    admins = {admin["user"]['id']
              for admin in admins}

    sender = message.from_user['id']

    if not (sender in admins):
        utils.send_in_private_or_in_group("Comando vietato. Non sei admin.", chat_id, message.from_user)
        return

    if message.reply_to_message is None:
        utils.send_in_private_or_in_group("Devi rispondere al messaggio dell'utente "
                                          "che vuoi bannare per eseguire tale azione.",
                                          chat_id, message.from_user)
        return

    time = None

    receiver = message.reply_to_message.from_user['id']

    if len(message.text.split(" ")) > 1:
        time_to_add = message.text.split(" ")[1]
        unit_of_measure = message.text.split(" ")[2]
        if is_a_number(time_to_add):
            time = float(datetime.datetime.now().timestamp()) + \
                   float(time_to_add) * time_unit_values.convert_time_in_seconds(unit_of_measure)
        else:
            utils.send_in_private_or_in_group("Hai inserito un valore non numerico.", chat_id, message.from_user)

    if command in "mute":
        bot.restrict_chat_member(chat_id, receiver, until_date=time,
                                 can_add_web_page_previews=False,
                                 can_send_media_messages=False,
                                 can_send_messages=False,
                                 can_send_other_messages=False)
    if command in "unmute":
        bot.restrict_chat_member(chat_id, receiver,
                                 can_add_web_page_previews=True,
                                 can_send_media_messages=True,
                                 can_send_messages=True,
                                 can_send_other_messages=True)
    if command in "ban":
        bot.kick_chat_member(chat_id, receiver, until_date=time)
    if command in "unban":
        bot.unban_chat_member(chat_id, receiver)


def ban_all(update, context):
    message = update.message
    chat = message.chat
    chat_id = chat.id
    if chat_id not in creators.owners:  # only owners can do this command
        return

    if message.reply_to_message is None:
        utils.send_in_private_or_in_group(
            "Devi rispondere al messaggio dell'utente che vuoi bannare per eseguire tale azione.", chat_id,
            message.from_user)
        return

    receiver = message.reply_to_message.from_user['id']

    for group in variable.groups_list:
        variable.updater.bot.restrict_chat_member(group['id'], receiver)
