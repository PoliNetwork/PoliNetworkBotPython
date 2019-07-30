from telegram.ext import MessageHandler, CommandHandler, Filters

import variable
from features import groups, reviews, test, moderation
from functions import utils


def start_handler(update, context):
    update.message.reply_text("Ciao! 👋\n"
                              "\nScrivi /help per la lista completa delle mie funzioni 👀\n"
                              "\nVisita anche il nostro sito https://polinetwork.github.io")


def contact_handler(update, context):
    update.message.reply_text("Puoi scriverci alla pagina facebook https://m.me/PolitecnicoDiMilanoNetwork")


def help_handler(update, context):
    variable.updater.bot.send_message(update.message.chat.id,
                                      "<i>Lista di funzioni</i>:\n"
                                      "\n📑 Sistema di recensioni dei corsi (per maggiori info /help_recensioni)\n"
                                      "\n🙋 <a href='https://polinetwork.github.io/it/faq/index.html'>"
                                      "FAQ (domande frequenti)</a>\n"
                                      "\n🏫 Bot ricerca aule libere @AulePolimiBot\n"
                                      "\n✍ Per contattarci /contact",
                                      parse_mode="HTML")


def check_message(update, context):
    # update.message.reply_text("Message received")
    groups.try_add_group(update.message)


dispatcher = variable.updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('contact', contact_handler))
dispatcher.add_handler(CommandHandler('help', help_handler))
dispatcher.add_handler(CommandHandler('help_recensioni', reviews.help_handler))
dispatcher.add_handler(CommandHandler('recensione', reviews.add_review))
dispatcher.add_handler(CommandHandler('ottieni_recensioni', reviews.get_reviews_html))
dispatcher.add_handler(CommandHandler('getgroupjson', groups.get_group_json))
dispatcher.add_handler(CommandHandler('getreviewjson', reviews.get_review_json))
dispatcher.add_handler(CommandHandler('testmessage', test.test_message))
dispatcher.add_handler(CommandHandler('mute', moderation.mute))
dispatcher.add_handler(CommandHandler('ban', moderation.ban))
dispatcher.add_handler(CommandHandler('banAll', moderation.ban_all))

dispatcher.add_handler(MessageHandler(Filters.all, check_message))

thread = utils.DeleteMessageThread()
thread.start()

variable.updater.start_polling()
