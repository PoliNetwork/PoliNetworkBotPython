from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from sub_bots.ask import variable_ask


def set_state_to(user_id, state_num):
    user_id = int(user_id)
    user_state = getUserState(user_id)
    if user_state is None:
        user_state = {"state": state_num}
        variable_ask.lock_ask_state.acquire()
        variable_ask.ask_list[user_id] = user_state
        variable_ask.write_ask_list2()
        variable_ask.lock_ask_state.release()
    else:
        state = tryGetProperty(user_state, "state")
        if state is None:
            user_state["state"] = state_num
            variable_ask.lock_ask_state.acquire()
            variable_ask.ask_list[user_id] = user_state
            variable_ask.write_ask_list2()
            variable_ask.lock_ask_state.release()
        else:
            if state != state_num:
                user_state["state"] = state_num
                variable_ask.lock_ask_state.acquire()
                variable_ask.ask_list[user_id] = user_state
                variable_ask.write_ask_list2()
                variable_ask.lock_ask_state.release()


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


def formatCallback(*a):
    r = ""
    for a2 in a:
        r += str(a2) + variable_ask.separators_callback
    return r


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


def getAuthor(user_id):
    return "[nessun autore per ora]"
    pass


def user_send(user_id, desc):
    user_state = getUserState(user_id)
    if user_state is None:
        return None

    title2 = user_state["title"]

    if title2 is None:
        return None

    if len(title2) > 0:
        desc += "\n\n"
        author = getAuthor(user_id)
        desc += "authour: " + author
        post = variable_ask.subreddit.submit(title=title2, selftext=desc)
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
