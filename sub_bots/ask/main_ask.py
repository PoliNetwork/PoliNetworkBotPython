import threading
import time

import praw
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackQueryHandler

from sub_bots.ask import variable_ask
from sub_bots.ask.ask_utils import getUserState, tryGetProperty, formatCallback, set_state_to, user_ask
from sub_bots.ask.state_management import do_state2


def user_started(user_id):
    set_state_to(user_id, 1)

    start_message = "Ciao! Benvenuto in AskPoliNetworkBot! 😎\n" \
                    "Questo è un bot di @PoliNetwork, visita il nostro sito! https://polinetwork.github.io/ \n" \
                    "\nTramite questo bot potrai porre domande e ottenere " \
                    "risposte (dai vari utenti del network) riguardo il politecnico! ❔\n"
    start_message += '\nCi appoggiamo a reddit, r/polinetwork. Puoi scegliere di porre domande direttamente dal ' \
                     'subreddit o interagire col bot, che ti notificherà delle eventuali risposte! 🔔'
    s1 = 'Iniziamo!'
    s2 = 'Contatta gli amministratori'
    menu_main = [[InlineKeyboardButton(s1, callback_data=formatCallback(1, "start", s1))],
                 [InlineKeyboardButton(s2, callback_data=formatCallback(1, "contact", s2))]]
    reply_markup = InlineKeyboardMarkup(menu_main)
    variable_ask.updater.bot.send_message(user_id, start_message, reply_markup=reply_markup)
    pass


def user_help(update):
    pass


def user_cancel(user_id):
    user_started(user_id)
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
    elif text.startswith("/cancel"):
        user_cancel(update.message.from_user.id)
    elif text.startswith("/ask"):
        user_ask(update.message.from_user.id)
    else:
        variable_ask.updater.bot.send_message(message.from_user.id,
                                              "Comando non riconosciuto! Contatta gli admin di @PoliNetwork")
    pass


def do_state(user_id, current_state, args, text):
    if current_state == -1:
        user_state = getUserState(user_id)
        if user_state is None:
            user_started(user_id)
            return None

        state = tryGetProperty(user_state, "state")
        if state is None:
            user_started(user_id)
            return None

        current_state = state

    if args is None:
        user_state = getUserState(user_id)
        if user_state is None:
            user_started(user_id)
            return None

        args = tryGetProperty(user_state, "args")

    try:
        do_state2(user_id, current_state, args, text)
    except Exception as e:
        print(e)

    pass


def check_message_ask(update, context):
    message = update.message
    text = str(message.text)

    message = update.message
    if message.chat.type != "private":
        return None

    if text.startswith("/"):
        check_command(update, text)
        return None

    user_id = update.message.from_user.id
    do_state(user_id, -1, None, text)

    pass


def getArgsFromCallback(data):
    data = str(data)
    r = data.split(variable_ask.separators_callback)
    return r


def menu_actions(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    args = getArgsFromCallback(query.data)
    current_state = int(args[0])

    do_state(user_id, current_state, args, None)

    chosen = str(args[2])
    if chosen is None or len(chosen) == 0:
        chosen = str(args[1])
    query.edit_message_text(text="Hai scelto: [" + chosen + "]")
    pass


def send_notify_new_comment(postid, missing_comment, submission):
    if len(missing_comment) == 0:
        return None

    user_id = variable_ask.watch_post_list[postid]["from_tg"]
    title_post = submission.title
    if len(missing_comment) == 1:
        variable_ask.updater.bot.send_message(user_id, "C'è un nuovo commento al tuo post (" + str(title_post) + ")")
    else:
        variable_ask.updater.bot.send_message(user_id,
                                              "Ci sono dei nuovi commenti al tuo post (" + str(title_post) + ")")

    for item_comment in missing_comment:
        a = 0

        s = "▫️ commento:\n\n"
        s += item_comment.body

        s1 = "Rispondi"
        s2 = "Non rispondere"
        menu_main = [
            [InlineKeyboardButton(s1, callback_data=formatCallback(10, item_comment.id, s1, postid))],
            [InlineKeyboardButton(s2, callback_data=formatCallback(11, s2, s2))],
                     ]
        reply_markup2 = InlineKeyboardMarkup(menu_main)

        variable_ask.updater.bot.send_message(user_id, s)
        variable_ask.updater.bot.send_message(user_id, "Vuoi rispondere?", reply_markup=reply_markup2)

    pass


def check_comments(name):
    while True:
        for key in variable_ask.watch_post_list:

            submission = variable_ask.reddit.submission(id=key)
            comments1 = submission.comments
            comments2 = []
            for item_comment in comments1:
                comments2.append(item_comment)

            missing_comment = []
            comment_known = variable_ask.watch_post_list[key]["comments"]
            for item_comment in comments2:

                found = False
                for item_comment2 in comment_known:
                    if item_comment2 == item_comment.id:
                        found = True
                        break

                if found is False:
                    missing_comment.append(item_comment)

            if len(missing_comment) > 0:
                send_notify_new_comment(key, missing_comment, submission)

                variable_ask.lock_watch_post.acquire()

                for item_comment in missing_comment:
                    variable_ask.watch_post_list[key]["comments"][item_comment.id] = {}

                variable_ask.write_watch_post_list2()

                variable_ask.lock_watch_post.release()

        time.sleep(5 * 60)  # 5 minuti


def main_ask():

    variable_ask.updater.dispatcher.add_handler(CallbackQueryHandler(menu_actions))
    variable_ask.updater.dispatcher.add_handler(MessageHandler(Filters.all, check_message_ask))
    variable_ask.updater.start_polling()

    variable_ask.reddit = praw.Reddit(client_id=variable_ask.reddit_client_id,
                         client_secret=variable_ask.reddit_secret_id,
                         user_agent="AskPoliNetworkBot",
                         username="PolinetworkPostBot",
                         password=variable_ask.reddit_password)

    variable_ask.reddit.validate_on_submit = True

    variable_ask.subreddit = variable_ask.reddit.subreddit(variable_ask.subreddit_name)

    x = threading.Thread(target=check_comments, args=(1,))
    x.start()

    pass


if __name__ == "__main__":
    main_ask()
