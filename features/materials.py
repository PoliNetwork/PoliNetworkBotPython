from features import groups
from functions import utils


def material_handler(update, context):
    message = update.message
    chat = message.chat

    if chat.type == "private":
        return

    found, group_found = groups.find(chat['id'])
    if found is False:
        utils.send_in_private_or_in_group("Gruppo non trovato.",
                                          group_id=chat.id,
                                          user=message.from_user.id)
        return

    link_material = group_found['material']

    if link_material is None or link_material == "":
        utils.send_in_private_or_in_group("Materiale non disponibile. Contatta gli amministratori.",
                                          group_id=chat.id,
                                          user=message.from_user.id)
        return

    # todo send link_material


def add_material_handler(update, context):
    # todo: formato testo: /addMateriale LINK

    message = update.message
    chat = message.chat

    if chat.type == "private":
        return

    found, group_found = groups.find(chat['id'])
    if found is False:
        utils.send_in_private_or_in_group("Gruppo non trovato.",
                                          group_id=chat.id,
                                          user=message.from_user.id)
        return

    link_material = group_found['material']

    if link_material is None or link_material == "":
        # todo aggiungere il materiale
        return

    utils.send_in_private_or_in_group("Materiale già presente.",
                                      group_id=chat.id,
                                      user=message.from_user.id)
