import variable
from functions import utils


def help_handler(update, context):
    message = update.message

    if message.chat.type != "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                          message.chat.id, message.from_user)

        try:
            variable.updater.bot.delete_message(message.chat.id, message.message_id)
        except Exception as e:
            utils.notify_owners(e)

        return

    variable.updater.bot.send_message(update.message.chat.id,
                                      "<i>Lista di funzioni</i>:\n"
                                      "\n📑 Sistema di recensioni dei corsi (per maggiori info /help_review)\n"
                                      "\n🔖 Link ai materiali nei gruppi (per maggiori info /help_material)\n"
                                      "\n🙋 <a href='https://polinetwork.github.io/it/faq/index.html'>"
                                      "FAQ (domande frequenti)</a>\n"
                                      "\n🏫 Bot ricerca aule libere @AulePolimiBot\n"
                                      "\n🕶️ Sistema di pubblicazione anonima (per maggiori info /help_anon)\n"
                                      "\n🎙️ Registrazione delle lezioni (per maggiori info /help_record)\n"
                                      "\n👥 Gruppo consigliati e utili /groups\n"
                                      "\n⚠ Hai già letto le regole del network? @PoliRules\n"
                                      "\n✍ Per contattarci /contact",
                                      parse_mode="HTML")


def help_groups_handler(update, context):
    message = update.message

    if message.chat.type != "private":
        utils.send_in_private_or_in_group("Questo comando funziona solo in chat privata",
                                          message.chat.id, message.from_user)
        return

    variable.updater.bot.send_message(update.message.chat.id,
                                      "<i>Lista di gruppi consigliati</i>:\n"
                                      "\n👥 Gruppo di tutti gli studenti @PoliGruppo 👈\n"
                                      "\n🤔 Hai domande? Chiedile qui @InfoPolimi\n"
                                      "\n📖 Libri @PoliBook\n"
                                      "\n🔦 <a href='https://www.facebook.com/groups/138006146900748/'>"
                                      "Oggetti smarriti</a>\n"
                                      "\n🤪 Spotted & Memes @PolimiSpotted @PolimiMemes\n"
                                      "\n🥳 Eventi @PoliEventi\n"
                                      "\nRicordiamo che sul nostro sito vi sono tutti i link"
                                      " ai gruppi con tanto ricerca, facci un salto!\n"
                                      "https://polinetwork.github.io/",
                                      parse_mode="HTML")
