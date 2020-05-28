import praw
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CommandHandler, CallbackQueryHandler

from sub_bots.ask import variable_ask
from praw import *

global reddit
global subreddit


# stati:
# 0 - Chiedi all'utente se vuole fare una domanda o cercare una domanda
# 1 - Start - Chiedi all'utente che vuole fare

def user_started(user_id):
    set_state_to(user_id, 1)

    s1 = 'Iniziamo!'
    s2 = 'Contatta gli amministratori'
    menu_main = [[InlineKeyboardButton(s1, callback_data=formatCallback(1, "start", s1))],
                 [InlineKeyboardButton(s2, callback_data=formatCallback(1, "contact", s2))]]
    reply_markup = InlineKeyboardMarkup(menu_main)
    variable_ask.updater.bot.send_message(user_id, 'Cosa vuoi fare?', reply_markup=reply_markup)
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


def getUserState(id):
    try:
        return variable_ask.ask_list[id]
    except:
        return None

    return None


def tryGetProperty(user_state, param):
    try:
        return user_state[param]
    except:
        return None

    return None


separators_callback = "|;|"


def formatCallback(*a):
    r = ""
    for a2 in a:
        r += str(a2) + separators_callback
    return r


def send_message_ask_0(user_id):
    s1 = 'Cerca una domanda'
    s2 = 'Fai una domanda'
    menu_main = [[InlineKeyboardButton(s1, callback_data=formatCallback(0, "search", s1))],
                 [InlineKeyboardButton(s2, callback_data=formatCallback(0, "ask", s2))]]
    reply_markup = InlineKeyboardMarkup(menu_main)
    variable_ask.updater.bot.send_message(user_id, 'Cosa vuoi fare?', reply_markup=reply_markup)

    pass


def set_state_to(user_id, state_num):
    id = user_id
    user_state = getUserState(user_id)
    if user_state is None:
        user_state = {"state": state_num}
        variable_ask.lock_ask_state.acquire()
        variable_ask.ask_list[id] = user_state
        variable_ask.write_ask_list2()
        variable_ask.lock_ask_state.release()
    else:
        state = tryGetProperty(user_state, "state")
        if state is None:
            user_state["state"] = state_num
            variable_ask.lock_ask_state.acquire()
            variable_ask.ask_list[id] = user_state
            variable_ask.write_ask_list2()
            variable_ask.lock_ask_state.release()
        else:
            if state != 0:
                user_state["state"] = state_num
                variable_ask.lock_ask_state.acquire()
                variable_ask.ask_list[id] = user_state
                variable_ask.write_ask_list2()
                variable_ask.lock_ask_state.release()


def user_ask(user_id):
    set_state_to(user_id, 0)
    send_message_ask_0(user_id)

    pass


def check_command(update, text):
    message = update.message
    if message.chat.type != "private":
        return None

    text = str(text).lower()

    if text.startswith("/start"):
        user_started(update.message.from_user.id)
    elif text.startswith("/help"):
        user_help(update)
    elif text.startswith("/send"):
        user_send(update)
    elif text.startswith("/ask"):
        user_ask(update.message.from_user.id)
    else:
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


def getArgsFromCallback(data):
    data = str(data)
    r = data.split(separators_callback)
    return r


def menu_actions(update, context):
    query = update.callback_query

    args = getArgsFromCallback(query.data)
    current_state = int(args[0])
    if current_state == 0: #/ask
        if args[1] == "search":
            variable_ask.updater.bot.send_message(query.from_user.id, "Cosa vuoi cercare?")
        elif args[1] == "ask":
            variable_ask.updater.bot.send_message(query.from_user.id, "Cosa vuoi chiedere?")
    elif current_state == 1: #/start
        if args[1] == "start":
            user_ask(query.from_user.id)
        elif args[1] == "contact":
            variable_ask.updater.bot.send_message(query.from_user.id, "Cosa vuoi chiedere?")
        pass

    query.edit_message_text(text="Hai scelto: [" + str(args[2]) + "]")
    pass


def main_ask():
    global reddit
    global subreddit

    variable_ask.updater.dispatcher.add_handler(CallbackQueryHandler(menu_actions))
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
