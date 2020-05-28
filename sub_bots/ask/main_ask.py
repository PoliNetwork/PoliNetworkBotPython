import praw
from telegram.ext import MessageHandler, Filters

from sub_bots.ask import variable_ask
from praw import *

global reddit
global subreddit


def user_started(update):
    pass


def user_help(update):
    pass


def user_send(update):
    global subreddit

    text = update.message.text
    text = str(text)[5:]
    text = str(text).strip()

    if text is not None and len(text) > 0:
        subreddit.submit(title=text, selftext=text)

    pass


def check_command(update, text):
    text = str(text).lower()

    if text.startswith("/start"):
        user_started(update)
    elif text.startswith("/help"):
        user_help(update)
    elif text.startswith("/send"):
        user_send(update)
    else:
        message = update.message
        if message.chat.type != "private":
            return None

        variable_ask.updater.bot.send_message(message.from_user.id,
                                              "Comando non riconosciuto! Contatta gli admin di @PoliNetwork")
    pass


def check_message_ask(update, context):
    message = update.message
    text = str(message.text)

    if text.startswith("/"):
        check_command(update, text)

    # variable_ask.updater.bot.send_message(message.from_user.id, "Ciao")

    pass


def main_ask():
    global reddit
    global subreddit

    variable_ask.updater.dispatcher.add_handler(MessageHandler(Filters.all, check_message_ask))
    variable_ask.updater.start_polling()

    reddit = praw.Reddit(client_id=variable_ask.reddit_client_id,
                         client_secret=variable_ask.reddit_secret_id,
                         user_agent="AskPoliNetworkBot",
                         username="PolinetworkPostBot",
                         password=variable_ask.reddit_password)

    subreddit = reddit.subreddit("polinetworktest")
    a = 0
    a = a + 1


if __name__ == "__main__":
    main_ask()
