import datetime

import variable
from features import groups
from functions import utils


def check_blacklist(message):
    chat = message.chat

    if chat.type == "private":
        return
    text = message.text

    is_valid = utils.is_valid(text)

    if is_valid is False:
        user = message.from_user.id
        variable.updater.bot.restrict_chat_member(chat.id,
                                                  user,
                                                  until_date=int(datetime.datetime.now().timestamp()) + 900)
        variable.updater.bot.delete_message(chat_id=chat.id, message_id=message.message_id)
        return


def check_message(update, context):
    message = update.message
    groups.try_add_group(message)

    check_blacklist(message)
