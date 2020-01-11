from telegram.ext import Updater

token = open("sub_bots/anon/token_anon.txt").read()
# token = open("token.txt").read()

updater = None
try:
    updater = Updater(token, use_context=True)
except:
    print(str(token))


