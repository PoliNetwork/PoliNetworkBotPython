import json
import re

import variable
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

    link_material = []
    if materials_dict.keys().__contains__(group_id):
        link_material = materials_dict.get(group_id)

    if not link_material:
        utils.send_in_private_or_in_group("Materiale non disponibile. Contatta gli amministratori.",
                                          group_id=chat.id,
                                          user=message.from_user)
        return

    message_to_send = "Materiale per il gruppo " + chat['title'] + "\n\n"
    count = 1
    for i in link_material:
        message_to_send += str(count) + ".  " + i["link"] + "\n" + i["comment"] + "\n\n"
        count = count + 1

    utils.send_in_private_or_in_group(message_to_send,
                                      group_id=group_id,
                                      user=message.from_user)

    variable.updater.bot.delete_message(group_id, message.message_id)


def eval_link(link):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(regex, link) is None:
        return False
    return True


def find_material(materials_in_group, link):
    for i in materials_in_group:
        if i["link"] == link:
            return True, i

    return False, None


def add_remove_material(update, context):
    message = update.message
    chat = message.chat

    if chat.type == "private":
        return

    sender = message.from_user.id
    admins = variable.updater.bot.get_chat_administrators(message['chat']['id'])
    group_id = str(chat.id)

    admins = {admin["user"]['id']
              for admin in admins}

    if not (sender in admins):
        utils.send_in_private_or_in_group("Comando vietato. Non sei admin.",
                                          group_id, message.from_user)
        variable.updater.bot.delete_message(group_id, message.message_id)
        return

    if len(message.text.split(" ")) == 1:
        utils.send_in_private_or_in_group("Il comando da usare deve contenere un link!",
                                          group_id, message.from_user)
        variable.updater.bot.delete_message(group_id, message.message_id)
        return

    command = message.text.split(" ")[0]
    link = message.text.split(" ")[1]

    if not eval_link(link):
        utils.send_in_private_or_in_group("Link non valido",
                                          group_id, message.from_user)
        variable.updater.bot.delete_message(group_id, message.message_id)
        return

    materials_in_group = []
    if not materials_dict.get(group_id) is None:
        materials_in_group = materials_dict.get(group_id)

    something_done = False
    variable.lock_material_list.acquire()

    if "remove_material" in command:
        (found, i) = find_material(materials_in_group, link)
        if found is True:
            materials_in_group.remove(i)
            utils.send_in_private_or_in_group("Materiale rimosso",
                                              group_id=group_id,
                                              user=message.from_user)
            something_done = True
        else:
            utils.send_in_private_or_in_group("Materiale non trovato",
                                              group_id=group_id,
                                              user=message.from_user)
    else:

        comment = ""
        try:
            comment = " ".join(message.text.split(" ")[2:])
        except:
            pass

        to_insert = {"link": link, "comment": comment}
        materials_in_group.append(to_insert)
        materials_dict.update({group_id: materials_in_group})
        utils.send_in_private_or_in_group("Materiale aggiunto",
                                          group_id=group_id,
                                          user=message.from_user)
        something_done = True

    if something_done is True:
        with open("data/materials.json", 'w', encoding="utf-8") as file:
            json.dump(materials_dict, file)

    variable.lock_material_list.release()

    variable.updater.bot.delete_message(group_id, message.message_id)


def help_handler(update, context):
    # todo
    update.message.reply_text("Todo")