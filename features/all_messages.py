from features import groups


def check_message(update, context):
    # update.message.reply_text("Message received")
    groups.try_add_group(update.message)