from features import anonimi


def handler(update, context):
    query = update.callback_query

    data = str(query.data).split(" ")
    if data[0] == "anon":
        anonimi.handler_callback(update, data)
        return
    else:
        # todo: in future, add new "modules"
        return

