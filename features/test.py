import variable
from functions import utils


def test_message(update, context):
    message = update.message

    if message.chat.type == "private":
        return

    from_user = message['from_user']
    utils.send_in_private_or_in_group("Ciao!", message.chat.id, from_user)


def stress_test(update, context):
    # todo: place a return on first line so this method is disabled.

    message = update.message
    from_user = message.from_user

    i = 0
    n = 10000
    while i <= n:
        if i == n:
            variable.updater.bot.send_message(from_user.id, "Completate " + str(n) + " iterazioni!")
        i = i + 1
    return None
