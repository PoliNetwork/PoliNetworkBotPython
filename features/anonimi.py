from functions import utils


def post_anonimi(update, context):
    message = update.message

    if message.chat.type != "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                          message.chat.id, message.from_user)
        return

    if message.reply_to_message is None:
        utils.send_in_private_or_in_group("Questo comando funziona solo se rispondi ad un messaggio, "
                                          "il quale messaggio sarà poi inviato "
                                          "per l'approvazione per la pubblicazione sul canale",
                                          message.chat.id, message.from_user)
        return

    # todo send message to group for approval
    # todo send a second message, replying the first one, with a keyboard for accepting it
    # todo send a message to the user "Il messaggio è stato inoltrato e in attesa di approvazione"

    # todo:
    #  (not sure if here in this part of code)
    #       if accept: post to channel and send the link to the original user
    #               "Il tuo messaggio è stato pubblicato, qui il link: [link]"
    #       if not accept: send to the original user
    #               "Il tuo messaggio è stato rifiutato.
    #               Controlla di aver rispettato le regole del network @PoliRules, e nel caso credi
    #               sia stato un errore, scrivici nella pagina facebook di PoliNetwork, grazie"
    return None
