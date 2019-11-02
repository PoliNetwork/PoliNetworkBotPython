import json as jsonn

messages_file = open("data/ass_messages.json", encoding="utf-8")
messages_dict = jsonn.load(messages_file)

config = open("data/date.json", encoding="utf-8")
config_json = jsonn.load(config)

group = "-1001452300981"
date = config_json.get("date")

json = {
    "Best": {
        "name": "Best",
        "link": "",
        "users": [
            564927807  # @Andrea_ilSigno
        ]
    },
    "PoliNetwork": {
        "name": "PoliNetwork",
        "link": "",
        "users": [
            5651789,  # @ArmeF97
            203350312  # @GabrieleAur98
        ]
    },
    "WoShou": {
        "name": "WoShou",
        "link": "",
        "users": [
            128132149  # @zhupeng
        ]
    },
    "PoliEdro": {
        "name": "PoliEdro",
        "link": "",
        "users": [
            652321021,  # @LucaUso
            793377028,  # @Dagorsil
            402462709,  # @disturbed_potato
            10570026,  # @Markobau
            166614456,  # @Helgafell
        ]
    }
}
