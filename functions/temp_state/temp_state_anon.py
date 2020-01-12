# Con questo modulo, si gestisce la possibilità di usare uno stato dell'utente.
# Esempio: io do un comando, il bot mi chiede "scrivi questo", io lo scrivo, poi il bot mi chiede
# "scrivi quest'altro". Il bot per seguirti ha bisogno di sapere, nella macchina a stati finiti,
# in quale punto ti trovi. Dopo 5 minuti lo stato sarà cancellato da un thread dedicato.
# Ogni qualvolta che un utente aggiorna il suo stato, i 5 minuti si resettano.
# Allo scadere dei 5 minuti di un utente, gli viene inviato il messaggio che la sua sessione è scaduta.
# Ovviamente, se l'utente completa la macchina a stati con successo arrivando alla fine,
# la sua sessione sarà rimossa senza dare nessun avviso.

# Gli stati sono un json che ha come chiave l'id telegram della persona, e come valore al suo interno 2 valori
# "date", "module", "state", "values" dove "module" è una stringa, è il nome della macchina a stati finiti che
# l'utente sta attraversando dove "state" è il punto della macchina a stati finiti in cui l'utente si trova dove
# "values" è un array di stringhe, delle variabili opzionali utili per passarsi valori man mano che si avanza negli
# stati

# {123:{"date":"2019-12-31_23:59", "module":"abc", "state": "1a", "values":["v1", "v2"]}}
# qui sopra un esempio, 123 è l'id telegram, abc il nome
# del modulo, 1a lo stato, v1 e v2 i valori dell'array dei valori.

# Per gestire il tutto serve un thread di eliminazione, un json scritto su file, e un lock che si usa scrittura. Nota
# bene: il lock potrebbe anche essere messo in una funzione di lettura, se nel suo percorso di esecuzione c'è anche
# solo la possibilità che scriva.
import datetime

import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import main_anon
from functions.temp_state import temp_state_variable_anon
from sub_bots.anon import variable_anon


def get_state(id_telegram):
    for ass in temp_state_variable_anon.state_dict.keys():
        if ass == id_telegram:
            return temp_state_variable_anon.state_dict.get(ass)
    return None


def overwrite_state(id_telegram, stato):
    temp_state_variable_anon.lock_state.acquire()

    if temp_state_variable_anon.state_dict[id_telegram] is None:
        # todo: occhio! bisogna controllare che ci sia qualcosa nel json, perché se è vuoto, è stato eliminato
        temp_state_variable_anon.lock_state.release()
        return None

    temp_state_variable_anon.state_dict[id_telegram] = stato
    temp_state_variable_anon.save_file_no_lock()
    temp_state_variable_anon.lock_state.release()
    return None


def not_supported_exception(id):
    variable_anon.updater.bot.send_message(chat_id=id,
                                           text="Questa funzione non è ancora supportata!")
    temp_state_variable_anon.delete_state(id)


def next_anon1(update, id_telegram, stato):

    if stato["state"] == "0":

        if update.callback_query is None:
            return None

        # dipende dal callback data
        cb = str(update.callback_query.data)

        main_anon.post_anonimi2(stato["values"]["data"], stato["values"]["message"]["reply_to_message"], identity=cb)

        temp_state_variable_anon.delete_state(id_telegram)

        return None

    elif stato["state"] == "0t2":

        if update.callback_query is None:
            return None

        # dipende dal callback data
        cb = str(update.callback_query.data)

        m2 = stato["values"]["message"]
        main_anon.post_anonimi2(data=None, message=m2, identity=cb)

        temp_state_variable_anon.delete_state(id_telegram)

        return None

    elif stato["state"] == "0t":

        if update.callback_query is None:
            return None

        # dipende dal callback data
        cb = str(update.callback_query.data)

        if cb != "0":
            variable_anon.updater.bot.send_message(chat_id=stato["values"]["message"]["from_user"]["id"],
                                                   text="Ok, se vuoi altre info, scrivi /help",
                                                   parse_mode="HTML")
            temp_state_variable_anon.delete_state(id_telegram)
            return

        keyboard = [
            [
                InlineKeyboardButton(text="ANONIMO", callback_data="0")
            ],
            [
                InlineKeyboardButton(text="IDENTITA' 1", callback_data="1")
            ],
            [
                InlineKeyboardButton(text="IDENTITA' 2", callback_data="2")
            ],
            [
                InlineKeyboardButton(text="IDENTITA' 3", callback_data="3")
            ],
            [
                InlineKeyboardButton(text="IDENTITA' 4", callback_data="4")
            ],
            [
                InlineKeyboardButton(text="IDENTITA' 5", callback_data="5")
            ],
            [
                InlineKeyboardButton(text="IDENTITA' 6", callback_data="6")
            ],
            [
                InlineKeyboardButton(text="IDENTITA' 7", callback_data="7")
            ]

        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        variable_anon.updater.bot.send_message(chat_id=stato["values"]["message"]["from_user"]["id"],
                                               text="Con quale identità anonima vuoi pubblicare?",
                                               reply_markup=reply_markup,
                                               parse_mode="HTML")

        stato["state"] = "0t2"
        overwrite_state(id_telegram, stato)

        return None

    return None


def next_main(id_telegram, update):
    # noinspection PyNoneFunctionAssignment
    stato = get_state(id_telegram)
    if stato is None:
        return None

    if stato["module"] == 'anon1':
        return next_anon1(update, id_telegram, stato)

    return None


def create_state(module, state, id_telegram, values):
    now = datetime.datetime.now()
    now2 = now.strftime("%m/%d/%Y %H:%M:%S %f")
    stato = {"module": module, "state": state, "values": values, "time": now2}

    temp_state_variable_anon.lock_state.acquire()
    temp_state_variable_anon.state_dict[id_telegram] = stato
    temp_state_variable_anon.save_file_no_lock()
    temp_state_variable_anon.lock_state.release()

    return None


def cancel(update, context):
    try:
        temp_state_variable_anon.delete_state(update.message.chat.id)
    except:
        pass
    return None


def callback_method(update, context):
    query = update.callback_query
    query.edit_message_text(text="⬇️".format(query.data))
    next_main(id_telegram=query.from_user.id, update=update)
