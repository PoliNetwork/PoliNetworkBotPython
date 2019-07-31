import datetime

import variable
from config import creators
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


def find_user(new_chat_members, to_find):
    for user in new_chat_members:
        if user.id == to_find:
            return True
    return False


def check_if_exit(message):
    if message.new_chat_members is None or len(message.new_chat_members) == 0:
        return False

    is_present = find_user(message.new_chat_members, creators.me)
    if is_present is False:
        return False

    admins = variable.updater.bot.get_chat_administrators(message.chat.id)
    if groups.creator_is_present(admins):
        return False

    return True  # we are not admins of this group, bot should exit


def check_message(update, context):
    message = update.message

    to_exit = check_if_exit(message)
    if to_exit is True:
        variable.updater.bot.leave_chat(message.chat.id)
        return

    groups.try_add_group(message)
    check_blacklist(message)
