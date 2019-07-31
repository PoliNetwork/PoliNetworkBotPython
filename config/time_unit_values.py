days = ["giorni", "days", "d"]
hours = ["hours", "h", "ore"]
minutes = ["minutes", "m", "min", "minuti"]
seconds = ["seconds", "s", "sec", "secondi"]
months = ["mon", "mesi", "months"]
years = ["y", "years", "anni"]

# e.g. s = 10 s


def convert_time_in_seconds(s):
    if years.__contains__(s):
        return 24 * 60 * 60 * 365
    if months.__contains__(s):
        return 24 * 60 * 60 * 30
    if days.__contains__(s):
        return 24 * 60 * 60
    if hours.__contains__(s):
        return 60 * 60
    if minutes.__contains__(s):
        return 60
    else:
        return 1
