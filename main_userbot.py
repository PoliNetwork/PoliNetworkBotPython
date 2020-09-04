import pyrogram
from pyrogram import Client

from config import userbot_config, creators
from functions import utils


def create_group(app, group_name, message):
    # todo: create a group and set it correctly.
    description = "Gruppo del @PoliNetwork\n" \
                  "Regole @PoliRules\n" \
                  "Visita il nostro sito polinetwork.github.io"

    try:
        chat = app.create_supergroup(group_name, description)
        admin = ["polinetworkbot", "polinetwork3bot"]
        for admin2 in admin:
            app.promote_chat_member(
                chat_id=chat.id,
                user_id=admin2,
                can_change_info=True,
                can_delete_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True
            )

    except Exception as e:
        utils.notify_owners(e,
                            "Volevi creare il gruppo " +
                            '"' + str(group_name) + '"' +
                            ". Quest'opzione sarà disponibile a breve.")


def message_from_owner(app, message):
    text = str(message.text)
    if text.startswith("/create"):
        group_name = text[8:]
        create_group(app, group_name, message)
    else:
        message.reply_text("Comando non valido.")


def main():
    if userbot_config.api_id is not None:
        app = Client("policreator", userbot_config.api_id, userbot_config.api_hash)

        def hello(client, message):

            return

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
