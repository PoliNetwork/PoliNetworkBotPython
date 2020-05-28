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
# 2 - L'utente vuole fare una domanda

def user_started(user_id):
    set_state_to(user_id, 1)

    start_message = "Ciao! Benvenuto in AskPoliNetworkBot! 😎\n" \
                    "Questo è un bot di @PoliNetwork, visita il nostro sito! https://polinetwork.github.io/ \n" \
                    "\nTramite questo bot potrai porre domande e ottenere " \
                    "risposte (dai vari utenti del network) riguardo il politecnico! ❔\n"
    start_message += "\nCi appoggiamo a reddit, r/polinetwork. Puoi scegliere di porre domande direttamente dal " \
                     "subreddit o interagire col bot, che ti notificherà delle eventuali risposte! 🔔"
    s1 = 'Iniziamo!'
    s2 = 'Contatta gli amministratori'
    menu_main = [[InlineKeyboardButton(s1, callback_data=formatCallback(1, "start", s1))],
                 [InlineKeyboardButton(s2, callback_data=formatCallback(1, "contact", s2))]]
    reply_markup = InlineKeyboardMarkup(menu_main)
    variable_ask.updater.bot.send_message(user_id, start_message, reply_markup=reply_markup)
    pass


def user_help(update):
    pass


def user_send(user_id, desc):
    global subreddit

    user_state = getUserState(user_id)
    if user_state is None:
        return None

    title2 = user_state["title"]

    if title2 is None:
        return None

    if len(title2) > 0:
        post = subreddit.submit(title=title2, selftext=desc)
        flair = user_state["flair"]
        try:
            choices = post.flair.choices()
            template_id = next(x for x in choices
                               if x["flair_text_editable"])["flair_template_id"]
            post.flair.select(template_id, flair)
        except Exception as e2:
            print(e2)

        return "https://www.reddit.com/r/" + variable_ask.subreddit_name + "/comments/" + str(post.id)

    return None
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
            if state != state_num:
                user_state["state"] = state_num
                variable_ask.lock_ask_state.acquire()
                variable_ask.ask_list[id] = user_state
                variable_ask.write_ask_list2()
                variable_ask.lock_ask_state.release()


def user_ask(user_id):
    set_state_to(user_id, 0)

    s1 = 'Cerca una domanda'
    s2 = 'Fai una domanda'
    menu_main = [[InlineKeyboardButton(s1, callback_data=formatCallback(0, "search", s1))],
                 [InlineKeyboardButton(s2, callback_data=formatCallback(0, "ask", s2))]]
    reply_markup = InlineKeyboardMarkup(menu_main)
    variable_ask.updater.bot.send_message(user_id,
                                          'Benvenuto! Che cosa vuoi fare? Vuoi cercare una domanda per '
                                          'vedere se è già stata posta? O vuoi porne una nuova?',
                                          reply_markup=reply_markup)

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
    elif text.startswith("/ask"):
        user_ask(update.message.from_user.id)
    else:
        variable_ask.updater.bot.send_message(message.from_user.id,
                                              "Comando non riconosciuto! Contatta gli admin di @PoliNetwork")
    pass


def do_state2(user_id, current_state, args, text):
    if current_state == 0:  # /ask
        if args[1] == "search":
            variable_ask.updater.bot.send_message(user_id, "Cosa vuoi cercare?")
            return None
        elif args[1] == "ask":
            set_state_to(user_id, 2)

            flairs = variable_ask.flair_available
            menu_main2 = []

            len_flair = len(flairs)

            i = 0
            menu_main = []
            if (len_flair % 3) == 0:
                while i < len_flair:
                    menu_main2 = []
                    menu_main2.append(
                        InlineKeyboardButton(flairs[i + 0], callback_data=formatCallback(2, flairs[i + 0])))
                    menu_main2.append(
                        InlineKeyboardButton(flairs[i + 1], callback_data=formatCallback(2, flairs[i + 1])))
                    menu_main2.append(
                        InlineKeyboardButton(flairs[i + 2], callback_data=formatCallback(2, flairs[i + 2])))
                    menu_main.append(menu_main2)
                    i = i + 3

            elif (len_flair % 2) == 0:
                while i < len_flair:
                    menu_main2 = []
                    menu_main2.append(
                        InlineKeyboardButton(flairs[i + 0], callback_data=formatCallback(2, flairs[i + 0])))
                    menu_main2.append(
                        InlineKeyboardButton(flairs[i + 1], callback_data=formatCallback(2, flairs[i + 1])))
                    menu_main.append(menu_main2)
                    i = i + 2
            else:
                for item2 in flairs:
                    menu_main2 = [InlineKeyboardButton(item2, callback_data=formatCallback(2, item2))]
                    menu_main.append(menu_main2)

            r1 = InlineKeyboardMarkup(menu_main)
            variable_ask.updater.bot.send_message(user_id, "Scegli la categoria della domanda", reply_markup=r1)
            return None
    elif current_state == 1:  # /start
        if args[1] == "start":
            user_ask(user_id)
            return None
        elif args[1] == "contact":
            variable_ask.updater.bot.send_message(user_id, "Ti consigliamo contattarci tramite chat facebook, "
                                                           "trovi il link sul sito del network "
                                                           "https://polinetwork.github.io/\n"
                                                           "\nTorna al menu premendo /start")
            return None
        pass
    elif current_state == 2:  # l'utente vuole fare una domanda e gli è stata presentata la lista dei flair
        user_state = getUserState(user_id)
        user_state["flair"] = args[1]
        variable_ask.lock_ask_state.acquire()
        variable_ask.ask_list[user_id] = user_state
        variable_ask.write_ask_list2()
        variable_ask.lock_ask_state.release()

        variable_ask.updater.bot.send_message(user_id,
                                              "Scrivi il titolo della domanda (successivamente potrai scrivere la descrizione):")
        set_state_to(user_id, 3)
        return None
    elif current_state == 3:
        user_state = getUserState(user_id)
        user_state["title"] = text
        variable_ask.lock_ask_state.acquire()
        variable_ask.ask_list[user_id] = user_state
        variable_ask.write_ask_list2()
        variable_ask.lock_ask_state.release()

        variable_ask.updater.bot.send_message(user_id, "Descrivi dettagliatamente la tua domanda:")
        set_state_to(user_id, 4)

        return None
    elif current_state == 4:  # l'utente ha inserito il testo della domanda
        url = user_send(user_id, desc=text)
        variable_ask.updater.bot.send_message(user_id,
                                              "La tua domanda è stata inviata con successo! "
                                              "Riceverai eventuali update sulle risposte. "
                                              "Ti ricordiamo che puoi seguire anche il post reddit dedicato: "
                                              + str(url))
        user_ask(user_id)
        return None
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
    r = data.split(separators_callback)
    return r


def menu_actions(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    args = getArgsFromCallback(query.data)
    current_state = int(args[0])

    do_state(user_id, current_state, args, None)

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

    reddit.validate_on_submit = True

    subreddit = reddit.subreddit(variable_ask.subreddit_name)
    pass


if __name__ == "__main__":
    main_ask()
