import datetime

import variable
from config import creators, time_unit_values


def mute(update, context):
    bot = variable.updater.bot
    message = update.message
    admins = bot.get_chat_administrators(message['chat']['id'])

    chat_id = message.chat_id

    admins = {admin["user"]['id']
                        for admin in admins}

    sender = message.from_user['id']

    if message.reply_to_message is None:
        return

    receiver = message.reply_to_message.from_user['id']

    if not (sender in admins):
        return

    time = time_unit_values.convert_time_in_seconds(message.text.split(" ")[1:])

    bot.restrict_chat_member(chat_id, receiver, until_date=datetime.datetime.now().timestamp() + time)

def ban(update, context):
    # todo: ban user of replied message
    # todo: check if the one that is using the command is admin
    return None


def ban_all(update, context):
    message = update.message
    chat = message.chat
    if chat.id not in creators.owners:  # only owners can do this command
        return

    # todo: ban user from all groups.
