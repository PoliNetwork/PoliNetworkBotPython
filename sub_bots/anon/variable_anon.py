from telegram.ext import Updater

token = open("sub_bots/anon/token_anon.txt").read()

if token is not None:
    token = str(token).strip()
# token = open("token.txt").read()

updater = None

try:
    updater = Updater(token, use_context=True)
except Exception as e:
    print(str(token) + " " + str(e))


