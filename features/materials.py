from features import groups


def material_handler(update, context):
    message = update.message
    chat = message.chat
    found, group_found = groups.find(chat['id'])
    if found is False:
        # todo inviare messaggio "Gruppo non trovato"
        return

    link_material = group_found['material']

    if link_material is None or link_material == "":
        # todo inviare messaggio "Materiale non disponibile, contatta gli amministratori"
        return

    # todo send link_material
