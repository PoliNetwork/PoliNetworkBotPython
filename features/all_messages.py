from features import groups
from functions import utils


def check_blacklist(message):
    chat = message.chat

    if chat.type == "private":
        return
    text = message.text

    is_valid = utils.is_valid(text)

    if is_valid is False:
        # todo: mute for 15 minutes and delete message.
        pass


def check_message(update, context):
    message = update.message
    groups.try_add_group(message)

    check_blacklist(message)
