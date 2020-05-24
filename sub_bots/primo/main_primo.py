from datetime import datetime, timedelta

from telegram.ext import MessageHandler, Filters

from sub_bots.primo import variable_primo
from sub_bots.primo.variable_primo import lock_primo_list

words = [
    {"word": "primo", "other": ["primo", "prima"]},
    {"word": "secondo", "other": ["secondo", "seconda"]},
    {"word": "terzo", "other": ["terzo", "terza"]},
    {"word": "kebabbaro", "other": ["kebabbaro", "kebabbara"]},
    {"word": "foco", "other": ["foco"]},
    {"word": "obeso", "other": ["obeso", "obesa"]},
    {"word": "magro", "other": ["magro", "magra"]},
    {"word": "ebreo", "other": ["ebreo", "ebrea"]},
    {"word": "imperatore", "other": ["imperatore", "imperatrice"]},
    {"word": "boomer", "other": ["boomer"]},
    {"word": "upkara", "other": ["upkara"]},
    {"word": "snitch", "other": ["snitch"]},
    {"word": "fattone", "other": ["fattone", "fattona"]},
    {"word": "ferruccio", "other": ["ferruccio"]},
    {"word": "pizzaiolo", "other": ["pizzaiolo", "pizzaiola"]},
    {"word": "lasagna", "other": ["lasagna"]}
]


def write_primo_list():
    variable_primo.write_primo_list2()
    pass


def getProperty(item, param_to_extract):
    r = None

    try:
        r = item[param_to_extract]
    except:
        pass

    return r
    pass


def check_if_already_won(primo_element, message, text):
    # TODO: vedere se il tizio ha già vinto da qualche parte

    list_counted = []
    for key in variable_primo.primo_list:
        iduser = getProperty(variable_primo.primo_list[key], "iduser")
        date2 = getProperty(variable_primo.primo_list[key], "date")

        if iduser is None:
            a = 0
        elif iduser is not None and date2 is None:
            if iduser == message.from_user.id:
                list_counted.append(key)
        elif iduser is not None and date2 is not None:
            if iduser == message.from_user.id:
                is_different_day = check_if_different_date(date2)
                if not is_different_day:
                    list_counted.append(key)

    return list_counted


def do_winner(primo_element, message, text):
    already_won_item = check_if_already_won(primo_element, message, text)
    if len(already_won_item) == 0:

        lock_primo_list.acquire()
        primo_element["iduser"] = message.from_user.id
        primo_element["date"] = datetime.timestamp(datetime.now())
        primo_element["first_name"] = message.from_user.first_name

        variable_primo.primo_list[text] = primo_element

        try:
            write_primo_list()
        except Exception as e:
            print(e)
        lock_primo_list.release()
        variable_primo.updater.bot.send_message(message.chat.id, "Congratulazioni, sei il re " + text + "!",
                                                reply_to_message_id=message.message_id)
    else:
        # TODO: invia un messaggio "sei già il re di already_won_item"
        r = ""
        for item in already_won_item:
            r = r + item + " "

        variable_primo.updater.bot.send_message(message.chat.id, "Sei già re " + str(r),
                                                reply_to_message_id=message.message_id)

        pass


def check_if_different_date(date):
    date2 = datetime.fromtimestamp(date) + timedelta(hours=2)
    now2 = datetime.now() + timedelta(hours=2)

    if date2.day == now2.day and date2.month == now2.month and date2.year == now2.year:
        return True

    return False


def check_winner(update, text):
    message = update.message

    primo_element = None
    try:
        primo_element = variable_primo.primo_list[text]
    except:
        primo_element = {}

    iduser = None

    try:
        iduser = primo_element["iduser"]
    except:
        pass

    date = None

    try:
        date = primo_element["date"]
    except:
        pass

    if not (iduser is not None and date is not None):
        do_winner(primo_element, message, text)
    else:

        is_different_day = check_if_different_date(date)

        if is_different_day:
            name_winner = message.from_user.first_name

            name_winner2 = None
            try:
                name_winner2 = primo_element["first_name"]
            except:
                pass

            if name_winner2 is not None:
                name_winner = name_winner2

            bot = variable_primo.updater.bot

            # bot.send_message(message.chat.id, str(iduser) + " " + str(message.from_user.id))

            if iduser != message.from_user.id:
                bot.send_message(message.chat.id,
                                 "C'è già <a href ='tg://user?id=" + str(iduser) + "'>" +
                                 name_winner + "</a> come re " + text + "!",
                                 reply_to_message_id=message.message_id, parse_mode="HTML")
            else:
                bot.send_message(message.chat.id,
                                 "Sei già il re " + text + "!",
                                 reply_to_message_id=message.message_id, parse_mode="HTML")
        else:
            do_winner(primo_element, message, text)

    pass


allowed_groups = [
    -1001129635578,  # gruppo cazzeggio di 2° livello
    5651789  # @ArmeF97
]


def check_if_valid(text):
    for item in words:
        item2 = item["other"]
        for item3 in item2:
            if text == item3:
                return True, item["word"]

    return False, None


def check_message_primo(update, context):
    message = update.message
    chat = message.chat

    if chat.id not in allowed_groups:
        return None

    text = message.text
    if text is None:
        return None

    if len(text) < 1:
        return None

    text = str(text).lower()

    valid, text_new = check_if_valid(text)
    if valid:
        text = text_new
        check_winner(update, text)

    return None


def main_primo():
    variable_primo.updater.dispatcher.add_handler(MessageHandler(Filters.all, check_message_primo))
    variable_primo.updater.start_polling()
