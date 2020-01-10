import json
import re

import variable
from config import material_config
from functions import utils

try:
    materials_file = open("data/materials.json", encoding="utf-8")
    materials_dict = json.load(materials_file)
except Exception as e:
    materials_dict = {}


def post_materials2(update, description):
    message = update.message

    text2 = "Group: " + message.chat.title + "\n"

    id2 = message.chat.id
    if id2 < 0:
        id2 = -id2

    text2 += "#id" + str(id2) + "\n\n"
    text2 += "Description: " + description

    forward_success, message2 = utils.forward_message(material_config.channel_id, message.reply_to_message)
    if forward_success is not True:
        utils.send_in_private_or_in_group("C'è stato un problema con l'inoltro del file. Contatta gli "
                                          "amministratori di @PoliNetwork",
                                          message.chat.id, message.from_user)
        return

    variable.updater.bot.send_message(material_config.channel_id, text=text2,
                                      reply_to_message_id=message2.message_id)
    utils.send_in_private_or_in_group("File correttamente inoltrato in " + str(material_config.channel_id),
                                      message.chat.id, message.from_user)

    try:
        variable.updater.bot.delete_message(message.chat.id, message.message_id)
    except:
        pass


def material_handler(update, context):
    message = update.message

    if message.chat.type == "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in un gruppo del network",
                                          message.chat.id, message.from_user)
        return

    if message.reply_to_message is None:
        utils.send_in_private_or_in_group("Questo comando funziona solo se rispondi ad un messaggio (di tipo file), "
                                          "il quale messaggio sarà poi inviato in " + str(material_config.channel_id),
                                          message.chat.id, message.from_user)
        return

    if message.reply_to_message.document is not None:

        text = message.text

        description = " ".join(text.split(" ")[1:])

        if len(description) < 12:
            utils.send_in_private_or_in_group(
                "La descrizione che hai dato è troppo corta!",
                message.chat.id, message.from_user)
            return

        post_materials2(update, description)
        return
    else:
        utils.send_in_private_or_in_group("Questo comando funziona solo se rispondi ad un messaggio (di tipo file), "
                                          "il quale messaggio sarà poi inviato in " + str(material_config.channel_id),
                                          message.chat.id, message.from_user)


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
    message = update.message

    if message.chat.type != "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                          message.chat.id, message.from_user)
        return

    variable.updater.bot.send_message(update.message.chat.id,
                                      "Entra in un gruppo e rispondi con /material [DESCRIZIONE]\n"
                                      "Esempio: /material Lezione 1 - Termodinamica\n"
                                      "Il nome del gruppo sarà scritto in automatico.\n"
                                      "Il file contenente gli appunti sarà pubblicato sul canale @PoliMaterials\n"
                                      "\n"
                                      "Attenzione a cosa pubblicate, vi invitiamo a leggere le regole @PoliRules",
                                      parse_mode="HTML")
