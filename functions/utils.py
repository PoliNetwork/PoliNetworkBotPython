import datetime

import bot


def send_in_private_or_in_group(text, group_id, user):
    success = True
    user_id = user.id

    try:
        bot.updater.bot.send_message(user_id, text)
    except:
        success = False

    if success is True:
        return

    if user.username is not None and user.username != "":
        text = "[Messaggio per @" + user.username + "]\n" + text

    done2 = bot.updater.bot.send_message(group_id, text)

    # to_delete.add(group_id, done2.message_id, datetime.datetime.now())
