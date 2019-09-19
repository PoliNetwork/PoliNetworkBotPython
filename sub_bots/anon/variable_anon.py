from telegram.ext import Updater

token = open("token.txt").read()
updater = Updater(token, use_context=True)


