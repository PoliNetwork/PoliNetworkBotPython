import threading
import time

import praw
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackQueryHandler

from sub_bots.ask import variable_ask

global reddit
global subreddit


# stati:
# 0 - Chiedi all'utente se vuole fare una domanda o cercare una domanda
# 1 - Start - Chiedi all'utente che vuole fare
# 2 - L'utente vuole fare una domanda e gli è stata presentata la lista dei flair
# 3 - L'utente ha scelto il titolo e ora gli viene chiesta la descrizione
# 4 - L'utente ha scelto la descrizione e il suo post viene ora pubblicato

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

        variable_ask.lock_watch_post.acquire()
        variable_ask.watch_post_list[post.id] = {}
        variable_ask.watch_post_list[post.id]["from_tg"] = user_id
        variable_ask.watch_post_list[post.id]["comments"] = {}
        variable_ask.write_watch_post_list2()
        variable_ask.lock_watch_post.release()

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
    s3 = "Gestisci le notifiche"
    menu_main = [
        [InlineKeyboardButton(s1, callback_data=formatCallback(0, "search", s1))],
        [InlineKeyboardButton(s2, callback_data=formatCallback(0, "ask", s2))],
        [InlineKeyboardButton(s3, callback_data=formatCallback(0, "notify", s3))]
    ]
    reply_markup = InlineKeyboardMarkup(menu_main)
    variable_ask.updater.bot.send_message(user_id,
                                          'Benvenuto! Che cosa vuoi fare? Vuoi cercare una domanda per '
                                          'vedere se è già stata posta? O vuoi porne una nuova?',
                                          reply_markup=reply_markup)

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


def notify_choose(user_id, repeat=True):
    set_state_to(user_id, 5)

    r1 = 'Qui puoi gestire le categorie di post a cui sei iscritto. ' \
         'Quando qualcuno pone una domanda ad una categoria ' \
         'di post a cui sei iscritto, ti notificheremo'

    if repeat is True:
        variable_ask.updater.bot.send_message(user_id, str(r1))

    s1 = 'Mostra le categorie di post a cui sono iscritto'
    s2 = "Iscriviti ad una nuova categoria"
    s3 = "Disiscriviti da una categoria"
    menu_main = [
        [InlineKeyboardButton(s1, callback_data=formatCallback(6, "show", s1))],
        [InlineKeyboardButton(s2, callback_data=formatCallback(6, "add", s2))],
        [InlineKeyboardButton(s3, callback_data=formatCallback(6, "remove", s3))]
    ]
    reply_markup = InlineKeyboardMarkup(menu_main)
    variable_ask.updater.bot.send_message(user_id,
                                          "Cosa scegli? (per tornare al menu principale premi /cancel)",
                                          reply_markup=reply_markup)


def createMenuFlair(param_state, flairs):
    menu_main2 = []
    len_flair = len(flairs)
    i = 0
    menu_main = []
    if (len_flair % 3) == 0:
        while i < len_flair:
            menu_main2 = [InlineKeyboardButton(flairs[i + 0], callback_data=formatCallback(param_state, flairs[i + 0])),
                          InlineKeyboardButton(flairs[i + 1], callback_data=formatCallback(param_state, flairs[i + 1])),
                          InlineKeyboardButton(flairs[i + 2], callback_data=formatCallback(param_state, flairs[i + 2]))]
            menu_main.append(menu_main2)
            i = i + 3

    elif (len_flair % 2) == 0:
        while i < len_flair:
            menu_main2 = [InlineKeyboardButton(flairs[i + 0], callback_data=formatCallback(param_state, flairs[i + 0])),
                          InlineKeyboardButton(flairs[i + 1], callback_data=formatCallback(param_state, flairs[i + 1]))]
            menu_main.append(menu_main2)
            i = i + 2
    else:
        for item2 in flairs:
            menu_main2 = [InlineKeyboardButton(item2, callback_data=formatCallback(param_state, item2))]
            menu_main.append(menu_main2)

    return menu_main


def do_state2(user_id, current_state, args, text):
    if current_state == 0:  # /ask
        if args[1] == "search":
            set_state_to(user_id, 9)
            variable_ask.updater.bot.send_message(user_id, "Cosa vuoi cercare? (annulla con /cancel)")
            return None
        elif args[1] == "ask":
            set_state_to(user_id, 2)

            menu_main = createMenuFlair(2, variable_ask.flair_available)

            r1 = InlineKeyboardMarkup(menu_main)
            variable_ask.updater.bot.send_message(user_id,
                                                  "Scegli la categoria della domanda \n(annulla tutto con /cancel)",
                                                  reply_markup=r1)
            return None

        elif args[1] == "notify":
            notify_choose(user_id)

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
                                              "Scrivi il titolo della domanda "
                                              "(successivamente potrai scrivere la descrizione):"
                                              "\n(annulla tutto con /cancel)")
        set_state_to(user_id, 3)
        return None
    elif current_state == 3:  # l'utente ha scelto il titolo e ora deve scrivere la descrizione
        user_state = getUserState(user_id)
        user_state["title"] = text
        variable_ask.lock_ask_state.acquire()
        variable_ask.ask_list[user_id] = user_state
        variable_ask.write_ask_list2()
        variable_ask.lock_ask_state.release()

        variable_ask.updater.bot.send_message(user_id,
                                              "Descrivi dettagliatamente la tua domanda: \n(annulla tutto con /cancel)")
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
    elif current_state == 5:
        notify_choose(user_id)
    elif current_state == 6:  # l'utente ha scelto quale sotto-azione inerente alle notifiche vuole fare
        if args[1] == "show":
            my_list = []
            for cat in variable_ask.ask_notify_list:
                if user_id in variable_ask.ask_notify_list[cat]:
                    my_list.append(cat)

            notify_choose(user_id, False)

            if len(my_list) > 0:

                my_list2 = "\n"
                for item in my_list:
                    my_list2 += item + "\n"

                variable_ask.updater.bot.send_message(user_id, "Lista delle categorie a cui sei iscritto: " + my_list2)
            else:
                variable_ask.updater.bot.send_message(user_id, "Non sei iscritto a nessuna categoria!")

            return None

        elif args[1] == "add":
            my_list = []
            for cat in variable_ask.ask_notify_list:
                if user_id in variable_ask.ask_notify_list[cat]:
                    my_list.append(cat)

            to_add = []
            for item in variable_ask.flair_available:
                if item not in my_list:
                    to_add.append(item)

            if len(to_add) > 0:

                menu_main = createMenuFlair(7, to_add)
                reply_markup = InlineKeyboardMarkup(menu_main)
                variable_ask.updater.bot.send_message(user_id, "Quale categoria vuoi aggiungere?",
                                                      reply_markup=reply_markup)
            else:
                notify_choose(user_id)
                variable_ask.updater.bot.send_message(user_id, "Nessuna categoria da aggiungere! Sei iscritto a tutte!")
            return None
        elif args[1] == "remove":

            my_list = []
            for cat in variable_ask.ask_notify_list:
                if user_id in variable_ask.ask_notify_list[cat]:
                    my_list.append(cat)

            if len(my_list) > 0:
                menu_main = createMenuFlair(8, my_list)
                reply_markup = InlineKeyboardMarkup(menu_main)
                variable_ask.updater.bot.send_message(user_id, "Quale categoria vuoi rimuovere?",
                                                      reply_markup=reply_markup)
            else:
                notify_choose(user_id)
                variable_ask.updater.bot.send_message(user_id, "Nessuna categoria da rimuovere! "
                                                               "Non sei iscritto a nessuna!")

            return None
    elif current_state == 7:  # l'utente ha scelto quale categoria vuole aggiungere
        variable_ask.lock_ask_notify_state.acquire()

        cat = args[1]

        cat2 = tryGetProperty(variable_ask.ask_notify_list, cat)
        if cat2 is None:
            variable_ask.ask_notify_list[cat] = []

        variable_ask.ask_notify_list[cat].append(user_id)

        variable_ask.write_ask_notify_list2()

        variable_ask.lock_ask_notify_state.release()

        notify_choose(user_id)
        variable_ask.updater.bot.send_message(user_id, "Categoria aggiunta con successo!")

    elif current_state == 8:  # l'utente ha scelto quale categoria vuole rimuovere
        variable_ask.lock_ask_notify_state.acquire()

        cat = args[1]

        cat2 = tryGetProperty(variable_ask.ask_notify_list, cat)
        if cat2 is None:
            variable_ask.ask_notify_list[cat] = []

        variable_ask.ask_notify_list[cat].remove(user_id)

        variable_ask.write_ask_notify_list2()

        variable_ask.lock_ask_notify_state.release()

        notify_choose(user_id)
        variable_ask.updater.bot.send_message(user_id, "Categoria rimossa con successo!")
    elif current_state == 9:  # l'utente ha inserito il testo da cercare
        results = subreddit.search(text)

        results2 = []

        for result_item in results:
            results2.append(result_item)

        n_result = len(results2)

        if n_result > 5:
            n_result = 5

        i = 0
        s = "\n"

        while i < n_result:
            url2 = "https://www.reddit.com/r/" + variable_ask.subreddit_name + "/comments/" + results2[i].id
            url = "<a href='" + url2 + "'>"
            url += results2[i].title
            url += "</a>"

            s += "▫️ "
            s += url
            s += "\n"

            i = i + 1

        if n_result > 0:
            variable_ask.updater.bot.send_message(user_id, "Ecco i risultati:\n" + s + "\n\nTorna al menu con /start",
                                                  parse_mode="HTML")
        else:
            variable_ask.updater.bot.send_message(user_id, "Nessun risultato! (torna al menu con /start)" + s)
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

    chosen = str(args[2])
    if chosen is None or len(chosen) == 0:
        chosen = str(args[1])
    query.edit_message_text(text="Hai scelto: [" + chosen + "]")
    pass


def send_notify_new_comment(postid, missing_comment):
    pass


def check_comments(name):
    while True:
        for key in variable_ask.watch_post_list:
            a = 0
            submission = reddit.submission(id=key)
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
                send_notify_new_comment(key, missing_comment)

                variable_ask.lock_watch_post.acquire()

                for item_comment in missing_comment:
                    variable_ask.watch_post_list[key]["comments"][item_comment.id] = {}

                variable_ask.write_watch_post_list2()

                variable_ask.lock_watch_post.release()


            a = a + 1

        time.sleep(5 * 60)  # 5 minuti


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

    x = threading.Thread(target=check_comments, args=(1,))
    x.start()

    pass


if __name__ == "__main__":
    main_ask()
