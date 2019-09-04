from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import variable
from config import anonimi_config
from functions import utils


def post_anonimi(update, context):
    message = update.message
    text = message.text
    data = str(text).split(" ")

    if message.chat.type != "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                          message.chat.id, message.from_user)
        return

    if message.reply_to_message is None:
        utils.send_in_private_or_in_group("Questo comando funziona solo se rispondi ad un messaggio, "
                                          "il quale messaggio sarà poi inviato "
                                          "per l'approvazione per la pubblicazione sul canale",
                                          message.chat.id, message.from_user)
        return

    identity_valid = True
    identity = None
    try:
        identity = data[1]
        if len(str(identity)) < 1:
            identity_valid = False
        else:
            identity = int(identity)
    except:
        identity_valid = False

    if identity_valid is False:
        variable.updater.bot.send_message(message.chat.id, "Devi indicare un'identità!\n"
                                                           "\n"
                                                           "Esempio:\n"
                                                           "/anon 1 [eventuale link di risposta]\n"
                                                           "\n"
                                                           "Maggiori info con /help_anon")
        return

    is_a_reply, message_reply_id = utils.is_an_anon_message_link(data)

    forward_success, message2 = utils.forward_message(anonimi_config.group_id,
                                                      message.reply_to_message)
    if forward_success is not True:
        variable.updater.bot.send_message(message.chat.id, "Errore nell'inoltro del messaggio per l'approvazione. "
                                                           "Contatta gli admin di @PoliNetwork")
        return

    message2_id = None
    try:
        message2_id = message2.message_id
    except:
        variable.updater.bot.send_message(message.chat.id, "Errore nell'inoltro del messaggio per l'approvazione. "
                                                           "Contatta gli admin di @PoliNetwork")
        return

    message_reply_id2 = ""
    if is_a_reply:
        message_reply_id2 = " " + message_reply_id

    keyboard = [
        [
            InlineKeyboardButton(text="Accetta", callback_data='anon'
                                                               + " " + str(message2_id)
                                                               + " " + str(message.chat.id)
                                                               + " " + 'Y'
                                                               + " " + str(identity)
                                                               + message_reply_id2),
            InlineKeyboardButton(text="Rifiuta", callback_data='anon'
                                                               + " " + str(message2_id)
                                                               + " " + str(message.chat.id)
                                                               + " " + 'N'
                                                               + " " + str(identity)
                                                               + message_reply_id2),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        reply_string = ""
        if is_a_reply:
            reply_string = "[In risposta a t.me/PoliAnoniMi/" + str(message_reply_id) + "]"

        text2 = reply_string + "\n\nApprovare?\n#id" + str(message.chat.id) + "\nIdentità: " + str(identity)

        variable.updater.bot.send_message(chat_id=anonimi_config.group_id,
                                          text=text2,
                                          reply_to_message_id=message2_id,
                                          reply_markup=reply_markup,
                                          parse_mode="HTML")
    except Exception as e:
        pass
    variable.updater.bot.send_message(message.chat.id, "Il messaggio è stato inoltrato e in attesa di approvazione")


def handler_callback(update, data):
    reply = None
    link = ""

    len_reply = 6
    identity = data[4]

    if len(data) == len_reply:
        reply = int(data[len_reply - 1])
    if data[3] == 'Y':
        group_id = anonimi_config.public_group_id
        result, message = utils.forward_message_anon(group_id,
                                                     update.callback_query.message.reply_to_message,
                                                     data[2],
                                                     reply,
                                                     identity)
        link = message.link
        variable.updater.bot.send_message(chat_id=data[2], text="Il tuo messaggio è "
                                                                "stato pubblicato, qui il link " + str(link))
    else:
        variable.updater.bot.send_message(chat_id=data[2], text="Il tuo messaggio è stato rifiutato. \nControlla di "
                                                                "aver rispettato le regole del network @PoliRules, "
                                                                "e nel caso credi sia stato un errore, scrivici nella "
                                                                "pagina facebook di PoliNetwork, grazie")

    query = update.callback_query
    id2 = data[2]
    option = data[3]

    if len(data) == len_reply:
        reply_string = "\n[In risposta a t.me/PoliAnoniMi/" + str(reply) + "]"
    else:
        reply_string = ""

    if data[3] == 'Y':
        query.edit_message_text(text="Selected option: " + str(option) + "\n#id" +
                                     str(id2) + reply_string + "\n" + str(link) + "\n" + "Identità: " + str(identity))
    else:
        query.edit_message_text(text="Selected option: " + str(option) + "\n#id" +
                                     str(id2) + reply_string + "\n" + "Identità: " + str(identity))
    return None


def help_handler(update, context):
    message = update.message

    if message.chat.type != "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                          message.chat.id, message.from_user)
        return

    variable.updater.bot.send_message(update.message.chat.id,
                                      "Scrivi il messaggio che vuoi inviare.\n"
                                      "Rispondi a quel messaggio con /anon per richiederne"
                                      " la pubblicazione sul canale @PoliAnoniMi.\n"
                                      "\n"
                                      "Devi indicare un'identità con la quale vuoi postare, 0 per identità nascosta.\n"
                                      "\n"
                                      "Esempio:\n"
                                      "/anon 1 [eventuale link del messaggio del canale a cui rispondere]\n"
                                      "Per inviare un messaggio con la propria identità anonima 1\n"
                                      "\n"
                                      "/anon 0 [eventuale link]\n"
                                      "Per inviare un messaggio con identità nascosta.\n"
                                      "\n"
                                      "In entrambi i casi (sia che si usi 0 come identità o un altro numero)"
                                      " nessun iscritto al canale sarà in grado di capire chi siete.\n"
                                      "L'identità è stata introdotta per permettere a delle persone di"
                                      " scrivere sotto uno pseudonimo fisso, se lo desiderano.\n"
                                      "\n"
                                      "Buon divertimento con questa funzione del nostro bot 😄!\n"
                                      "\n"
                                      "Se dovesse esserci qualsiasi problema, "
                                      "scriveteci alla pagina Facebook di PoliNetwork",
                                      parse_mode="HTML")
