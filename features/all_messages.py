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

    if groups.subcreator_is_present(admins):
        return False

    return True  # we are not admins of this group, bot should exit


def check_spam(message):
    chat = message.chat

    if chat.type == "private":
        return

    s_to_check = ""

    if message.text is not None:
        s_to_check = message.text

    if not s_to_check and message.caption is not None:
        s_to_check = message.caption

    if not s_to_check:
        return

    is_spam = utils.is_spam(s_to_check)

    if is_spam is True:
        utils.mute_and_delete(message)
        return

    if utils.contains_ko_ja_chi(s_to_check):
        utils.temp_mute_and_delete(message, 60)


def check_username_and_name(message):
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

    username_valid = True
    if username is None or len(username) < 2:
        username_valid = False

    if username_valid is False and message.from_user.id in creators.allowed_no_username:
        username_valid = True

    firstname = None
    try:
        firstname = from_user.first_name
    except:
        pass

    firstname_valid = True
    if firstname is None or len(firstname) < 2:
        firstname_valid = False

    seconds = 40

    message_to_send = None
    if username_valid is False and firstname_valid is False:
        message_to_send = "Imposta un username e un nome più lungo dalle impostazioni di telegram\n\n" \
                          "Set an username and a longer first name from telegram settings"
    elif username_valid is False:
        message_to_send = "Imposta un username dalle impostazioni di telegram\n\n" \
                          "Set an username from telegram settings"
    elif firstname_valid is False:
        message_to_send = "Imposta un nome più lungo " \
                          "dalle impostazioni di telegram\n\n" \
                          "Set a longer first name from telegram settings"

    if message_to_send is not None:
        try:
            utils.send_in_private_or_in_group(message_to_send, message.chat.id, from_user)
        except Exception as e:
            utils.notify_owners(e)

        try:
            variable.updater.bot.delete_message(message.chat.id, message.message_id)
        except Exception as e:
            try:
                utils.notify_owners(e, message.chat.title)
            except:
                utils.notify_owners(e)

        try:
            time = float(datetime.datetime.now().timestamp()) + seconds
            variable.updater.bot.restrict_chat_member(message.chat.id, from_user.id, until_date=time,
                                                      can_add_web_page_previews=False,
                                                      can_send_media_messages=False,
                                                      can_send_messages=False,
                                                      can_send_other_messages=False)
        except Exception as e:
            utils.notify_owners(e)


def check_if_is_exit_message_of_user(message):

    if message.left_chat_member is not None:
        variable.updater.bot.delete_message(message.chat.id, message.message_id)

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

    check_username_and_name(message)
    check_blacklist(message)

    if not creators.allowed_spam.__contains__(message.from_user.id):
        check_spam(message)

    try:
        check_if_is_exit_message_of_user(message)
    except Exception as e:
        utils.notify_owners(e)
