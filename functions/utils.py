import bot


def send_in_private_or_in_group(text, group_id, user_id):
    success = True

    try:
        done = bot.updater.bot.send_message(user_id, text)
    except:
        success = False

    try:
        get_id = done.chat.id
        if get_id is None or get_id == "":
            success = False
    except:
        success = False

    if success is False:
        bot.updater.bot.send_message(group_id, text)
