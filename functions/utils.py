import datetime
import hashlib
import json
import time
from json import JSONDecodeError
from threading import Thread

import requests
from telegram.error import Unauthorized

import variable
from config import blacklist_words, creators

try:
    file = open("data/to_delete.json", encoding="utf-8")
    messages_list_to_delete = json.load(file)
except (JSONDecodeError, IOError):
    messages_list_to_delete = []


def escape(html):
    """Returns the given HTML with ampersands, quotes and carets encoded."""
    html = str(html)
    return html.replace('&', '&amp;').replace('<', '&lt;') \
        .replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')


def add_message_to_delete(group_id, done2):
    global messages_list_to_delete

    j5on = {
        "group_id": group_id,
        "message_id": done2.message_id,
        "datetime": str(datetime.datetime.now().timestamp())
    }
    variable.lock_to_delete.acquire()
    messages_list_to_delete.append(j5on)
    with open("data/to_delete.json", 'w', encoding="utf-8") as file_to_write:
        json.dump(messages_list_to_delete, file_to_write)
    variable.lock_to_delete.release()


def send_in_private_or_in_group(text, group_id, user):
    success = True
    user_id = user.id

    try:
        variable.updater.bot.send_message(user_id, text)
    except Unauthorized as e:
        success = False

    if success is True:
        return

    message_to = get_user_mention(user)

    text = "[Messaggio per " + message_to + "]\n\n" + text

    done2 = variable.updater.bot.send_message(group_id, text, parse_mode="HTML")
    add_message_to_delete(group_id, done2)


def DeleteMessageThread2():
    global messages_list_to_delete

    variable.lock_to_delete.acquire()

    updated = 0
    for message in messages_list_to_delete:
        difference = float(message['datetime']) - datetime.datetime.now().timestamp()
        if (abs(difference) / 60) > 5:
            messages_list_to_delete.remove(message)
            updated += 1
            try:
                variable.updater.bot.deleteMessage(chat_id=message['group_id'],
                                                   message_id=message['message_id'])
            except:
                pass

    if updated > 0:  # array is changed and so we need to update the file
        with open("data/to_delete.json", 'w', encoding="utf-8") as file_to_write:
            json.dump(messages_list_to_delete, file_to_write)

    variable.lock_to_delete.release()


class DeleteMessageThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            DeleteMessageThread2()
            time.sleep(5)


def get_user_mention(user):
    if user.username is not None and user.username != "":
        return "@" + user.username
    else:
        nome = user['first_name']
        if user['last_name'] is not None and user['last_name'] != "":
            nome = nome + " " + user["last_name"]

        nome = str(escape(nome))
        return "<a href='tg://user?id=" + str(user.id) + "'>" + nome + "</a>"


def send_file_in_private_or_warning_in_group(user, document, group_id, title):
    success = True
    user_id = user.id

    if title is None or title == "":
        title = "[No title]"

    caption = escape("Review: " + title)
    try:
        variable.updater.bot.send_document(chat_id=user_id, document=document, caption=caption)
    except Unauthorized as e:
        success = False

    if success is True:
        return

    message_to = get_user_mention(user)

    text = message_to + ", devi prima scrivermi in privato per ricevere ciò che hai chiesto!"

    done2 = variable.updater.bot.send_message(group_id, text, parse_mode="HTML")
    add_message_to_delete(group_id, done2)


def is_valid(text):
    if text is None or text == "":
        return True

    t = text.split(" ")
    for word in t:
        if (str(word)).lower() in blacklist_words.blacklist_words:
            return False
    return True


def mute_and_delete(message):
    chat = message.chat
    user = message.from_user.id
    variable.updater.bot.restrict_chat_member(chat.id,
                                              user,
                                              until_date=int(datetime.datetime.now().timestamp()) + 900)
    variable.updater.bot.delete_message(chat_id=chat.id, message_id=message.message_id)


def has_spam_links(text):
    t = text.split(" ")
    for word in t:
        for banned_site in blacklist_words.blacklist_sites:
            if word.find(banned_site) >= 0:
                return True

    return False


def has_spam_mention(text):
    t = text.split(" ")
    for word in t:
        if word.startswith("@") and word not in blacklist_words.allowed_tags:
            try:
                chat = variable.updater.bot.get_chat(word)
                if chat.type != "private":
                    return True
            except Exception as e:
                pass

    return False


def is_spam(text):
    if text is None or text == "":
        return False

    text = str(text).lower()

    has_link = text.find("http")
    if has_link >= 0:
        is_spam_link = has_spam_links(text)
        if is_spam_link:
            return True

    has_mention = text.find("@")
    if has_mention >= 0:
        is_spam_mention = has_spam_mention(text)
        if is_spam_mention:
            return True

    return False


def leave_chat(chat, ec1, ec2):
    text = "Solo gli amministratori di @PoliNetwork possono aggiungermi ai gruppi!" \
           " Sono uscito dal gruppo. Contatta gli amministratori.\n"
    text += "Error code: "
    text += str(ec1)
    text += "-"
    text += str(ec2)
    variable.updater.bot.send_message(chat.id, text)
    variable.updater.bot.leave_chat(chat.id)


def validate_link(link):
    return "tgme_page_title" in requests.get(link).text


def detectIfToUpdate(p):
    link2 = p['Chat']

    if link2 is None:
        return True

    try:
        link2 = link2['invite_link']
    except:
        return True

    if link2 is None:
        return True
    elif len(link2) < 3:
        return True
    else:
        pvt_link_format = "https://t.me/joinchat/"
        pvt_link_format += link2.split("/")[len(link2.split("/")) - 1]

        pbl_link_format = "https://t.me/"
        pbl_link_format += link2.split("/")[len(link2.split("/")) - 1]

        if validate_link(pvt_link_format) is False and validate_link(pbl_link_format) is False:
            return True

    return False


def get_link_and_last_update(id2):
    chat = variable.updater.bot.get_chat(id2)
    link = chat.invite_link

    if link is None or link == "":
        try:
            link = variable.updater.bot.export_chat_invite_link(id2)
        except:
            pass

    if link is None or link == "":
        return None, None

    last_update = str(datetime.datetime.now())
    return link, last_update


def update_link(p):
    id2 = None

    (invite_link, last_update) = None, None
    title = None

    try:
        id2 = p['Chat']['id']
        title = p['Chat']['title']
    except:
        pass

    for group in variable.groups_list:
        if group['Chat']['id'] == id2:

            title2 = None
            try:
                title2 = group['Chat']['title']
            except:
                pass

            id_is_good = True
            if id2 is None:
                id_is_good = False
            else:
                id3 = str(id2)
                if len(id3) < 1:
                    id_is_good = False

            if title2 == title or id_is_good:
                try:
                    if invite_link is not None:
                        group['Chat']['invite_link'] = invite_link
                        group['LastUpdateInviteLinkTime'] = last_update
                    else:
                        (invite_link, last_update) = get_link_and_last_update(id2)
                        group['Chat']['invite_link'] = invite_link
                        group['LastUpdateInviteLinkTime'] = last_update
                except:
                    pass


def check3(message, list_to_update):
    for group in list_to_update:
        try:
            variable.updater.bot.send_message(message.chat.id, str(group))
        except:
            pass


def check2(message):
    list_to_update = []

    for p in variable.groups_list:

        to_update = detectIfToUpdate(p)

        if to_update:
            list_to_update.append(p)

    variable.updater.bot.send_message(message.chat.id, str(len(list_to_update)))

    if len(list_to_update) < 5:
        check3(message, list_to_update)

    done = False
    try:
        variable.lock_group_list.acquire()

        for p in list_to_update:
            try:
                update_link(p)
            except:
                try:
                    variable.updater.bot.send_message(message.chat.id, "Can't update " + str(p))
                except:
                    variable.updater.bot.send_message(message.chat.id, "Can't update a group")

        groups_dict = {"Gruppi": variable.groups_list}
        with open("data/groups.json", 'w', encoding="utf-8") as file2:
            json.dump(groups_dict, file2)

        done = True

    except:
        pass

    variable.lock_group_list.release()

    if done:
        variable.updater.bot.send_message(message.chat.id, "Done")
    else:
        variable.updater.bot.send_message(message.chat.id, "Eccezione check!")


def check(update, context):
    message = update.message
    chat = message.chat
    if chat.id in creators.owners:
        try:
            check2(message)
        except Exception as inst:
            try:
                variable.updater.bot.send_message(chat.id, str(inst))
            except:
                try:
                    variable.updater.bot.send_message(chat.id, "Eccezione!")
                except:
                    pass
        except:
            try:
                variable.updater.bot.send_message(chat.id, "Eccezione!")
            except:
                pass


def notify_owners(e):
    e2 = str(e)
    for owner2 in creators.owners:
        variable.updater.bot.send_message(owner2, "Eccezione:\n\n" + e2)


def forward_message_anon(group_id, message, user_id, reply, identity):
    identity = int(identity)

    if identity == 0:
        author_line = ""
    else:
        salt = open("salt/salt_anonimi.txt", encoding="utf-8").read()
        to_hash = (str(user_id) + str(identity) + str(salt)).encode('utf-8')
        hash2 = hashlib.sha512(to_hash).hexdigest()
        author_id = (str(hash2)[:6]).upper()

        author_line = "\n\nAuthor: #id_" + str(author_id)

    try:
        caption = ""
        if message.caption is not None:
            caption = message.caption

        if message.text is not None:
            message_sent = variable.updater.bot.send_message(chat_id=group_id,
                                                             text=message.text + author_line, reply_to_message_id=reply)
        elif message.photo:
            message_sent = variable.updater.bot.send_photo(chat_id=group_id,
                                                           photo=message.photo[0],
                                                           caption=caption + author_line, reply_to_message_id=reply)
        elif message.audio:
            message_sent = variable.updater.bot.send_audio(chat_id=group_id,
                                                           audio=message.audio.file_id,
                                                           caption=caption + author_line, reply_to_message_id=reply)
        elif message.voice is not None:
            message_sent = variable.updater.bot.send_voice(chat_id=group_id,
                                                           voice=message.voice.file_id,
                                                           caption=caption + author_line, reply_to_message_id=reply)
        elif message.video is not None:
            message_sent = variable.updater.bot.send_video(chat_id=group_id,
                                                           video=message.video.file_id,
                                                           caption=caption + author_line, reply_to_message_id=reply)
        elif message.video_note is not None:
            message_sent = variable.updater.bot.send_video_note(chat_id=group_id,
                                                                video_note=message.video_note.file_id,
                                                                caption=caption + author_line,
                                                                reply_to_message_id=reply)
        elif message.document is not None:
            message_sent = variable.updater.bot.send_document(chat_id=group_id,
                                                              document=message.document.file_id,
                                                              caption=caption + author_line, reply_to_message_id=reply)
        elif message.sticker is not None:
            message_sent = variable.updater.bot.send_sticker(chat_id=group_id,
                                                             sticker=message.sticker.file_id,
                                                             caption=caption + author_line, reply_to_message_id=reply)
        elif message.location is not None:
            message_sent = variable.updater.bot.send_location(chat_id=group_id,
                                                              latitude=message.location.latitude,
                                                              longitude=message.location.longitude,
                                                              caption=caption + author_line, reply_to_message_id=reply)
        else:
            return False, None

        return True, message_sent
    except Exception as e:
        notify_owners(e)
        return False, None


def forward_message(group_id, message):
    try:
        message_sent = variable.updater.bot.forward_message(group_id, message.chat.id, message.message_id)
        return True, message_sent
    except Exception as e:
        e2 = str(e)
        for owner2 in creators.owners:
            variable.updater.bot.send_message(owner2, "Error forwarding message!\n\n" + e2)
    return False, None


def is_an_anon_message_link(parts):
    if len(parts) <= 2:
        return False, ""
    if "t.me/PoliAnoniMi/" in parts[2]:
        return True, parts[2].split("/")[-1]
