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

import variable
from features import aule, reviews
from functions.temp_state import temp_state_variable


def get_state(id_telegram):
    for ass in temp_state_variable.state_dict.keys():
        if ass == id_telegram:
            return temp_state_variable.state_dict.get(ass)
    return None


def overwrite_state(id_telegram, stato):
    temp_state_variable.lock_state.acquire()

    if temp_state_variable.state_dict[id_telegram] is None:
        # todo: occhio! bisogna controllare che ci sia qualcosa nel json, perché se è vuoto, è stato eliminato
        temp_state_variable.lock_state.release()
        return None

    temp_state_variable.state_dict[id_telegram] = stato
    temp_state_variable.save_file_no_lock()
    temp_state_variable.lock_state.release()
    return None


def delete_state(id_telegram):
    temp_state_variable.lock_state.acquire()
    del temp_state_variable.state_dict[id_telegram]
    temp_state_variable.save_file_no_lock()
    temp_state_variable.lock_state.release()
    return None


def next_a1(update, id_telegram, stato):
    if stato["state"] == "0":
        variable.updater.bot.send_message(chat_id=update.message.chat.id,
                                          text="Scrivi il codice dell'aula (esempio: N.0.1)")
        stato["state"] = "1"
        overwrite_state(id_telegram, stato)
        return None
    elif stato["state"] == "1":
        datetime_object = datetime.datetime.now()
        message = update.message
        text = message.text
        aula_da_trovare = text
        result = aule.f5(datetime_object.day, datetime_object.month, datetime_object.year, aula_da_trovare)
        n = random.randint(1, 9999999)
        filename = 'data/aula' + str(n) + "_" + str(abs(int(update.message.chat.id))) + '.html'
        reviews.send_file(update, result, filename, aula_da_trovare)

        delete_state(id_telegram)

        return None

    return None


def next_main(id_telegram, update):
    # noinspection PyNoneFunctionAssignment
    stato = get_state(id_telegram)
    if stato is None:
        return None

    if stato["module"] == "a1":
        return next_a1(update, id_telegram, stato)

    return None


def create_state(module, state, id_telegram):

    stato = {"module": module, "state": state, "values": [], "time": ""}

    temp_state_variable.lock_state.acquire()
    temp_state_variable.state_dict[id_telegram] = stato
    temp_state_variable.save_file_no_lock()
    temp_state_variable.lock_state.release()

    return None


def cancel(update, context):
    delete_state(update.message.chat.id)
    return None
