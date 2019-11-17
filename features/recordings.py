import variable
from config import recordings_config
from functions import utils


def post_recordings2(update, description):
    message = update.message

    text2 = "Group: " + message.chat.title + "\n"

    id2 = message.chat.id
    if id2 < 0:
        id2 = -id2

    text2 += "#id" + str(id2) + "\n\n"
    text2 += "Description: " + description

    forward_success, message2 = utils.forward_message(recordings_config.channel_id, message.reply_to_message)
    if forward_success is not True:
        utils.send_in_private_or_in_group("C'è stato un problema con l'inoltro dell'audio. Contatta gli "
                                          "amministratori di @PoliNetwork",
                                          message.chat.id, message.from_user)
        return

    variable.updater.bot.send_message(recordings_config.channel_id, text=text2,
                                      reply_to_message_id=message2.message_id)
    utils.send_in_private_or_in_group("Audio correttamente inoltrato in " + str(recordings_config.channel_id),
                                      message.chat.id, message.from_user)


def post_recordings(update, context):
    message = update.message

    if message.chat.type == "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in un gruppo del network",
                                          message.chat.id, message.from_user)
        return

    if message.reply_to_message is None:
        utils.send_in_private_or_in_group("Questo comando funziona solo se rispondi ad un messaggio (di tipo audio), "
                                          "il quale messaggio sarà poi inviato in " + str(recordings_config.channel_id),
                                          message.chat.id, message.from_user)
        return

    if message.reply_to_message.voice is not None \
            or message.reply_to_message.audio is not None\
            or message.reply_to_message.video is not None\
            or message.reply_to_message.video_note is not None:

        text = message.text

        description = " ".join(text.split(" ")[1:])

        if len(description) < 8:
            utils.send_in_private_or_in_group(
                "La descrizione che hai dato è troppo corta!",
                message.chat.id, message.from_user)
            return

        post_recordings2(update, description)
        return
    else:
        utils.send_in_private_or_in_group("Questo comando funziona solo se rispondi ad un messaggio (di tipo audio), "
                                          "il quale messaggio sarà poi inviato in " + str(recordings_config.channel_id),
                                          message.chat.id, message.from_user)


def help_handler(update, context):
    message = update.message

    if message.chat.type != "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                          message.chat.id, message.from_user)
        return

    variable.updater.bot.send_message(update.message.chat.id,
                                      "Entra in un gruppo e rispondi con /postrecording [DESCRIZIONE]\n"
                                      "Esempio: /postrecording Lezione 1 - Termodinamica\n"
                                      "Il nome del gruppo sarà scritto in automatico.\n"
                                      "L'audio sarà pubblicato sul canale @PoliRecordings",
                                      parse_mode="HTML")
