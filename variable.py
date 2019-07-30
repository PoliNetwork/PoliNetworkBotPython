import json
from json import JSONDecodeError

from telegram.ext import Updater

token = open("token.txt").read()
updater = Updater(token, use_context=True)

try:
    group_read = open("data/groups.json", encoding="utf-8")
    groups_list = json.load(group_read)['Gruppi']
except (JSONDecodeError, IOError):
    groups_list = []
