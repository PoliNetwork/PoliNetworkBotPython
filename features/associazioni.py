import datetime
from threading import Thread
import json as jsonn
import time

import variable
from config import db_associazioni
from functions import utils


def errore_no_associazione(update):
    utils.send_in_private_or_in_group("Non fai parte di nessuna associazione, scrivi agli admin di @PoliNetwork",
                                      update.message.chat.id, update.message.from_user)
    pass


def get_associazione_name_from_user(x):
    for ass in db_associazioni.json.keys():
        for user in db_associazioni.json.get(ass).get("users"):
            if user == x:
                return ass
    return None


def get_associazione_json_from_associazione_name(name):
    for ass in db_associazioni.json.keys():
        if ass is name:
            return db_associazioni.json.get(ass)
    return None


# prendi il messaggio dell'associazione dal nome dell'associazione
def get_message_from_associazione_name(name):
    assoc = None
    for associ in db_associazioni.json.keys():
        if associ is name:
            assoc = associ

    if db_associazioni.messages_dict.__contains__(assoc):
        return db_associazioni.messages_dict.get(assoc)

    return None


def get_message_from_associazione_json(json):
    assoc = None
    for associ in db_associazioni.json.keys():
        if associ is json:
            assoc = associ

    if db_associazioni.messages_dict.__contains__(assoc):
        return db_associazioni.messages_dict.get(assoc)

    return None


# leggi ed inoltra
def assoc_read(update, context):
    associazione = get_associazione_name_from_user(update.message.from_user.id)

    if associazione is None:
        errore_no_associazione(update)
        return None

    error1 = "Nessun messaggio in coda!"

    try:
        read_message = get_message_from_associazione_name(associazione)
        if read_message is None:
            utils.send_in_private_or_in_group(error1 + " - 01", update.message.chat.id, update.message.from_user)
            pass
        else:
            variable.updater.bot.forward_message(read_message.get("chat_id"), read_message.get("chat_id"),
                                                 read_message.get("message_id"))
            pass

    except:
        utils.send_in_private_or_in_group(error1 + " - 02", update.message.chat.id, update.message.from_user)
        pass
    return None


def check_message_associazioni(update):
    # todo: controllare che il messaggio rispetti i requisiti, inviare all'utente eventuali errori, e poi tornare True se il messaggio è valido, False altrimenti

    message2 = update.message.reply_to_message
    if message2.text is None:
        return True

    if len(message2.text) > 0:
        return False
    return True


def assoc_write(update, context):
    associazione = get_associazione_name_from_user(update.message.from_user.id)

    if associazione is None:
        errore_no_associazione(update)
        return None

    messaggio_valido = check_message_associazioni(update)
    if messaggio_valido:
        if get_message_from_associazione_name(associazione) is not None:
            utils.send_in_private_or_in_group("Messaggio già in coda. Rimuovilo con /assoc delete.",
                                              update.message.chat.id, update.message.from_user)
            return

        else:
            messaggio_originale = update.message.reply_to_message
            if messaggio_originale is None:
                utils.send_in_private_or_in_group("Devi rispondere ad un messaggio per aggiungerlo alla coda",
                                                  update.message.chat.id, update.message.from_user)
                return
            db_associazioni.messages_dict.__setitem__(associazione, {"chat_id": messaggio_originale.chat.id,
                                                                     "message_id": messaggio_originale.message_id,
                                                                     "time": datetime.datetime.now().strftime(
                                                                         '%d-%m-%Y %H:%M:%S')})
            save_ass_messages()
            utils.send_in_private_or_in_group("Messaggio aggiunto alla coda correttamente",
                                              update.message.chat.id, update.message.from_user)
        pass
    else:
        utils.send_in_private_or_in_group(
            "Il messaggio non rispetta i requisiti richiesti! Contatta gli admin di @PoliNetwork!",
            update.message.chat.id, update.message.from_user)

    return None


def assoc_delete(update, context):
    associazione = get_associazione_name_from_user(update.message.from_user.id)

    if associazione is None:
        errore_no_associazione(update)
        return None

    read_message = get_message_from_associazione_name(associazione)
    if read_message is None:
        utils.send_in_private_or_in_group("Nessun messaggio in coda",
                                          update.message.chat.id, update.message.from_user)
        pass
    else:
        db_associazioni.messages_dict.pop(associazione, None)
        utils.send_in_private_or_in_group("Messaggio rimosso con successo",
                                          update.message.chat.id, update.message.from_user)
        save_ass_messages()
    pass
    return None


class start_check_Thread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            start_check()
            time.sleep(60 * 5)


def send_scheduled_messages():
    for associazione in db_associazioni.messages_dict:
        try:
            associazione2 = db_associazioni.messages_dict.get(associazione)
            chat_id = associazione2['chat_id']
            message_id = associazione2['message_id']
            if len(str(chat_id)) > 1 and len(str(message_id)) > 1:
                variable.updater.bot.forward_message(chat_id=db_associazioni.group, from_chat_id=chat_id,
                                                     message_id=message_id)
            else:
                # todo: inviare un messaggio a quelli dell'associazione dicendo che non hanno preso parte a questa
                #  data di pubblicazione
                pass
        except Exception as e:
            pass
    db_associazioni.date = "00:00:00:00:00"
    db_associazioni.config_json.update({"date": db_associazioni.date})
    save_date()

    for associazione in db_associazioni.messages_dict:
        try:
            associazione2 = db_associazioni.messages_dict.get(associazione)
            associazione2['chat_id'] = 0
            associazione2['message_id'] = 0
            associazione2['time'] = None
            db_associazioni.messages_dict[associazione] = associazione2
        except Exception as e:
            pass

    save_ass_messages()
    pass


def start_check():
    if db_associazioni.date == "00:00:00:00:00":
        return

    time2 = db_associazioni.date.split(":")
    day = time2[2]
    month = time2[1]
    year = time2[0]
    hour = time2[3]
    minute = time2[4]

    scheduled_time = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
    dt_now = datetime.datetime.now()
    if dt_now > scheduled_time:  # i.e. is the scheduled time over?
        send_scheduled_messages()


def save_ass_messages():
    with open("data/ass_messages.json", 'w', encoding="utf-8") as file:
        jsonn.dump(db_associazioni.messages_dict, file)


def save_date():
    with open("data/date.json", 'w', encoding="utf-8") as file:
        jsonn.dump(db_associazioni.config_json, file)
