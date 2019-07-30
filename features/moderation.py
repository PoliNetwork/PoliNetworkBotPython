from config import creators


def mute(update, context):
    # todo: mute user of replied message
    # todo: check if the one that is using the command is admin
    return None


def ban(update, context):
    # todo: ban user of replied message
    # todo: check if the one that is using the command is admin
    return None


def ban_all(update, context):
    message = update.message
    chat = message.chat
    if chat.id not in creators.owners:  # only owners can do this command
        return

    # todo: ban user from all groups.
