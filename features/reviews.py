import json
import os
import random
from json import JSONDecodeError
import hashlib

import variable
from config import creators
from functions import utils

try:
    file = open("data/reviews.json", encoding="utf-8")
    groups_reviews = json.load(file)
except (JSONDecodeError, IOError):
    groups_reviews = {}

# /add_review <anno> <prof> <voto> <descrizione>


def add_review(update, context):
    message = update.message
    chat = message['chat']
    if chat['type'] == 'private':
        variable.updater.bot.send_message(message.chat.id, "Le recensioni non possono essere fatte in privato."
                                                           " Devi entrare nel gruppo del corso da recensire.")
        print('Received a private message.')
        return

    salt = open("salt/salt.txt", encoding="utf-8").read()
    text = message.text

    # Review's attributes + hash

    vote_valid = True
    vote = ""
    year = text.split(" ")[1]

    if not utils.is_valid(year):
        variable.updater.bot.deleteMessage(chat_id=update.message.chat_id,
                                           message_id=update.message.message_id)
        utils.send_in_private_or_in_group("La data deve essere in formato AAAA/AAAA"
                                          "Ti invitiamo a mandare nuovamente la recensione.",
                                          chat.id, message.from_user)
        return

    prof = text.split(" ")[2]
    prof = prof.upper()

    try:
        vote = text.split(" ")[3]
        if vote != "":
            vote = int(vote)
        else:
            vote_valid = False
    except:
        vote_valid = False

    if vote_valid and (vote < 0 or vote > 100):
        vote_valid = False

    if vote_valid is False:
        variable.updater.bot.deleteMessage(chat_id=update.message.chat_id,
                                           message_id=update.message.message_id)
        utils.send_in_private_or_in_group("Il voto dev'essere compreso tra 0 e 100", chat.id, message.from_user)
        return

    description = " ".join(text.split(" ")[4:])
    description_valid = utils.is_valid(description)

    if description_valid is False:
        variable.updater.bot.deleteMessage(chat_id=update.message.chat_id,
                                           message_id=update.message.message_id)
        utils.send_in_private_or_in_group("La recensione contiene parole non ammesse.\n"
                                          "Ti invitiamo a leggere le regole, @PoliRules",
                                          chat.id, message.from_user)
        return

    group_id = str(chat['id'])
    to_hash = str(message.from_user).join(salt).encode('utf-8')
    hash2 = hashlib.sha512(to_hash).hexdigest()
    author_id = str(hash2)

    '''
    So, the groups is made in the following way:
     
     GROUP_ID:
        ANNO:
            PROF:
                AUTHOR:
                VOTO:
                DESCRIZIONE:
                
                AUTHOR:
                VOTO:
                DESCRIZIONE:
                
                AUTHOR:
                VOTO:
                DESCRIZIONE:
        ANNO2:
            PROF:
                AUTHOR:
                VOTO:
                DESCRIZIONE:
                
                AUTHOR:
                VOTO:
                DESCRIZIONE:
                
                AUTHOR:
                VOTO:
                DESCRIZIONE:
     Let's assume group_id as the key of the dict. While the jsons are the reviews that are in that group.
     Pretty easy, isn't it?!
    DICT = "A" : "B"
    '''

    years_dict = {}
    if groups_reviews and groups_reviews.keys().__contains__(group_id):
        years_dict = groups_reviews.__getitem__(group_id)

    prof_dict = {}
    if years_dict and years_dict.__contains__(year):
        prof_dict = years_dict.__getitem__(year)

    prof_reviews_list = []
    if prof_dict and prof_dict.__contains__(prof):
        prof_reviews_list = prof_dict.__getitem__(prof)

    # Lets check if the author has already voted that group

    author_already_voted = False
    for review in prof_reviews_list:
        if review['author_id'] == author_id:
            author_already_voted = True
    if author_already_voted:
        variable.updater.bot.deleteMessage(chat_id=message.chat_id,
                                           message_id=message.message_id)
        utils.send_in_private_or_in_group("Hai già fatto una recensione!", chat.id, message.from_user)
        return

    # Create the json that will be appended to the list

    save = {
        "author_id": author_id,
        "vote": vote,
        "description": description
    }

    # Add the json built to the existing list of reviews

    prof_reviews_list.append(save)
    prof_dict.update({prof: prof_reviews_list})
    years_dict.update({year: prof_dict})
    groups_reviews.update({group_id: years_dict})

    # Save everything and delete the message sent by user
    with open("data/reviews.json", 'w', encoding="utf-8") as file_to_write:
        json.dump(groups_reviews, file_to_write)

    variable.updater.bot.deleteMessage(chat_id=update.message.chat_id,
                                       message_id=update.message.message_id)
    utils.send_in_private_or_in_group("Recensione ricevuta. Grazie!", chat.id, message.from_user)


def get_review_json(update, context):
    message = update.message
    chat = message.chat
    if chat.id in creators.owners:
        try:
            variable.updater.bot.send_document(chat_id=chat.id, document=open("data/reviews.json", 'rb'))
        except:
            pass


def help_handler(update, context):
    message = update.message

    if message.chat.type != "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                          message.chat.id, message.from_user)
        return

    update.message.reply_text("E' possibile recensire i corsi.\n"
                              "1. Entra nel gruppo del tuo corso.\n"
                              "2. Scrivi /review VOTO TESTO\n"
                              "Dove VOTO è un numero da 0 a 100 e TESTO è il testo vero e proprio della recensione\n"
                              "\nEsempio: /review 10 Corso pessimo! State alla larga!\n"
                              "\nLeggi le recensioni con il comando /get_reviews")


def get_reviews_html2(review_list, update):
    html1 = "<html><head><style>.carousel-control.left,.carousel-control.right  {background:none;width:25px;}" \
            ".carousel-control.left {left:-25px;}.carousel-control.right {right:-25px;}" \
            ".broun-block {    padding-bottom: 34px;}" \
            ".block-text {    background-color: #fff;    border-radius: 5px;    box-shadow: 0 3px 0 #2c2222;" \
            "    color: #626262;    font-size: 14px;    margin-top: 27px;    padding: 15px 18px;}" \
            ".block-text a { color: #7d4702;    font-size: 25px;    font-weight: bold;    line-height: 21px;" \
            "    text-decoration: none;    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);}" \
            ".mark {    padding: 12px 0;background:none;}.block-text p {    color: #585858;  " \
            "  font-family: Georgia;    font-style: italic;    line-height: 20px;}" \
            ".sprite-i-triangle {    background-position: 0 -1298px;    height: 44px;    width: 50px;}" \
            ".block-text ins {    bottom: -44px;    left: 50%;    margin-left: -60px;}" \
            ".block {    display: block;}.zmin {    z-index: 1;}" \
            ".ab {    position: absolute;}" \
            ".person-text {    padding: 10px 0 0;    text-align: center;    z-index: 2;}" \
            ".person-text a {    color: #ffcc00;    display: block;    font-size: 14px;    margin-top: 3px;" \
            "    text-decoration: underline;}" \
            ".person-text i {    color: #fff;    font-family: Georgia;    font-size: 13px;}" \
            ".rel {    position: relative;}" \
            "</style></head>" \
            "<body><div class='container'>	<div class='row'>		<h2>"

    html1 += "Recensioni: " + utils.escape(update.message.chat.title)

    html1 += "</div></div><div class='carousel-reviews broun-block'>    <div class='container'>" \
             "<div class='row'><div id='carousel-reviews' class='carousel slide' data-ride='carousel'>" \
             "<div class='item active'>"

    html3 = "				</div>            </div>        </div>    </div></div></body></html>"

    html2 = ""

    sum_votes = 0

    for review in review_list:
        vote = int(review['vote'])
        sum_votes += vote
        html2 += "<div class='col-md-4 col-sm-6'><div class='block-text rel zmin'><a title='' href='#'>"
        html2 += str(vote) + "/100 ⭐"
        html2 += "</a><p>"
        html2 += utils.escape(review['description'])
        html2 += "</p><ins class='ab zmin sprite sprite-i-triangle block'></ins>	</div>"
        html2 += "</div>	</div>"

    avg = sum_votes / len(review_list)
    return html1 + "</h2>&nbsp;Media: " + str(avg) + "/100" + html2 + html3


def get_reviews_html(update, context):
    if update.message.chat.type == "private":
        variable.updater.bot.send_message(update.message.chat.id, "Questo comando funziona solo in un gruppo!")
        return

    variable.updater.bot.delete_message(update.message.chat.id, update.message.message_id)

    group_id = update.message.chat['id']

    reviews_list = []

    if groups_reviews.keys().__contains__(str(group_id)):
        reviews_list = groups_reviews.get(str(group_id))

    if len(reviews_list) < 1:
        utils.send_in_private_or_in_group("Spiacente, non c'è ancora nessuna recensione!",
                                          update.message.chat.id, update.message.from_user)
        return

    html = get_reviews_html2(reviews_list, update)

    n = random.randint(1, 9999999)
    filename = 'data/review' + str(n) + "_" + str(abs(int(update.message.chat.id))) + '.html'

    with open(filename, 'w', encoding="utf-8") as file_to_write:
        file_to_write.write(html)

    html = open(filename, 'rb')
    # then send them
    utils.send_file_in_private_or_warning_in_group(update.message.from_user, html,
                                                   update.message.chat.id, update.message.chat.title)
    html.close()
    try:
        os.remove(filename)
    except Exception as e:
        print(e)
