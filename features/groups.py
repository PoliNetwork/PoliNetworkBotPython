import datetime
import json
from json import JSONDecodeError

import bot
from config import creators


def find(id):
    for group in groups_list:
        if group['Chat']['id'] == id:
            return True
    return False


def write_group_file(id, type, title, invite_link, last_update):
    group = {
        "Chat": {
            "id": id,
            "type": type,
            "title": title,
            "invite_link": invite_link
        },
        "LastUpdateInviteLinkTime": last_update
    }
    groups_list.append(group)

    groups_dict = {"Gruppi": groups_list}
    with open("data/groups.json", 'w', encoding="utf-8") as file:
        json.dump(groups_dict, file)


def get_link_and_last_update(message):
    chat = bot.updater.bot.get_chat(message.chat.id)
    link = chat.invite_link
    if link is None or link == "":
        link = bot.updater.bot.export_chat_invite_link(message['chat']['id'])
    last_update = str(datetime.datetime.now())
    return link, last_update


def creator_is_present(admins):
    for admin in admins:
        if admin.user.username in creators.creators:
            # if admin.status == "creator":
            return True
    return False


def try_add_group(message):
    chat = message['chat']
    if chat['type'] == 'private':
        print('Received a private message.')
        return

    admins = bot.updater.bot.get_chat_administrators(chat.id)
    if not creator_is_present(admins):
        return

    group_already_present = find(chat['id'])
    if group_already_present is False:
        (invite_link, last_update) = get_link_and_last_update(message)
        write_group_file(chat['id'], chat['type'], chat['title'], invite_link, last_update)


try:
    group_read = open("data/groups.json", encoding="utf-8")
    groups_list = json.load(group_read)['Gruppi']
except (JSONDecodeError, IOError):
    groups_list = []


def get_group_json(update, context):
    message = update.message
    chat = message.chat
    if chat.id == 5651789:  # id of @ArmeF97
        bot.updater.bot.send_document(chat_id=message.chat.id, document=open("data/groups.json", 'rb'))
