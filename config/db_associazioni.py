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
            5651789  # @ArmeF97
        ]
    },
    "WoShou": {
        "name": "WoShou",
        "link": "",
        "users": [
            128132149  # @zhupeng
        ]
    }
}
