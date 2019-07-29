from telegram.ext import MessageHandler, CommandHandler, Filters

import bot
from features import groups, reviews


def start_handler(update, context):
    update.message.reply_text("Ciao! Scrivi /help per la lista completa delle mie funzioni\n"
                              "Visita anche il nostro sito https://polinetwork.github.io")


def contact_handler(update, context):
    update.message.reply_text("Puoi scriverci alla pagina facebook https://m.me/PolitecnicoDiMilanoNetwork")


def help_handler(update, context):
    bot.updater.bot.send_message(update.message.chat.id,
                                 "Lista di funzioni:\n"
                                 "🔹 Sistema di recensioni dei corsi (per maggiori info /help_recensioni)\n"
                                 "🔹 FAQ (domande frequenti) https://polinetwork.github.io/it/faq/index.html\n"
                                 "🔹 Bot ricerca aule libere @AulePolimiBot\n"
                                 "🔹 Per contattarci /contact")


def check_message(update, context):
    # update.message.reply_text("Message received")
    groups.try_add_group(update.message)


dispatcher = bot.updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('contact', contact_handler))
dispatcher.add_handler(CommandHandler('help', help_handler))
dispatcher.add_handler(CommandHandler('help_recensioni', reviews.help_handler))
dispatcher.add_handler(CommandHandler('recensione', reviews.add_review))
dispatcher.add_handler(CommandHandler('getgroupjson', groups.get_group_json))
dispatcher.add_handler(CommandHandler('getreviewjson', reviews.get_review_json))
dispatcher.add_handler(MessageHandler(Filters.all, check_message))

bot.updater.start_polling()
