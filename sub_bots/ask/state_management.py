from telegram import InlineKeyboardMarkup

from config.blacklist_words import blacklist_words
from sub_bots.ask import variable_ask
from sub_bots.ask.ask_utils import set_state_to, createMenuFlair, notify_choose, user_ask, getUserState, user_send, \
    tryGetProperty


# stati:
# 00 - Chiedi all'utente se vuole fare una domanda o cercare una domanda
# 01 - Start - Chiedi all'utente che vuole fare
# 02 - L'utente vuole fare una domanda e gli è stata presentata la lista dei flair
# 03 - L'utente ha scelto il titolo e ora gli viene chiesta la descrizione
# 04 - L'utente ha scelto la descrizione e il suo post viene ora pubblicato
# 10 - L'utente ha scelto di rispondere ad un commento


def check_if_valid_to_blacklist(text):
    text2 = str(text).split(" ")
    for word in text2:
        if word in blacklist_words:
            return False

    return True


def reset_bad_char(user_id):
    variable_ask.updater.bot.send_message(user_id,
                                          "Ciò che hai scritto contiene delle parole che non rispettano il "
                                          "linguaggio consono del network. Ti invitiamo a leggere le regole "
                                          "del network.\n\nL'operazione è stata annullata")
    user_ask(user_id)
    pass


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

        valid_text = check_if_valid_to_blacklist(text)
        if valid_text:

            user_state = getUserState(user_id)
            user_state["title"] = text
            variable_ask.lock_ask_state.acquire()
            variable_ask.ask_list[user_id] = user_state
            variable_ask.write_ask_list2()
            variable_ask.lock_ask_state.release()

            variable_ask.updater.bot.send_message(user_id,
                                                  "Descrivi dettagliatamente la tua domanda: \n(annulla tutto con /cancel)")
            set_state_to(user_id, 4)
        else:
            reset_bad_char(user_id)
            return None

        return None
    elif current_state == 4:  # l'utente ha inserito il testo della domanda

        valid_text = check_if_valid_to_blacklist(text)
        if valid_text:
            url = user_send(user_id, desc=text)
            variable_ask.updater.bot.send_message(user_id,
                                                  "La tua domanda è stata inviata con successo! "
                                                  "Riceverai eventuali update sulle risposte. "
                                                  "Ti ricordiamo che puoi seguire anche il post reddit dedicato: "
                                                  + str(url))
        else:
            reset_bad_char(user_id)
            return None
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
        results = variable_ask.subreddit.search(text)

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

    elif current_state == 10:  # l'utente vuole rispondere ad un commento

        set_state_to(user_id, 12)

        comment_id = args[1]
        post_id = args[3]

        variable_ask.lock_ask_state.acquire()

        variable_ask.ask_list[user_id]["comment_id"] = comment_id
        variable_ask.ask_list[user_id]["post_id"] = post_id

        variable_ask.write_ask_list2()

        variable_ask.lock_ask_state.release()

        variable_ask.updater.bot.send_message(user_id, "Inserisci il commento di risposta che vuoi dare:")
    elif current_state == 11:  # l'utente non vuole rispondere
        user_ask(user_id)
        return None
    elif current_state == 12:  # l'utente ha scritto la sua risposta

        valid_text = check_if_valid_to_blacklist(text)
        if valid_text is False:
            reset_bad_char(user_id)
            return None
        a = 0
    pass
