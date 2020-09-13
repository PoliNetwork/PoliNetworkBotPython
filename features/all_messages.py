import datetime

import telegram

import variable
from config import creators
from features import groups
from functions import utils
from functions.temp_state import temp_state_main
from functions.temp_state import temp_state_variable_main

ignored_chinese = [-1001394018284]


def check_blacklist(message):
    if message is None:
        return

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
    if message is None:
        return False, 10

    if message.new_chat_members is None or len(message.new_chat_members) == 0:
        return False, 1

    is_present = find_user(message.new_chat_members, creators.me)
    if is_present is False:
        return False, 2

    chat = message['chat']
    group_already_present, group_found = groups.find(chat['id'])
    if group_already_present is True:
        if group_found["we_are_admin"] is False:

            admins = variable.updater.bot.get_chat_administrators(message.chat.id)

            if groups.creator_is_present(admins):
                return False, 8

            if groups.subcreator_is_present(admins):
                return False, 9

            return True, 3

        elif group_found["we_are_admin"] is True:
            return False, 4

    admins = variable.updater.bot.get_chat_administrators(message.chat.id)

    if groups.creator_is_present(admins):
        return False, 5

    if groups.subcreator_is_present(admins):
        return False, 6

    return True, 7  # we are not admins of this group, bot should exit


def isNotBlank(myString):
    if myString and myString.strip():
        # myString is not None AND myString is not empty or blank
        return True
    # myString is None OR myString is empty or blank
    return False


def admin_is_present(admins, message):

    if message is None:
        return False

    if message.from_user is None:
        return False

    if not isNotBlank(message.from_user.username):
        return False

    for admin in admins:
        if isNotBlank(admin.user.username):
            if admin.user.username == message.from_user.username:
                return True

    return False


def checkIfAdmin(message):
    if message is not None and message.chat is not None:
        admins = variable.updater.bot.get_chat_administrators(chat_id=message.chat.id)
        return admin_is_present(admins, message)
    else:
        return False
    pass


def check_spam(message):
    if message is None:
        return

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

    boolMessageFromAdmin = checkIfAdmin(message)
    if boolMessageFromAdmin is True:
        return

    is_spam = utils.is_spam(s_to_check)

    if is_spam is True:
        utils.mute_and_delete(message)
        return

    if chat.id not in ignored_chinese:
        if utils.contains_ko_ja_chi(s_to_check):
            try:
                utils.temp_mute_and_delete(message, 60)
            except:
                pass


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
            if message.chat.id not in variable.group_users_enter_too_much:
                utils.send_in_private_or_in_group(message_to_send, message.chat.id, from_user)
            else:
                try:
                    variable.updater.bot.send_message(chat_id=from_user.id, text=message_to_send)
                except Exception as e2:
                    pass

        except Exception as e:
            utils.notify_owners(e)

        if message.chat.id not in variable.group_users_enter_too_much:
            try:
                utils.notify_owners(message.chat.id, "Utente senza user e/o nome lungo")
            except:
                pass

        try:
            variable.updater.bot.delete_message(message.chat.id, message.message_id)
        except Exception as e:
            try:
                utils.notify_owners(e, message.chat.title)
            except:
                utils.notify_owners(e)

        try:
            time = float(datetime.datetime.now().timestamp()) + seconds
            permission = telegram.ChatPermissions(can_add_web_page_previews=False,
                                                  can_send_media_messages=False,
                                                  can_send_messages=False,
                                                  can_send_other_messages=False)
            variable.updater.bot.restrict_chat_member(message.chat.id, from_user.id, until_date=time,
                                                      permissions=permission)
        except Exception as e:
            utils.notify_owners(e)


def check_if_is_exit_message_of_user(message):
    if message.left_chat_member is not None:
        variable.updater.bot.delete_message(message.chat.id, message.message_id)

    pass


def check_for_state(update):
    stato = None
    try:
        stato = temp_state_variable_main.state_dict[update.message.chat.id]
    except:
        stato = None

    if stato is None:
        return None

    return temp_state_main.next_main(update.message.chat.id, update=update)


def checkTextForTriggerWords(text, message):

    if message.chat.title is None:
        return

    if not str(message.chat.title).lower().__contains__("polimi"):
        return

    if message.chat.id not in [-1001208900229]:
        if text.__contains__("piano di studi") \
                or text.__contains__("piano studi") \
                or text.__contains__("piano degli studi"):

            text2 = "Ciao 👋 sembra tu stia chiedendo domande in merito al piano di studi. " \
                    "PoliNetwork ti consiglia di scrivere nel gruppo dedicato, " \
                    "<a href='https://t.me/joinchat/FNGD_0gOWoXdxdMhwUeMdw'>clicca qui</a>!"

            try:
                variable.updater.bot.send_message(chat_id=message.chat.id, text=text2,
                                                  parse_mode="HTML", disable_web_page_preview=True,
                                                  reply_to_message_id=message.message_id)

            except Exception as e2:
                utils.notify_owners(e2, text2)
    if message.chat.id not in [-1001241129618]:
        if text.__contains__("dsu") \
                or text.__contains__("diritto studio universitario") \
                or text.__contains__("diritto allo studio"):

            text2 = "Ciao 👋 sembra tu stia chiedendo domande in merito al DSU. " \
                    "PoliNetwork ti consiglia di scrivere nel gruppo dedicato, " \
                    "<a href='https://t.me/joinchat/FNGD_xs3LIL1jKC9klPPSw'>clicca qui</a>!"

            try:
                variable.updater.bot.send_message(chat_id=message.chat.id, text=text2,
                                                  parse_mode="HTML", disable_web_page_preview=True,
                                                  reply_to_message_id=message.message_id)
            except Exception as e3:
                utils.notify_owners(e3, text2)


def check_message(update, context):
    message = update.message

    if message is not None:

        to_exit, error_code = groups.try_add_group(message)
        if to_exit is True:
            utils.leave_chat(message.chat, 1, error_code, 0)
            return

        to_exit, error_code2 = check_if_exit(message)
        if to_exit is True:
            utils.leave_chat(message.chat, 2, 0, error_code2)
            return

        try:
            check_username_and_name(message)
            check_blacklist(message)
        except:
            pass

        if not creators.allowed_spam.__contains__(message.from_user.id):
            check_spam(message)

        try:
            check_if_is_exit_message_of_user(message)
        except Exception as e:
            utils.notify_owners(e)

        text = message.text
        if text is not None and message.chat is not None:
            text = str(text).lower()
            checkTextForTriggerWords(text, message)

            try:
                if message.chat.type != "private":
                    if text.startswith("/"):
                        try:
                            variable.updater.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                        except Exception as e2:
                            utils.notify_owners(e2, "Delete command fail 02")
            except Exception as e3:
                utils.notify_owners(e3, "Delete command fail 01")

    check_for_state(update)
