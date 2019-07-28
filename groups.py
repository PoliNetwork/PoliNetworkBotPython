import json
import main


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
        file.write(json.dumps(groups_dict))


def get_link_and_last_update(message):
    chat = main.updater.bot.get_chat(message.chat.id)
    link = chat.invite_link
    if link is None or link == "":
        link = main.updater.bot.export_chat_invite_link(message['chat']['id'])

    last_update = ""
    return link, last_update


def try_add_group(message):
    chat = message['chat']
    if chat['type'] == 'private':
        print('Received a private message.')
        return

    already_present = find(chat['id'])
    if already_present is False:
        id = chat['id']
        type = chat['type']
        title = chat['title']
        (invite_link, last_update) = get_link_and_last_update(message)
        write_group_file(id, type, title, invite_link, last_update)


try:
    group_read = open("data/groups.json", encoding="utf-8")
    groups_list = json.load(group_read)['Gruppi']
except:
    groups_list = []
