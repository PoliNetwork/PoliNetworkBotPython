from functions import utils


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

    pass
