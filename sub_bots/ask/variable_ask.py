import json
from json import JSONDecodeError
from threading import Lock

from telegram.ext import Updater

lock_ask_state = Lock()
lock_ask_notify_state = Lock()
lock_watch_post = Lock()

reddit = None
subreddit = None

separators_callback = "|;|"

ask_json_path = "ask.json"
ask_notify_json_path = "ask_notify.json"
watch_post_path = "watch_post.json"

subreddit_name = "polinetworktest"

flair_available = ["Immatricolazione", "Tasse", "Test di ingresso",
                   "Certificazioni", "Magistrale", "Tesi",
                   "Passaggio di corso", "Borse di studio"]
flair_available.sort()
flair_available.append("Altro")

try:
    token = open("sub_bots/ask/token_ask.txt").read()
except:
    token = None

    try:
        token = open("token_ask.txt").read()
    except:
        token = None

if token is not None:
    token = str(token).strip()
    updater = Updater(token, use_context=True)

lock_ask_state.acquire()
ask_list = {}
try:
    ask_read = open(ask_json_path, encoding="utf-8")
    ask_list = json.load(ask_read)
except (JSONDecodeError, IOError):
    ask_list = {}

lock_ask_state.release()

lock_watch_post.acquire()
watch_post_list = {}
try:
    watch_post_list_read = open(watch_post_path, encoding="utf-8")
    watch_post_list = json.load(watch_post_list_read)
except (JSONDecodeError, IOError):
    watch_post_list = {}

lock_watch_post.release()

lock_ask_notify_state.acquire()
ask_notify_list = {}
try:
    ask_notify_read = open(ask_notify_json_path, encoding="utf-8")
    ask_notify_list = json.load(ask_notify_read)
except (JSONDecodeError, IOError):
    ask_notify_list = {}

lock_ask_notify_state.release()

reddit_client_id = None
reddit_secret_id = None
reddit_password = None

try:
    reddit_client_id = open("sub_bots/ask/reddit_client_id.txt").read()
except:
    reddit_client_id = None

    try:
        reddit_client_id = open("reddit_client_id.txt").read()
    except:
        reddit_client_id = None

try:
    reddit_secret_id = open("sub_bots/ask/reddit_secret_id.txt").read()
except:
    reddit_secret_id = None

    try:
        reddit_secret_id = open("reddit_secret_id.txt").read()
    except:
        reddit_secret_id = None

try:
    reddit_password = open("sub_bots/ask/reddit_password.txt").read()
except:
    reddit_password = None

    try:
        reddit_password = open("reddit_password.txt").read()
    except:
        reddit_password = None


def clean_duplicates(list2):
    result = {}

    for key, value in list2.items():
        if value not in result.values():
            result[key] = value

    return result


ask_list = clean_duplicates(ask_list)
ask_notify_list = clean_duplicates(ask_notify_list)
watch_post_list = clean_duplicates(watch_post_list)




def write_ask_list2():
    try:
        with open(ask_json_path, 'w', encoding="utf-8") as file_to_write:
            json.dump(ask_list, file_to_write)
    except Exception as e:
        return False, e
    return True, None


def write_ask_notify_list2():
    try:
        with open(ask_notify_json_path, 'w', encoding="utf-8") as file_to_write:
            json.dump(ask_notify_list, file_to_write)
    except Exception as e:
        return False, e
    return True, None


def write_watch_post_list2():
    try:
        with open(watch_post_path, 'w', encoding="utf-8") as file_to_write:
            json.dump(watch_post_list, file_to_write)
    except Exception as e:
        return False, e
    return True, None


lock_ask_state.acquire()
write_ask_list2()
lock_ask_state.release()
