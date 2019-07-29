import json
from json import JSONDecodeError
import hashlib

import bot

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

    # Review's attributes + hash

    vote = text.split(" ")[1]
    description = " ".join(text.split(" ")[2:])
    group_id = str(chat['id'])
    to_hash = str(chat['id']).join(salt).encode('utf-8')
    hash2 = hashlib.sha512(to_hash).hexdigest()
    author_id = str(hash2)

    '''
    So, the reviews_dict is made in the following way:
    "group_id : [{
        author: ""
        vote: ""
        description: ""
     }], [...], [...]
     Let's assume group_id as the key of the dict. While the jsons are the reviews that are in that group.
     Pretty easy, isnt it?!
    '''

    group_reviews = []
    if reviews_dict and reviews_dict.keys().__contains__(group_id):
        group_reviews = reviews_dict.get(group_id)

    # Lets check if the author has already voted that group

    author_already_voted = False
    for group in group_reviews:
        if group['author_id'] == author_id:
            author_already_voted = True
    if author_already_voted:
        bot.updater.bot.deleteMessage(chat_id=update.message.chat_id,
                                  message_id=update.message.message_id)
        return

    # Create the json that will be appended to the list

    save = {
        "author_id": author_id,
        "vote": vote,
        "description": description
    }

    # Add the json built to the existing list of reviews

    group_reviews.append(save)

    # Replace the original group_reviews with the new one and save everything on the file

    reviews_dict.update({group_id: group_reviews})

    # Save everything and delete the message sent by user
    with open("data/reviews.json", 'w', encoding="utf-8") as file_to_write:
        json.dump(reviews_dict, file_to_write)

    bot.updater.bot.deleteMessage(chat_id=update.message.chat_id,
                                  message_id=update.message.message_id)


def get_review_json(update, context):
    message = update.message
    chat = message.chat
    if chat.id == 5651789:  # id of @ArmeF97
        bot.updater.bot.send_document(chat_id=chat.id, document=open("data/reviews.json", 'rb'))


def help_handler(update, context):
    # todo
    update.message.reply_text("Spiegazione del sistema delle recensioni.")
