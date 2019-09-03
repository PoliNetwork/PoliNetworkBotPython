import variable
from functions import utils


def post_recordings2(update, description):

    message = update.message

    text2 = "Group: " + message.chat.title + "\n"

    id2 = message.chat.id
    if id2 < 0:
        id2 = -id2

    text2 += "#id" + str(id2) + "\n\n"
    text2 += "Description: " + description

    forward_success, message2 = utils.forward_message("@PoliRecordings", message.reply_to_message)
    if forward_success is not True:
        utils.send_in_private_or_in_group("C'è stato un problema con l'inoltro dell'audio. Contatta gli "
                                          "amministratori di @PoliNetwork",
                                          message.chat.id, message.from_user)
        return

    variable.updater.bot.send_message("@PoliRecordings", text=text2, reply_to_message_id=message2.message_id)
    utils.send_in_private_or_in_group("Audio correttamente inoltrato in @PoliRecordings",
                                      message.chat.id, message.from_user)


def post_recordings(update, context):
    message = update.message

    if message.chat.type == "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo un gruppo del network",
                                          message.chat.id, message.from_user)
        return

    if message.reply_to_message is None:
        utils.send_in_private_or_in_group("Questo comando funziona solo se rispondi ad un messaggio (di tipo audio), "
                                          "il quale messaggio sarà poi inviato in @PoliRecordings",
                                          message.chat.id, message.from_user)
        return

    if message.reply_to_message.voice is not None or message.reply_to_message.audio is not None:

        text = message.text

        description = " ".join(text.split(" ")[1:])

        if len(description) < 5:
            utils.send_in_private_or_in_group(
                "La descrizione che hai dato è troppo corta!",
                message.chat.id, message.from_user)
            return

        post_recordings2(update, description)
        return
    else:
        utils.send_in_private_or_in_group("Questo comando funziona solo se rispondi ad un messaggio (di tipo audio), "
                                          "il quale messaggio sarà poi inviato in @PoliRecordings",
                                          message.chat.id, message.from_user)
