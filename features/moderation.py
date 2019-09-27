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
    splitted_text = message.text.split(" ")
    command = splitted_text[0].replace("/", "")
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

    if len(splitted_text) > 1:
        time_to_add = splitted_text[1]
        unit_of_measure = splitted_text[2]
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
        utils.send_in_private_or_in_group("Utente mutato con successo.", chat_id, message.from_user)
    elif command in "unmute":
        bot.restrict_chat_member(chat_id, receiver,
                                 can_add_web_page_previews=True,
                                 can_send_media_messages=True,
                                 can_send_messages=True,
                                 can_send_other_messages=True)
        utils.send_in_private_or_in_group("Utente smutato con successo.", chat_id, message.from_user)
    elif command in "ban":
        bot.kick_chat_member(chat_id, receiver, until_date=time)
        utils.send_in_private_or_in_group("Utente bannato con successo.", chat_id, message.from_user)
    elif command in "unban":
        bot.unban_chat_member(chat_id, receiver)
        utils.send_in_private_or_in_group("Utente sbannato con successo.", chat_id, message.from_user)


def ban_all2(receiver):
    missed_list = []
    try:
        for group in variable.groups_list:
            try:
                variable.updater.bot.kick_chat_member(group['Chat']['id'], receiver)
            except:
                try:
                    missed_list.append(group['Chat']['title'])
                except:
                    try:
                        missed_list.append("[NAME NOT FOUND!] " + str(group['Chat']['id']))
                    except:
                        try:
                            missed_list.append("[NAME NOT FOUND!] [ID NOT FOUND!]")
                        except:
                            pass
    except Exception as e:
        utils.notify_owners(e, "Crash in ban")

    return missed_list


def ban_all(update, context):
    message = update.message
    chat = message.chat
    chat_id = chat.id
    if chat_id not in creators.owners:  # only owners can do this command
        return

    receiver = None
    try:
        if message.reply_to_message is None:
            receiver = message.text.split(" ")[1]
        else:
            receiver = message.reply_to_message.from_user['id']

        receiver = int(receiver)
    except:
        pass

    if receiver is None:
        utils.send_in_private_or_in_group(
            "Non riesco a capire chi vuoi bannare", chat_id, message.from_user)
        return

    utils.send_in_private_or_in_group(
        "Sto cercando di bannare " + str(receiver), chat_id, message.from_user)

    missed_list = None
    try:
        missed_list = ban_all2(receiver)
    except Exception as e:
        utils.notify_owners(e)

    if missed_list is None:
        utils.send_in_private_or_in_group("Non sono riuscito a bannare "+str(receiver)+".", chat_id, message.from_user)
        return

    text = "Fatto! Ho bannato " + str(receiver)
    if len(missed_list) > 0:
        text = text + "\nTranne in " + str(len(missed_list)) + " gruppi.\n"
        for missed in missed_list:
            text = text + "\n" + str(missed)
    
    utils.send_in_private_or_in_group(text, chat_id, message.from_user)
