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


def add_review_private(update):
    variable.updater.bot.send_message(update.message.chat.id, "Le recensioni non possono essere fatte in privato."
                                                              " Devi entrare nel gruppo del corso da recensire.")
    print('Received a private message.')


# /add_review <anno> <prof> <voto> <descrizione>
def add_review(update, context):
    message = update.message
    chat = message['chat']
    if chat['type'] == 'private':
        add_review_private(update)
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

    if not prof.isalpha():
        variable.updater.bot.deleteMessage(chat_id=update.message.chat_id,
                                           message_id=update.message.message_id)
        utils.send_in_private_or_in_group("Nome del professore non accettabile."
                                          "Ti invitiamo a mandare nuovamente la recensione.",
                                          chat.id, message.from_user)
        return

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
        for year in review_list.get(review):
            for prof in review_list.get(review)[year]:
                for single_review in review_list.get(review)[year][prof]:
                    vote = int(single_review['vote'])
                    sum_votes += vote
                    html2 += "<div class='col-md-4 col-sm-6'><div class='block-text rel zmin'><a title='' href='#'>"
                    html2 += str(vote) + "/100 ⭐"
                    html2 += "</a><p>"
                    html2 += utils.escape(single_review['description'])
                    html2 += "</p><ins class='ab zmin sprite sprite-i-triangle block'></ins>	</div>"
                    html2 += "</div>	</div>"
    avg = sum_votes / len(review_list)
    return html1 + "</h2>&nbsp;Media: " + str(avg) + "/100" + html2 + html3


def remove_spaces(text):
    while True:
        if text.startswith(" "):
            text = text[1:]
        else:
            break

    return text


def get_reviews_private_from_text(text, update):
    text = text[13:]  # remove "/get_reviews"

    if len(text) < 2:
        variable.updater.bot.send_message(update.message.chat.id,
                                          "Devi aggiungere qualche filtro in chat privata! "
                                          "Scopri di più con /help_review")
        return None

    if "&&" in text:
        data = text.split("&&")
    else:
        data = [text]

    prof_b = False
    year_b = False
    group_b = False

    prof_v = None
    year_v = None
    group_v = None

    for data2 in data:
        data2 = remove_spaces(data2)
        data3 = data2.split(" ")
        if data3[0] == "teacher":
            prof_b = True
            prof_v = remove_last_char_space(" ".join(data3[1:]))
        elif data3[0] == "year":
            year_b = True
            year_v = data3[1]
        elif data3[0] == "group":
            group_b = True
            group_v = remove_last_char_space(" ".join(data3[1:]))

    # todo: migliorare group_v e prof_v di modo che le funzioni qui sotto funzionino

    if prof_b and year_b and group_b:
        return get_reviews_by_gpy(group_v, prof_v, year_v)
    elif prof_b and year_b:
        return get_reviews_by_py(prof_v, year_v)
    elif group_b and year_b:
        return get_reviews_by_gy(group_v, year_v)
    elif group_b and prof_b:
        return get_reviews_by_group_and_prof(group_v, prof_v)
    elif group_b:
        return get_reviews_by_group_name(group_v)
    elif prof_b:
        return get_reviews_by_prof(prof_v)
    elif year_b:
        variable.updater.bot.send_message(update.message.chat.id, "Non è possibile indicare solo l'anno!")
        return None

    variable.updater.bot.send_message(update.message.chat.id, "Errore sconosciuto nella richiesta delle recensioni! "
                                                              "Contattare gli amministratori di @PoliNetwork!")
    return None


def get_reviews_html_private(update):
    # variable.updater.bot.send_message(update.message.chat.id, "Questo comando funziona solo in un gruppo!")
    text = update.message.text

    reviews_list = []

    try:
        reviews_list = get_reviews_private_from_text(text, update)
    except:
        pass

    send_html_reviews(reviews_list, update)


def send_html_reviews(reviews_list, update):
    if reviews_list is None:
        return

    if len(reviews_list) < 1:
        utils.send_in_private_or_in_group("Spiacente, non c'è ancora nessuna recensione!",
                                          update.message.chat.id, update.message.from_user)
        return

    html = get_reviews_html2(reviews_list, update)
    # ASD

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
        utils.notify_owners(e)


def get_reviews_html(update, context):
    if update.message.chat.type == "private":
        get_reviews_html_private(update)
        return

    variable.updater.bot.delete_message(update.message.chat.id, update.message.message_id)

    group_id = update.message.chat['id']

    reviews_list = []

    if groups_reviews.keys().__contains__(str(group_id)):
        reviews_list = groups_reviews.get(str(group_id))

    send_html_reviews(reviews_list, update)


def get_group_id_by_name(groupz):
    groups = variable.groups_list
    group_id = -1
    for group in groups:
        if group['Chat']['title'] == groupz:
            group_id = group['Chat']['id']
    return group_id


# by prof


def get_reviews_by_prof(prof):
    clone = {}
    for group in groups_reviews:
        for date in groups_reviews.get(group):
            for proff in groups_reviews.get(group).get(date):
                if proff == prof:
                    prof_j = {prof: groups_reviews.get(group).get(date).get(prof)}
                    new_date = {date: prof_j}
                    clone.update({group: new_date})
    return clone


# by group name


def get_reviews_by_group_name(groupz):
    group_id = get_group_id_by_name(groupz)
    clone = {}
    for group in groups_reviews:
        if group == str(group_id):
            clone.update({group_id: groups_reviews.get(group)})
    return clone


# by group name and prof


def get_reviews_by_group_and_prof(group, prof):
    group_id = get_group_id_by_name(group)
    clone = get_reviews_by_prof(prof)
    for groupx in get_reviews_by_prof(prof):
        if str(groupx) != str(group_id):
            clone.pop(groupx)
    return clone


# by group name, prof and year


def get_reviews_by_gpy(group, prof, year):
    reviews_by_pg = get_reviews_by_group_and_prof(group, prof)
    json_dict = {}
    for group in reviews_by_pg:
        for date in reviews_by_pg.get(group):
            if date == year:
                new_date = {date: reviews_by_pg.get(group).get(date)}
                json_dict.update({group: new_date})
    return json_dict


# by group name and year

def get_reviews_by_gy(group, year):
    reviews_by_g = get_reviews_by_group_name(group)
    json_dict = {}
    for group in reviews_by_g:
        for date in reviews_by_g.get(group):
            if date == year:
                new_date = {date: reviews_by_g.get(group).get(date)}
                json_dict.update({group: new_date})
    return json_dict


# by prof name and year

def get_reviews_by_py(prof, year):
    reviews_by_prof = get_reviews_by_prof(prof)
    json_dict = {}
    for group in reviews_by_prof:
        for date in reviews_by_prof.get(group):
            if date == year:
                new_date = {date: reviews_by_prof.get(group).get(date)}
                json_dict.update({group: new_date})
    return json_dict


def remove_last_char_space(string):
    if string.endswith(" "):
        return string[:-1]
    else:
        return string
