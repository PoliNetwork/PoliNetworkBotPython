import datetime
import json
import re
import time
from json import JSONDecodeError
from threading import Thread

import requests
import telegram
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
    user_id = user['id']

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
    if user['username'] is not None and user['username'] != "":
        return "@" + user['username']
    else:
        nome = user['first_name']
        if user['last_name'] is not None and user['last_name'] != "":
            nome = nome + " " + user["last_name"]

        nome = str(escape(nome))
        return "<a href='tg://user?id=" + str(user['id']) + "'>" + nome + "</a>"


def send_file_in_private_or_warning_in_group(user, document, group_id, title, forced_title):
    success = True
    user_id = user.id

    if title is None or title == "":
        title = "[No title]"

    caption = escape("Review: " + title)
    try:
        if forced_title:
            variable.updater.bot.send_document(chat_id=user_id, document=document, caption=title)
        else:
            variable.updater.bot.send_document(chat_id=user_id, document=document, caption=caption)
    except Unauthorized as e:
        success = False
    except Exception as e2:
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
    if message is None:
        return

    temp_mute_and_delete(message, 900)
    return


def temp_mute_and_delete(message, seconds):
    if message is None:
        return

    chat = message.chat

    if chat is None:
        return

    user = message.from_user.id
    permission = telegram.ChatPermissions(can_add_web_page_previews=False,
                                          can_send_media_messages=False,
                                          can_send_messages=False,
                                          can_send_other_messages=False)
    variable.updater.bot.restrict_chat_member(chat.id,
                                              user,
                                              until_date=int(datetime.datetime.now().timestamp()) + seconds,
                                              permissions=permission)
    variable.updater.bot.delete_message(chat_id=chat.id, message_id=message.message_id)
    return


def has_spam_links(text):
    t = text.split(" ")
    for word in t:
        for banned_site in blacklist_words.blacklist_sites:
            if word.find(banned_site) >= 0:
                return True

        if word.find("t.me") >= 0:
            if word.find("t.me/c/") < 0:
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


def remove_spaces(text):
    while True:
        if text.startswith(" "):
            text = text[1:]
        else:
            break

    return text


def leave_chat(chat, ec1, ec2, ec3):
    text = "Solo gli amministratori di @PoliNetwork possono aggiungermi ai gruppi!" \
           " Sono uscito dal gruppo. Contatta gli amministratori.\n"
    text += "Error code: "
    text += str(ec1)
    text += "-"
    text += str(ec2)
    text += "-"
    text += str(ec3)
    variable.updater.bot.send_message(chat.id, text)
    variable.updater.bot.leave_chat(chat.id)


def validate_link(link):
    return "tgme_page_title" in requests.get(link).text


def detectIfToUpdate2(p):
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


def detectIfToUpdate(p):
    c = detectIfToUpdate2(p)
    if c is True:
        keep_link = None
        try:
            keep_link = p["keep_link"]
        except:
            pass

        if keep_link is None or keep_link is True:
            c = True
        else:
            c = False

    return c


def contains_ko_ja_chi(texts):
    if re.search("[\uac00-\ud7a3]", texts):
        return True
    if re.search("[\u3040-\u30ff]", texts):
        return True
    if re.search("[\u4e00-\u9FFF]", texts):
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

                        keep_link = None
                        try:
                            keep_link = group["keep_link"]
                        except:
                            pass

                        if keep_link is True or keep_link is None:
                            (invite_link, last_update) = get_link_and_last_update(id2)
                            group['Chat']['invite_link'] = invite_link
                            group['LastUpdateInviteLinkTime'] = last_update
                        else:
                            group['Chat']['invite_link'] = None
                            group['LastUpdateInviteLinkTime'] = None
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


def notify_owners(e, extra_info=None):
    e2 = str(e)

    if extra_info is not None:
        e2 += "\n\n" + str(extra_info)

    for owner2 in creators.owners:
        variable.updater.bot.send_message(owner2, "Eccezione:\n\n" + e2)


def forward_message(group_id, message):
    try:
        message_sent = variable.updater.bot.forward_message(group_id, message.chat.id, message.message_id)
        return True, message_sent
    except Exception as e:
        e2 = str(e)
        for owner2 in creators.owners:
            variable.updater.bot.send_message(owner2, "Error forwarding message!\n\n" + e2)
    return False, None


def check_date(date):
    if date == "":
        return False
    if "/" not in date:
        return False
    f_year = date.split("/")[0]
    s_year = date.split("/")[1]

    if len(f_year) != 4 or len(s_year) != 4:
        return False

    if s_year <= f_year or (s_year - f_year) > 1:
        return False
    return True


def getLog(update, context):
    message = update.message
    chat = message.chat
    if chat.id in creators.owners:
        try:
            variable.updater.bot.send_document(chat_id=message.chat.id, document=open("out_log.txt", 'rb'))
        except:
            try:
                variable.updater.bot.send_message(chat.id, "Eccezione out_log")
            except:
                pass
            pass