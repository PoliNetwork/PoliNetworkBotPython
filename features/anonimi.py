import variable
from functions import utils


def help_handler(update, context):
    message = update.message

    if message.chat.type != "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                          message.chat.id, message.from_user)
        return

    variable.updater.bot.send_message(update.message.chat.id,
                                      "Abbiamo spostato questa funzionalità sul bot @PoliAnonimi_Bot.\n"
                                      "Scrivi a lui!", parse_mode="HTML")
