from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

from features import groups, reviews


def start(update, context):
    update.message.reply_text("Bot started")


def check_message(update, context):
    # update.message.reply_text("Message received")
    groups.try_add_group(update.message)


def get_group_json(update, context):
    message = update.message
    chat = message.chat
    if chat.id == 5651789:  # id of @ArmeF97
        groups.send_group_json(message)


token = open("token.txt").read()
updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('recensione', reviews.add_review))

group_handler = CommandHandler('getgroupjson', get_group_json)

dispatcher.add_handler(group_handler)
dispatcher.add_handler(MessageHandler(Filters.all, check_message))

updater.start_polling()
