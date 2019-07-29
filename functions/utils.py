import datetime

import bot


def escape(html):
    """Returns the given HTML with ampersands, quotes and carets encoded."""
    html = str(html)
    return (html.encode('utf-8')).replace('&', '&amp;').replace('<', '&lt;') \
        .replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')


def send_in_private_or_in_group(text, group_id, user):
    success = True
    user_id = user.id

    try:
        bot.updater.bot.send_message(user_id, text)
    except:
        success = False

    if success is True:
        return

    message_to = "";
    if user.username is not None and user.username != "":
        message_to = "@" + user.username
    else:
        nome = user['first_name']
        if user['last_name'] is not None and user['last_name'] != "":
            nome = nome + " " + user["last_name"]

        nome = str(escape(nome))
        message_to = "<a href='tg://user?id=" + user_id + "'>" + nome + "</a>"

    text = "[Messaggio per " + message_to + "]\n" + text

    done2 = bot.updater.bot.send_message(group_id, text, parse_mode="HTML")

    # to_delete.add(group_id, done2.message_id, datetime.datetime.now())
