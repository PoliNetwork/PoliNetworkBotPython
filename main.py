from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

import groups


def start(update, context):
    update.message.reply_text("Bot started")


def check_message(update, context):
    update.message.reply_text("Message received")
    groups.try_add_group(update.message)


token = open("token.txt").read()
updater = Updater(token, use_context=True)
start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.all, check_message)
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
