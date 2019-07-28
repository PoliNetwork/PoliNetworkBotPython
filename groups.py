import json


def find(id):
    for group in groups_list:
        if group['id'] == id:
            return True

    return False


def write_group_file():
    # todo: write group
    json_text = json.dumps(groups_list)
    with open("data/groups.json", 'w') as the_file:
        the_file.write(json_text)


def try_add_group(message):
    chat = message['chat']
    if chat['type'] == 'private':
        print('Received a private message.')
        return

    # todo: add group to json
    print(chat)
    already_present = find(chat['id'])
    if already_present is False:
        group = {'id': chat['id']}
        groups_list.append(group)
        write_group_file()


try:
    groups_list = open("data/groups.json").read().json()
except:
    groups_list = []
