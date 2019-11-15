import json as jsonn

state_dict = None
try:
    state_file = open("data/state.json", encoding="utf-8")
    state_dict = jsonn.load(state_file)
except:
    state_dict = {}
    # todo: crea il file e scrivilo su disco
