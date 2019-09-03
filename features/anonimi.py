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
                                                      message.reply_to_message)  # todo send message to group for approval
    if forward_success is not True:
        variable.updater.bot.send_message(message.chat.id, "Errore nell'inoltro del messaggio per l'approvazione. "
                                                           "Contatta gli admin di @PoliNetwork")
        return

    keyboard = [[InlineKeyboardButton("Accetta", callback_data='1'),
                 InlineKeyboardButton("Rifiuta", callback_data='2')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    message2_id = None
    try:
        message2_id = message2.message_id
    except:
        pass

    try:
        variable.updater.bot.send_message(chat_id=anonimi_config.group_id,
                                          text="Approvare?",
                                          reply_to_message_id=message2_id,
                                          reply_markup=reply_markup,
                                          parse_mode="HTML")
        # todo send a second message, replying the first one, with a keyboard for accepting it
    except Exception as e:
        pass
    variable.updater.bot.send_message(message.chat.id, "Il messaggio è stato inoltrato e in attesa di approvazione")

    # todo:
    #  (not sure if here in this part of code)
    #       if accept: post to channel and send the link to the original user
    #               "Il tuo messaggio è stato pubblicato, qui il link: [link]"
    #       if not accept: send to the original user
    #               "Il tuo messaggio è stato rifiutato.
    #               Controlla di aver rispettato le regole del network @PoliRules, e nel caso credi
    #               sia stato un errore, scrivici nella pagina facebook di PoliNetwork, grazie"
