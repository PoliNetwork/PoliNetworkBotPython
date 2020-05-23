import json
from json import JSONDecodeError
from threading import Lock

from telegram.ext import Updater


lock_primo_list = Lock()

primo_json_path = "primo.json"


try:
    token = open("token_primo.txt").read()
except:
    token = None

if token is not None:
    token = str(token).strip()
    updater = Updater(token, use_context=True)

lock_primo_list.acquire()
try:
    primo_read = open(primo_json_path, encoding="utf-8")
    primo_list = json.load(primo_read)
except (JSONDecodeError, IOError):
    primo_list = {}

lock_primo_list.release()


def write_primo_list2():
    with open(primo_json_path, 'w', encoding="utf-8") as file_to_write:
        json.dump(primo_list, file_to_write)
    return None