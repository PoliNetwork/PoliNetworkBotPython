import json
from json import JSONDecodeError

import main

try:
    file = open("data/reviews.json", encoding="utf-8")
    reviews_dict = json.load(file)
except (JSONDecodeError, IOError):
    reviews_dict = {}


def add_review(update, context):
    message = update.message
    chat = message['chat']
    if chat['type'] == 'private':
        print('Received a private message.')
        return

    salt = open("salt.txt", encoding="utf-8").read()

    text = message.text
    vote = text.split(" ")[1]
    description = " ".join(text.split(" ")[2:])
    group_id = str(chat['id'])
    author_id = hash(str(chat['id']).join(salt))

    group_reviews = []
    if reviews_dict and reviews_dict.keys().__contains__(group_id):
        group_reviews = reviews_dict.get(group_id)

    # Create the json
    save = {
        "author_id": author_id,
        "vote": vote,
        "description": description
    }
    # Add to existing list of reviews the json built
    group_reviews.append(save)
    # Create a dict made up by group id and reviews linked to that group
    dict = {group_id: group_reviews}
    reviews_dict.update(dict)
    # Save everything and delete the message sent by user
    with open("data/reviews.json", 'w', encoding="utf-8") as file:
        json.dump(reviews_dict, file)

    main.updater.bot.deleteMessage(chat_id=update.message.chat_id,
                                   message_id=update.message.message_id)
