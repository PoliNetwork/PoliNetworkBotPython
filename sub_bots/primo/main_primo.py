from datetime import datetime

from telegram.ext import MessageHandler, Filters

from sub_bots.primo import variable_primo
from sub_bots.primo.variable_primo import lock_primo_list

words = ["primo", "secondo", "terzo", "kebabbaro", "foco", "obeso", "magro", "ebreo", "imperatore", "boomer", "upkara", "snitch", "fattone"]


def write_primo_list():
    variable_primo.write_primo_list2()
    pass


def do_winner(primo_element, message, text):
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
    variable_primo.updater.bot.send_message(message.chat.id, "Congratulazioni, sei il re " + text + "!", reply_to_message_id=message.message_id)


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
        date2 = datetime.fromtimestamp(date)
        now2 = datetime.now()

        if date2.day == now2.day and date2.month == now2.month and date2.year == now2.year:
            name_winner = message.from_user.first_name

            name_winner2 = None
            try:
                name_winner2 = primo_element["first_name"]
            except:
                pass

            if name_winner2 is not None:
                name_winner = name_winner2

            variable_primo.updater.bot.send_message(message.chat.id, "Oggi è il giorno " + str(now2.day) + " ore  " + str(now2.hour) + " minuti " + str(now2.minute) +". C'è già <a href ='tg://user?id=" + str(iduser) + "'>"+name_winner+"</a> come re " + text + "!", reply_to_message_id=message.message_id, parse_mode="HTML")
        else:
            do_winner(primo_element, message, text)

    pass


allowed_groups = [-1001129635578, 5651789]


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

    if text in words:
        check_winner(update, text)

    return None


def main_primo():
    variable_primo.updater.dispatcher.add_handler(MessageHandler(Filters.all, check_message_primo))
    variable_primo.updater.start_polling()


