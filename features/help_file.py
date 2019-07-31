import variable


def help_handler(update, context):
    variable.updater.bot.send_message(update.message.chat.id,
                                      "<i>Lista di funzioni</i>:\n"
                                      "\n📑 Sistema di recensioni dei corsi (per maggiori info /help_recensioni)\n"
                                      "\n🙋 <a href='https://polinetwork.github.io/it/faq/index.html'>"
                                      "FAQ (domande frequenti)</a>\n"
                                      "\n🏫 Bot ricerca aule libere @AulePolimiBot\n"
                                      "\n👥 Gruppo consigliati e utili /groups\n"
                                      "\n✍ Per contattarci /contact",
                                      parse_mode="HTML")


def help_groups_handler(update, context):
    variable.updater.bot.send_message(update.message.chat.id,
                                      "<i>Lista di gruppi consigliati</i>:\n"
                                      "\n👥 Gruppo di tutti gli studenti @PoliGruppo\n"
                                      "\n🤔 Hai domande? Chiedile qui @InfoPolimi\n"
                                      "\n📖 Libri @PoliBook\n"
                                      "\nRicordiamo che sul nostro sito vi sono tutti i link"
                                      " ai gruppi con tanto ricerca, facci un salto!\n"
                                      "https://polinetwork.github.io/",
                                      parse_mode="HTML")
