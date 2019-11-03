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
    },
    "PoliRadio": {
        "name": "PoliRadio",
        "link": "",
        "users": [
            381711172  # @johnnyshock
        ]
    },
    "MESA": {
        "name": "MESA",
        "link": "",
        "users": [
            572959546,  # @Paoli_sPRitz_ina
            498674296,  # @FrauLichteschtoin
            169445839,  # @SimoneMaestri
            436266604,  # @alepas
            457924371,  # @tommy_lucarelli
            192532766,  # @emilygreta
            191331983  # @fatmagentatranslucent
        ]
    },
    "ListaAperta": {
        "name": "ListaAperta",
        "link": "",
        "users": [
            451955751  # @matteooggioni
        ]
    },
    "AESport": {
        "name": "AESport",
        "link": "",
        "users": [
            94927507  # @GioScatta
        ]
    },
    "AIM": {
        "name": "AIM",
        "link": "",
        "users": [
            89735486  # @SirPopiel
        ]
    },
    "Resilient GAP": {
        "name": "Resilient GAP",
        "link": "",
        "users": [
            566650603  # @Eleonora_Redaelli
        ]
    },
    "Skyward": {
        "name": "Skyward",
        "link": "",
        "users": [
            93369600  # @jeyjey11
        ]
    }
}
