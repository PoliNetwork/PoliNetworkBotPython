from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import variable
from config import anonimi_config
from functions import utils


def post_anonimi(update, context):
    message = update.message

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
        pass

    keyboard = [[InlineKeyboardButton("Accetta", callback_data='anon ' + str(message2_id)
                                                               + " " + str(message.chat.id) + " " + 'Y'),
                 InlineKeyboardButton("Rifiuta", callback_data='anon ' + str(message2_id)
                                                               + " " + str(message.chat.id) + " " + 'N')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        variable.updater.bot.send_message(chat_id=anonimi_config.group_id,
                                          text="Approvare?\n#id" + str(message.chat.id),
                                          reply_to_message_id=message2_id,
                                          reply_markup=reply_markup,
                                          parse_mode="HTML")
    except Exception as e:
        pass
    variable.updater.bot.send_message(message.chat.id, "Il messaggio è stato inoltrato e in attesa di approvazione")


def handler_callback(update, data):
    if data[3] == 'Y':
        group_id = anonimi_config.public_group_id
        result, message = utils.forward_message_anon(group_id, update.callback_query.message.reply_to_message, data[2])
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
    query.edit_message_text(text="Selected option: " + str(option) + "\n#id" + str(id2))
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
                                      " la pubblicazione sul canale @PoliAnoniMi",
                                      parse_mode="HTML")
