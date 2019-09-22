import pyrogram
from pyrogram import Client

from config import userbot_config, creators
from functions import utils


def create_group(app, group_name):
    # todo: create a group and set it correctly.
    pass


def message_from_owner(app, message):
    text = str(message.text)
    if text.startswith("/create"):
        group_name = text[7:]
        create_group(app, group_name)
    else:
        message.reply_text("Comando non valido.".format(message.from_user.first_name))


def main():
    if userbot_config.api_id is not None:
        app = Client("policreator", userbot_config.api_id, userbot_config.api_hash)

        @app.on_message(pyrogram.Filters.private)
        def hello(client, message):
            try:
                app.read_history(message.chat.id)
            except Exception as e:
                utils.notify_owners(e, "userbot non riesce a leggere i messaggi")

            try:
                if message.chat.id in creators.owners:
                    message_from_owner(app, message)
                    return
            except Exception as e:
                utils.notify_owners(e, "userbot non riesce a controllare il messaggio")

            message.reply_text("Hello {}".format(message.from_user.first_name))

        app.run()
