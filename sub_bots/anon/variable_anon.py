from telegram.ext import Updater

token = open("sub_bots/anon/token_anon.txt").read()
updater = Updater(token, use_context=True)


