from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

import groups
import reviews


def start(update, context):
    update.message.reply_text("Bot started")


def check_message(update, context):
    # update.message.reply_text("Message received")
    groups.try_add_group(update.message)


token = open("token.txt").read()
updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.all, check_message))
dispatcher.add_handler(CommandHandler('recensione', reviews.add_review))

updater.start_polling()
