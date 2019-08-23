import datetime

import variable
from config import creators
from features import groups
from functions import utils


def check_blacklist(message):
    chat = message.chat

    if chat.type == "private":
        return

    is_valid = utils.is_valid(message.text)

    if is_valid is False:
        utils.mute_and_delete(message)
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

    chat = message['chat']
    group_already_present, group_found = groups.find(chat['id'])
    if group_already_present is True:
        if group_found["we_are_admin"] is False:
            return True
        elif group_found["we_are_admin"] is True:
            return False

    admins = variable.updater.bot.get_chat_administrators(message.chat.id)
    if groups.creator_is_present(admins):
        return False

    return True  # we are not admins of this group, bot should exit


def check_spam(message):
    chat = message.chat

    if chat.type == "private":
        return

    is_spam = utils.is_spam(message.text)

    if is_spam is True:
        utils.mute_and_delete(message)
        return


def check_username(message):
    from_user = None
    try:
        from_user = message.from_user
    except:
        return

    username = None
    try:
        username = from_user.username
    except:
        pass

    if username is None or len(username) < 2:
        try:
            variable.updater.bot.send_message(from_user.id, "Imposta un username dalle impostazioni di telegram\n\n"
                                                            "Set an username from telegram settings")
        except:
            pass

        try:
            time = float(datetime.datetime.now().timestamp()) + 35  # 35 seconds
            variable.updater.bot.restrict_chat_member(message.chat.id, from_user.id, until_date=time,
                                                      can_add_web_page_previews=False,
                                                      can_send_media_messages=False,
                                                      can_send_messages=False,
                                                      can_send_other_messages=False)
        except:
            pass


def check_message(update, context):
    message = update.message

    to_exit, error_code = groups.try_add_group(message)
    if to_exit is True:
        utils.leave_chat(message.chat, 1, error_code)
        return

    to_exit = check_if_exit(message)
    if to_exit is True:
        utils.leave_chat(message.chat, 2, 0)
        return

    check_username(message)
    check_blacklist(message)

    if not creators.allowed_spam.__contains__(message.from_user.id):
        check_spam(message)
