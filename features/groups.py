import json

import variable
from config import creators
from functions import utils
from sub_bots.anon import config_anon


def find(id_to_find):
    # lock not needed here
    for group in variable.groups_list:
        if group['Chat']['id'] == id_to_find:
            return True, group
    return False, None


def write_group_file(chat_id, chat_type, title, invite_link, last_update, we_are_admin, keep_link):
    group = {
        "Chat": {
            "id": chat_id,
            "type": chat_type,
            "title": title,
            "invite_link": invite_link
        },
        "LastUpdateInviteLinkTime": last_update,
        "we_are_admin": we_are_admin,
        "keep_link": keep_link
    }

    variable.lock_group_list.acquire()

    variable.groups_list.append(group)

    groups_dict = {"Gruppi": variable.groups_list}
    with open("data/groups.json", 'w', encoding="utf-8") as file:
        json.dump(groups_dict, file)

    variable.lock_group_list.release()


def isNotBlank(myString):
    if myString and myString.strip():
        # myString is not None AND myString is not empty or blank
        return True
    # myString is None OR myString is empty or blank
    return False


def creator_is_present(admins):
    for admin in admins:
        if isNotBlank(admin.user.username):
            a = str(admin.user.username).lower()
            if a in creators.creators and admin.status == "creator":
                return True

    return False


def subcreator_is_present(admins):
    for admin in admins:
        if isNotBlank(admin.user.username):
            a = str(admin.user.username).lower()
            if a in creators.subcreators and admin.status == "creator":
                return True

    return False


def try_add_group(message):
    chat = None

    try:
        chat = message['chat']
    except:
        chat = None

    if chat is None:
        return None, 10

    if chat['type'] == 'private':
        print('Received a private message.')
        return None, 1

    if chat['id'] == config_anon.group_id:
        print("k")
        return None, 8

    group_already_present, group_found = find(chat['id'])

    if group_already_present is False:

        admins = None
        try:
            admins = variable.updater.bot.get_chat_administrators(chat.id)
        except:
            admins = None

        if admins is None:
            return None, 12

        if not creator_is_present(admins):

            if subcreator_is_present(admins):
                write_group_file(chat['id'], chat['type'], chat['title'], None, None, True, False)
                return None, 11
            else:
                write_group_file(chat['id'], chat['type'], chat['title'], None, None, False, False)
                return True, 2
        else:
            (invite_link, last_update) = utils.get_link_and_last_update(message.chat.id)

            if invite_link is not None and invite_link != "":
                write_group_file(chat['id'], chat['type'], chat['title'], invite_link, last_update, True, True)

                # check if we have to send invite link in chat
                if message.new_chat_members is not None and len(message.new_chat_members) > 0 \
                        and creators.me in message.new_chat_members:
                    variable.updater.bot.send_message(chat.id, "Invite link: " + invite_link)

        return None, 3  # todo: get admin list, update json and return true or false accordingly

    try:
        if group_found["we_are_admin"] is False:
            admins = variable.updater.bot.get_chat_administrators(chat.id)

            if subcreator_is_present(admins):
                write_group_file(chat['id'], chat['type'], chat['title'], None, None, True, False)
                return None, 9

            if not creator_is_present(admins) and not subcreator_is_present(admins):
                write_group_file(chat['id'], chat['type'], chat['title'], None, None, False, False)
                return True, 4
            else:
                group_found["we_are_admin"] = True
                return False, 5
        elif group_found["we_are_admin"] is True:
            return False, 6
    except:
        pass

    return None, 7  # todo: get admin list, update json and return true or false accordingly


def get_group_json(update, context):
    message = update.message
    chat = message.chat
    if chat.id in creators.owners:
        try:
            variable.updater.bot.send_document(chat_id=message.chat.id, document=open("data/groups.json", 'rb'))
        except:
            try:
                variable.updater.bot.send_message(chat.id, "Eccezione get_group_json")
            except:
                pass
            pass
