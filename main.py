#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import MessageHandler, CommandHandler, Filters

import main_userbot
import variable
from config import creators
from features import groups, reviews, test, moderation, all_messages, materials, help_file, anonimi, recordings, \
    associazioni
from functions import utils


def start_handler(update, context):
    update.message.reply_text("Ciao! 👋\n"
                              "\nScrivi /help per la lista completa delle mie funzioni 👀\n"
                              "\nVisita anche il nostro sito https://polinetwork.github.io")


def contact_handler(update, context):
    update.message.reply_text("Puoi scriverci alla pagina facebook https://m.me/PolitecnicoDiMilanoNetwork")


creators.me = variable.updater.bot.get_me().id

dispatcher = variable.updater.dispatcher

# main
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('contact', contact_handler))

# help
dispatcher.add_handler(CommandHandler('help', help_file.help_handler))
dispatcher.add_handler(CommandHandler('groups', help_file.help_groups_handler))

# review
dispatcher.add_handler(CommandHandler('help_review', reviews.help_handler))
dispatcher.add_handler(CommandHandler('review', reviews.add_review))
dispatcher.add_handler(CommandHandler('get_reviews', reviews.get_reviews_html))

# PoliAnoniMi
dispatcher.add_handler(CommandHandler('anon', anonimi.help_handler))
dispatcher.add_handler(CommandHandler('help_anon', anonimi.help_handler))

# PoliRecordings
dispatcher.add_handler(CommandHandler('postrecording', recordings.post_recordings))
dispatcher.add_handler(CommandHandler('help_record', recordings.help_handler))

# test
dispatcher.add_handler(CommandHandler('getgroupjson', groups.get_group_json))
dispatcher.add_handler(CommandHandler('getreviewjson', reviews.get_review_json))
dispatcher.add_handler(CommandHandler('testmessage', test.test_message))
dispatcher.add_handler(CommandHandler('stress_test', test.stress_test))
dispatcher.add_handler(CommandHandler('check', utils.check))

# moderation
dispatcher.add_handler(CommandHandler('mute', moderation.mutes_bans_handler))
dispatcher.add_handler(CommandHandler('unmute', moderation.mutes_bans_handler))
dispatcher.add_handler(CommandHandler('ban', moderation.mutes_bans_handler))
dispatcher.add_handler(CommandHandler('unban', moderation.mutes_bans_handler))
dispatcher.add_handler(CommandHandler('banAll', moderation.ban_all))

# books and materials
dispatcher.add_handler(CommandHandler('help_material', materials.help_handler))
dispatcher.add_handler(CommandHandler('material', materials.material_handler))
dispatcher.add_handler(CommandHandler('add_material', materials.add_remove_material))
dispatcher.add_handler(CommandHandler('remove_material', materials.add_remove_material))

# associazioni
dispatcher.add_handler(CommandHandler('assoc_read', associazioni.assoc_read))
dispatcher.add_handler(CommandHandler('assoc_write', associazioni.assoc_write))
dispatcher.add_handler(CommandHandler('assoc_delete', associazioni.assoc_delete))

# all
dispatcher.add_handler(MessageHandler(Filters.all, all_messages.check_message))

thread = utils.DeleteMessageThread()
thread.start()

thread2 = associazioni.start_check_Thread()
thread2.start()

variable.updater.start_polling()

# ---
# BOT - USERBOT
main_userbot.main()
