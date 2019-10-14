def errore_no_associazione(update):
    # todo inviare "Non fai parte di nessuna associazione, scrivi agli admin di @PoliNetwork"
    pass


def get_associazione(update):
    # todo: dato l'id del mittente del messaggio, ritornare l'associazione di cui fa parte, None se non fa parte di nessuna
    return None


def get_message_associazione(associazione):
    # todo: tirare fuori il messaggio a partire dall'associazione trovata qui sopra, tornare None se non c'è nessun messaggio
    return None


def assoc_read(update, context):
    associazione = get_associazione(update)

    if associazione is not None:
        errore_no_associazione(update)

        return None

    read_message = get_message_associazione(associazione)
    if read_message is None:
        # todo: inviare "nessun messaggio in coda!"
        pass
    else:
        # todo: inviare il messaggio con forward normale
        pass

    return None


def check_message_associazioni(update):
    # todo: controllare che il messaggio rispetti i requisiti, inviare all'utente eventuali errori, e poi tornare True se il messaggio è valido, False altrimenti
    return False


def assoc_write(update, context):
    associazione = get_associazione(update)

    if associazione is not None:
        errore_no_associazione(update)
        return None

    messaggio_valido = check_message_associazioni(update)
    if messaggio_valido:
        # todo: aggiungere il messaggio alla coda.
        #  inviare all'utente che il messaggio è stato messo correttamente in coda
        pass

    return None


def assoc_delete(update, context):
    associazione = get_associazione(update)

    if associazione is not None:
        errore_no_associazione(update)
        return None

    read_message = get_message_associazione(associazione)
    if read_message is None:
        # todo: inviare "nessun messaggio in coda!"
        pass
    else:
        # todo: rimuovere il messaggio dalla coda e informare l'utente che è stato rimosso con successo.
        pass
    return None
