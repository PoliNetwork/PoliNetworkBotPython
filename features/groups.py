import datetime
import json

import variable
from config import creators


def find(id_to_find):
    # lock not needed here
    for group in variable.groups_list:
        if group['Chat']['id'] == id_to_find:
            return True, group
    return False, None


def write_group_file(chat_id, chat_type, title, invite_link, last_update, we_are_admin):
    group = {
        "Chat": {
            "id": chat_id,
            "type": chat_type,
            "title": title,
            "invite_link": invite_link
        },
        "LastUpdateInviteLinkTime": last_update,
        "we_are_admin": we_are_admin
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

    group_already_present, group_found = find(chat['id'])

    if group_already_present is False:

        admins = variable.updater.bot.get_chat_administrators(chat.id)
        if not creator_is_present(admins):
            write_group_file(chat['id'], chat['type'], chat['title'], None, None, False)
            return True
        else:
            (invite_link, last_update) = get_link_and_last_update(message)

            if invite_link is not None and invite_link != "":
                write_group_file(chat['id'], chat['type'], chat['title'], invite_link, last_update, True)

                # check if we have to send invite link in chat
                if message.new_chat_members is not None and len(message.new_chat_members) > 0 \
                        and creators.me in message.new_chat_members:
                    variable.updater.bot.send_message(chat.id, "Invite link: " + invite_link)

        return None  # todo: get admin list, update json and return true or false accordingly

    try:
        if group_found["we_are_admin"] is False:
            return True
        elif group_found["we_are_admin"] is True:
            return False
    except:
        pass

    return None  # todo: get admin list, update json and return true or false accordingly


def get_group_json(update, context):
    message = update.message
    chat = message.chat
    if chat.id in creators.owners:
        variable.updater.bot.send_document(chat_id=message.chat.id, document=open("data/groups.json", 'rb'))
