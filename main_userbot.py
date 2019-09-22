import pyrogram
from pyrogram import Client

from config import userbot_config
from functions import utils


def main():
    if userbot_config.api_id is not None:
        app = Client("policreator", userbot_config.api_id, userbot_config.api_hash)

        @app.on_message(pyrogram.Filters.private)
        def hello(client, message):
            try:
                app.read_history(message.chat.id)
            except Exception as e:
                utils.notify_owners(e, "userbot non riesce a leggere i messaggi")
            message.reply_text("Hello {}".format(message.from_user.first_name))

        app.run()
