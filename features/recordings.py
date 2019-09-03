from functions import utils


def post_recordings2(update):
    message = update.message
    # todo: forward audio or voice to @PoliRecordings
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
        post_recordings2(update)
        return
    else:
        utils.send_in_private_or_in_group("Questo comando funziona solo se rispondi ad un messaggio (di tipo audio), "
                                          "il quale messaggio sarà poi inviato in @PoliRecordings",
                                          message.chat.id, message.from_user)
