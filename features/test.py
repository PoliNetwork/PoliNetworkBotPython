from functions import utils


def test_message(update, context):
    message = update.message

    if message.chat.type == "private":
        return

    from_user = message['from_user']
    utils.send_in_private_or_in_group("Ciao!", message.chat.id, from_user)