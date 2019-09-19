#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import MessageHandler, CommandHandler, Filters, CallbackQueryHandler

from features import all_messages, help_file, anonimi, callback_query
from functions import utils
from sub_bots.anon import config_anon, variable_anon


def start_handler(update, context):
    update.message.reply_text("Ciao! 👋\n"
                              "\nScrivi /help per la lista completa delle mie funzioni 👀\n"
                              "\nVisita anche il nostro sito https://polinetwork.github.io")


def contact_handler(update, context):
    update.message.reply_text("Puoi scriverci alla pagina facebook https://m.me/PolitecnicoDiMilanoNetwork")


config_anon.me = variable_anon.updater.bot.get_me().id

dispatcher = variable_anon.updater.dispatcher

# main
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('contact', contact_handler))

# help
dispatcher.add_handler(CommandHandler('help', help_file.help_handler))
dispatcher.add_handler(CommandHandler('groups', help_file.help_groups_handler))

# PoliAnoniMi
dispatcher.add_handler(CommandHandler('anon', anonimi.post_anonimi))
dispatcher.add_handler(CommandHandler('help_anon', anonimi.help_handler))

# all
dispatcher.add_handler(MessageHandler(Filters.all, all_messages.check_message))
dispatcher.add_handler(CallbackQueryHandler(callback_query.handler))

thread = utils.DeleteMessageThread()
thread.start()

variable_anon.updater.start_polling()
