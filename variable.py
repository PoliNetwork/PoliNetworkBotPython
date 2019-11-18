import json
from json import JSONDecodeError
from threading import Lock

from telegram.ext import Updater

lock_to_delete = Lock()
lock_group_list = Lock()
lock_material_list = Lock()

try:
    token = open("token.txt").read()
except:
    token = None

if token is not None:
    updater = Updater(token, use_context=True)

lock_group_list.acquire()
try:
    group_read = open("data/groups.json", encoding="utf-8")
    groups_list = json.load(group_read)['Gruppi']
except (JSONDecodeError, IOError):
    groups_list = []

lock_group_list.release()

