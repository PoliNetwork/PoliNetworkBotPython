days = ["giorni", "days", "d"]
hours = ["hours", "h", "ore"]
minutes = ["minutes", "m", "min", "minuti"]
seconds = ["seconds", "s", "sec", "secondi"]

# e.g. s = 10 s


def convert_time_in_seconds(s):
    time = float(s.split(" ")[0])
    unit = s.split(" ")[1]
    if days.__contains__(unit):
        return time * 24 * 60 * 60;
    if hours.__contains__(unit):
        return time * 60 * 60
    if minutes.__contains__(unit):
        return time * 60
    else:
        return time
