import json
from json import JSONDecodeError
from threading import Lock

from telegram.ext import Updater


lock_ask_state = Lock()

ask_json_path = "ask.json"


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
try:
    primo_read = open(ask_json_path, encoding="utf-8")
    primo_list = json.load(primo_read)
except (JSONDecodeError, IOError):
    primo_list = {}

lock_ask_state.release()


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


def write_primo_list2():
    with open(ask_json_path, 'w', encoding="utf-8") as file_to_write:
        json.dump(primo_list, file_to_write)
    return None