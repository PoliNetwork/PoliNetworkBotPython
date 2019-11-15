# Con questo modulo, si gestisce la possibilità di usare uno stato dell'utente.
# Esempio: io do un comando, il bot mi chiede "scrivi questo", io lo scrivo, poi il bot mi chiede
# "scrivi quest'altro". Il bot per seguirti ha bisogno di sapere, nella macchina a stati finiti,
# in quale punto ti trovi. Dopo 5 minuti lo stato sarà cancellato da un thread dedicato.
# Ogni qualvolta che un utente aggiorna il suo stato, i 5 minuti si resettano.
# Allo scadere dei 5 minuti di un utente, gli viene inviato il messaggio che la sua sessione è scaduta.
# Ovviamente, se l'utente completa la macchina a stati con successo arrivando alla fine,
# la sua sessione sarà rimossa senza dare nessun avviso.

# Gli stati sono un json che ha come chiave l'id telegram della persona, e come valore al suo interno 2 valori
# "module", "state", "values"
# dove "module" è una stringa, è il nome della macchina a stati finiti che l'utente sta attraversando
# dove "state" è il punto della macchina a stati finiti in cui l'utente si trova
# dove "values" è un array di stringhe, delle variabili opzionali utili per passarsi valori man mano che si avanza negli stati

# {123:{"module":"abc", "state": "1a", "values":["v1", "v2"]}}
# qui sopra un esempio, 123 è l'id telegram, abc il nome del modulo, 1a lo stato, v1 e v2 i valori dell'array dei valori.

# Per gestire il tutto serve un thread di eliminazione, un json scritto su file, e un lock che si usa scrittura.
# Nota bene: il lock potrebbe anche essere messo in una funzione di lettura, se nel suo percorso di esecuzione c'è anche solo la possibilità che scriva.

def get_state(id_telegram):
    # todo, ritorna lo stato di una persona leggendolo dal json
    return None


def next_abc(id_telegram, stato):
    # esempio: se il modulo è abc, viene gestito dalla next abc
    # occhio: prima di passare ad un nuovo stato aggiornando il valore di "state", bisogna controllare che sia ancora nel json, perché magari il tempo è scaduto
    return None


def next_main(id_telegram):
    # noinspection PyNoneFunctionAssignment
    stato = get_state(id_telegram)
    if stato["module"] == "abc":  # esempio
        return next_abc(id_telegram, stato)
    else:
        return None
