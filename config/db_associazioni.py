import json as jsonn

messages_dict = None
try:
    messages_file = open("data/ass_messages.json", encoding="utf-8")
    messages_dict = jsonn.load(messages_file)
except:
    messages_dict = {}
    # todo: crea il file e scrivilo su disco
    pass

config_json = None
try:
    config = open("data/date.json", encoding="utf-8")
    config_json = jsonn.load(config)
except:
    config_json = {"date": "00:00:00:00:00"}
    # todo: crea il file e scrivilo su disco
    pass

group = "@PoliAssociazioni"
# group = "-1001117918825"  # @PoliAssociazioni
# group = "-1001452300981" # Canale test


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
            94927507,  # @GioScatta
            246910856  # @Marco_Crisafulli
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
    },
    "Svoltastudenti": {
        "name": "Svoltastudenti",
        "link": "",
        "users": [
            238880018,  # @CarloGiova
            341098092,  # @Teclilaa
            232009625,  # @NyquistX
            592268417  # @Francescamarra
        ]
    },
    "TernaSinistrosa": {
        "name": "TernaSinistrosa",
        "link": "",
        "users": [
            450395880,  # @Alice_Simionato
            125235631  # @fabrizio_vasconi
        ]
    },
    "JEMP": {
        "name": "JEMP",
        "link": "",
        "users": [
            624959740  # @Emi97
        ]
    },
    "Scacchi": {
        "name": "Scacchi",
        "link": "",
        "users": [
            126779544,  # @clark197
            420795114  # @Bendragon96
        ]
    },
    "Sit Polimi": {
        "name": "Sit Polimi",
        "link": "",
        "users": [
            567238569  # @enzino08
        ]
    },
    "Mussulmani": {
        "name": "Mussulmani",
        "link": "",
        "users": [
            143793921,  # @MuDy_abou
            126696677  # @hamma9
        ]
    },
    "ESTIEM": {
        "name": "ESTIEM",
        "link": "",
        "users": [
            602747198  # @andrearizzo1998
        ]
    }
}
