import pyrogram
from pyrogram import Client

from config import userbot_config


def main():
    if userbot_config.api_id is not None:
        app = Client("policreator", userbot_config.api_id, userbot_config.api_hash)

        @app.on_message(pyrogram.Filters.private)
        def hello(client, message):
            message.reply_text("Hello {}".format(message.from_user.first_name))

        app.run()
