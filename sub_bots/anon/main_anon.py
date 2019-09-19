#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackQueryHandler

from config import creators
from sub_bots.anon import config_anon, variable_anon


def start_handler(update, context):
    update.message.reply_text("Ciao! 👋\n"
                              "\nScrivi /help per la lista completa delle mie funzioni 👀\n"
                              "\nVisita anche il nostro sito https://polinetwork.github.io")


def contact_handler(update, context):
    update.message.reply_text("Puoi scriverci alla pagina facebook https://m.me/PolitecnicoDiMilanoNetwork")


def send_in_private_or_in_group(text, chat_id, from_user):
    pass


def is_an_anon_message_link(parts):
    if len(parts) <= 2:
        return False, ""
    if "t.me/PoliAnoniMi/" in parts[2]:
        return True, parts[2].split("/")[-1]


def forward_message(group_id, message):
    try:
        message_sent = variable_anon.updater.bot.forward_message(group_id, message.chat.id, message.message_id)
        return True, message_sent
    except Exception as e:
        e2 = str(e)
        for owner2 in creators.owners:
            variable_anon.updater.bot.send_message(owner2, "Error forwarding message!\n\n" + e2)
    return False, None


def post_anonimi(update, context):
    message = update.message
    text = message.text
    data = str(text).split(" ")

    if message.chat.type != "private":
        send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                    message.chat.id, message.from_user)
        return

    if message.reply_to_message is None:
        send_in_private_or_in_group("Questo comando funziona solo se rispondi ad un messaggio, "
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
        variable_anon.updater.bot.send_message(message.chat.id, "Devi indicare un'identità!\n"
                                                                "\n"
                                                                "Esempio:\n"
                                                                "/anon 1 [eventuale link di risposta]\n"
                                                                "\n"
                                                                "Maggiori info con /help_anon")
        return

    is_a_reply, message_reply_id = is_an_anon_message_link(data)

    forward_success, message2 = forward_message(config_anon.group_id,
                                                message.reply_to_message)
    if forward_success is not True:
        variable_anon.updater.bot.send_message(message.chat.id, "Errore nell'inoltro del messaggio per l'approvazione. "
                                                                "Contatta gli admin di @PoliNetwork")
        return

    message2_id = None
    try:
        message2_id = message2.message_id
    except:
        variable_anon.updater.bot.send_message(message.chat.id, "Errore nell'inoltro del messaggio per l'approvazione. "
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

        variable_anon.updater.bot.send_message(chat_id=config_anon.group_id,
                                               text=text2,
                                               reply_to_message_id=message2_id,
                                               reply_markup=reply_markup,
                                               parse_mode="HTML")
    except Exception as e:
        pass
    variable_anon.updater.bot.send_message(message.chat.id,
                                           "Il messaggio è stato inoltrato e in attesa di approvazione")


def notify_owners(e):
    e2 = str(e)
    for owner2 in creators.owners:
        variable_anon.updater.bot.send_message(owner2, "Eccezione:\n\n" + e2)


def forward_message_anon(group_id, message, user_id, reply, identity):
    identity = int(identity)

    if identity == 0:
        author_line = ""
    else:
        salt = open("salt/salt_anonimi.txt", encoding="utf-8").read()
        to_hash = (str(user_id) + "_" + str(identity) + str(salt)).encode('utf-8')
        hash2 = hashlib.sha512(to_hash).hexdigest()
        author_id = (str(hash2)[:8]).upper()

        author_line = "\n\nAuthor: #id_" + str(author_id)

    try:
        caption = ""
        if message.caption is not None:
            caption = message.caption

        if message.text is not None:
            message_sent = variable_anon.updater.bot.send_message(chat_id=group_id,
                                                                  text=message.text + author_line,
                                                                  reply_to_message_id=reply)
        elif message.photo:
            message_sent = variable_anon.updater.bot.send_photo(chat_id=group_id,
                                                                photo=message.photo[0],
                                                                caption=caption + author_line,
                                                                reply_to_message_id=reply)
        elif message.audio:
            message_sent = variable_anon.updater.bot.send_audio(chat_id=group_id,
                                                                audio=message.audio.file_id,
                                                                caption=caption + author_line,
                                                                reply_to_message_id=reply)
        elif message.voice is not None:
            message_sent = variable_anon.updater.bot.send_voice(chat_id=group_id,
                                                                voice=message.voice.file_id,
                                                                caption=caption + author_line,
                                                                reply_to_message_id=reply)
        elif message.video is not None:
            message_sent = variable_anon.updater.bot.send_video(chat_id=group_id,
                                                                video=message.video.file_id,
                                                                caption=caption + author_line,
                                                                reply_to_message_id=reply)
        elif message.video_note is not None:
            message_sent = variable_anon.updater.bot.send_video_note(chat_id=group_id,
                                                                     video_note=message.video_note.file_id,
                                                                     caption=caption + author_line,
                                                                     reply_to_message_id=reply)
        elif message.document is not None:
            message_sent = variable_anon.updater.bot.send_document(chat_id=group_id,
                                                                   document=message.document.file_id,
                                                                   caption=caption + author_line,
                                                                   reply_to_message_id=reply)
        elif message.sticker is not None:
            message_sent = variable_anon.updater.bot.send_sticker(chat_id=group_id,
                                                                  sticker=message.sticker.file_id,
                                                                  caption=caption + author_line,
                                                                  reply_to_message_id=reply)
        elif message.location is not None:
            message_sent = variable_anon.updater.bot.send_location(chat_id=group_id,
                                                                   latitude=message.location.latitude,
                                                                   longitude=message.location.longitude,
                                                                   caption=caption + author_line,
                                                                   reply_to_message_id=reply)
        else:
            return False, None

        return True, message_sent
    except Exception as e:
        notify_owners(e)
        return False, None


def handler_callback(update, data):
    reply = None
    link = ""

    len_reply = 6

    try:
        identity = data[4]
    except:
        identity = None

    if identity is None:
        return

    if len(data) == len_reply:
        reply = int(data[len_reply - 1])
    if data[3] == 'Y':
        group_id = config_anon.public_group_id
        try:
            result, message = forward_message_anon(group_id,
                                                   update.callback_query.message.reply_to_message,
                                                   data[2],
                                                   reply,
                                                   identity)
        except Exception as e:
            pass

        link = message.link
        variable_anon.updater.bot.send_message(chat_id=data[2], text="Il tuo messaggio è "
                                                                     "stato pubblicato, qui il link " + str(link))
    else:
        variable_anon.updater.bot.send_message(chat_id=data[2],
                                               text="Il tuo messaggio è stato rifiutato. \nControlla di "
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


def handler_callback2(update, context):
    query = update.callback_query

    data = str(query.data).split(" ")

    if data[0] == "anon":
        handler_callback(update, data)
        return
    else:
        # todo: in future, add new "modules"
        return


def help_handler(update, context):
    message = update.message

    if message.chat.type != "private":
        send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                    message.chat.id, message.from_user)
        return

    variable_anon.updater.bot.send_message(update.message.chat.id,
                                           "Scrivi il messaggio che vuoi inviare.\n"
                                           "Rispondi a quel messaggio con /anon per richiederne"
                                           " la pubblicazione sul canale @PoliAnoniMi.\n"
                                           "\n"
                                           "Devi indicare un'identità con la quale"
                                           " vuoi postare, 0 per identità nascosta.\n"
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


config_anon.me = variable_anon.updater.bot.get_me().id

dispatcher = variable_anon.updater.dispatcher

# main
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('contact', contact_handler))

# PoliAnoniMi
dispatcher.add_handler(CommandHandler('anon', post_anonimi))
dispatcher.add_handler(CommandHandler('help', help_handler))

# all


dispatcher.add_handler(CallbackQueryHandler(handler_callback2))

variable_anon.updater.start_polling()
