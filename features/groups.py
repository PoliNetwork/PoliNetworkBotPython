import datetime
import json

import variable
from config import creators


def find(id_to_find):
    # lock not needed here
    for group in variable.groups_list:
        if group['Chat']['id'] == id_to_find:
            return True
    return False


def write_group_file(chat_id, chat_type, title, invite_link, last_update):
    group = {
        "Chat": {
            "id": chat_id,
            "type": chat_type,
            "title": title,
            "invite_link": invite_link
        },
        "LastUpdateInviteLinkTime": last_update
    }

    variable.lock_group_list.acquire()

    variable.groups_list.append(group)

    groups_dict = {"Gruppi": variable.groups_list}
    with open("data/groups.json", 'w', encoding="utf-8") as file:
        json.dump(groups_dict, file)

    variable.lock_group_list.release()


def get_link_and_last_update(message):
    chat = variable.updater.bot.get_chat(message.chat.id)
    link = chat.invite_link
    if link is None or link == "":
        link = variable.updater.bot.export_chat_invite_link(message.chat.id)

    if link is None or link == "":
        return None, None

    last_update = str(datetime.datetime.now())
    return link, last_update


def creator_is_present(admins):
    for admin in admins:
        if admin.user.username in creators.creators:
            # todo: re-enable this check
            # if admin.status == "creator":
            return True
    return False


def try_add_group(message):
    chat = message['chat']
    if chat['type'] == 'private':
        print('Received a private message.')
        return

    admins = variable.updater.bot.get_chat_administrators(chat.id)
    if not creator_is_present(admins):
        return

    group_already_present = find(chat['id'])
    if group_already_present is False:
        (invite_link, last_update) = get_link_and_last_update(message)
        write_group_file(chat['id'], chat['type'], chat['title'], invite_link, last_update)


def get_group_json(update, context):
    message = update.message
    chat = message.chat
    if chat.id in creators.owners:
        variable.updater.bot.send_document(chat_id=message.chat.id, document=open("data/groups.json", 'rb'))
