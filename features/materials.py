import json

import variable
from features import groups
from functions import utils

try:
    materials_file = open("data/materials.json", encoding="utf-8")
    materials_dict = json.load(materials_file)
except Exception as e:
    materials_dict = {}


def material_handler(update, context):
    message = update.message
    chat = message.chat
    group_id = str(chat.id)

    if chat.type == "private":
        return

    link_material = materials_dict.get(group_id)

    if link_material is None or link_material == "":
        utils.send_in_private_or_in_group("Materiale non disponibile. Contatta gli amministratori.",
                                          group_id=chat.id,
                                          user=message.from_user.id)
        return

    message_to_send = "Materiale per il gruppo " + chat['title'] + "\n\n"
    message_to_send += "\n".join(link_material)
    utils.send_in_private_or_in_group(message_to_send,
                                      group_id=group_id,
                                      user=message.from_user)

    variable.updater.bot.delete_message(group_id, message.message_id)


def add_material_handler(update, context):
    message = update.message
    chat = message.chat

    if chat.type == "private":
        return

    group_id = str(chat.id)
    link = message.text.split(" ")[1]

    materials_in_group = []
    if not materials_dict.get(group_id) is None:
        materials_in_group = materials_dict.get(group_id)

    materials_in_group.append(link)

    materials_dict.update({group_id: materials_in_group})

    with open("data/materials.json", 'w', encoding="utf-8") as file:
        json.dump(materials_dict, file)

    utils.send_in_private_or_in_group("Materiale aggiunto",
                                      group_id=group_id,
                                      user=message.from_user)
    variable.updater.bot.delete_message(group_id, message.message_id)
