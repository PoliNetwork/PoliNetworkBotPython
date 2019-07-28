import json


def find(id):
    for group in groups_list:
        if group['Chat']['id'] == id:
            return True
    return False


def write_group_file(id, type, title, invite_link, last_update):
    group = {
        "Chat":{
            "id": id,
            "type": type,
            "title": title,
            "invite_link": invite_link
        },
        "LastUpdateInviteLinkTime": last_update
    }
    groups_list.append(group)
    with open("data/groups.json",'w',encoding="utf-8") as file:
        file.write(json.dumps(groups_list))


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
        invite_link = "" #TODO: Add invite link and last_update
        last_update = ""
        write_group_file(id, type, title, invite_link, last_update)


try:
    group_read = open("data/groups.json",encoding="utf-8")
    groups_list = json.load(group_read)['Gruppi']
except:
    groups_list = []

