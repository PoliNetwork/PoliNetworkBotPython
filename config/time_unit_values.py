days = ["giorni", "days", "d"]
hours = ["hours", "h", "ore"]
minutes = ["minutes", "m", "min", "minuti"]
seconds = ["seconds", "s", "sec", "secondi"]

# e.g. s = 10 s


def convert_time_in_seconds(s):
    if days.__contains__(s):
        return 24 * 60 * 60;
    if hours.__contains__(s):
        return 60 * 60
    if minutes.__contains__(s):
        return 60
    else:
        return 1
