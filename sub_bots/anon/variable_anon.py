from telegram.ext import Updater

token = open("token_anon.txt").read()
updater = Updater(token, use_context=True)


