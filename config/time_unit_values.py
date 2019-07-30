days = ["giorni", "days", "d"]
hours = ["hours", "h", "ore"]
minutes = ["minutes", "m", "min", "minuti"]
seconds = ["seconds", "s", "sec", "secondi"]


def convert_time_in_seconds(s):
    time = s[0]
    unit = s[1]
    if days.__contains__(unit):
        return float(time) * 24 * 60 * 60;
    if hours.__contains__(unit):
        return float(time) * 60 * 60
    if minutes.__contains__(unit):
        return float(time) * 60
    else:
        return time
