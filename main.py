from telegram.ext import MessageHandler, CommandHandler, Filters

import bot
from features import groups, reviews


def start(update, context):
    update.message.reply_text("Ciao! Scrivi /help per la lista completa delle mie funzioni\n"
                              "Visita anche il nostro sito https://polinetwork.github.io")


def help_handler(update, context):
    bot.updater.bot.send_message(update.message.chat.id,
                                 "Lista di funzioni:\n"
                                 "Ecc...")


def check_message(update, context):
    # update.message.reply_text("Message received")
    groups.try_add_group(update.message)


dispatcher = bot.updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help_handler))
dispatcher.add_handler(CommandHandler('recensione', reviews.add_review))
dispatcher.add_handler(CommandHandler('getgroupjson', groups.get_group_json))
dispatcher.add_handler(CommandHandler('getreviewjson', reviews.get_review_json))
dispatcher.add_handler(MessageHandler(Filters.all, check_message))

bot.updater.start_polling()
