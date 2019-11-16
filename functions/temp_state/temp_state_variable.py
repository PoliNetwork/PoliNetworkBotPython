import json as jsonn
from threading import Lock

state_dict = None
lock_state = Lock()


def save_file_no_lock():
    try:
        with open("data/state.json", 'w', encoding="utf-8") as file:
            jsonn.dump(state_dict, file)
    except Exception as e:
        pass
    pass


try:
    lock_state.acquire()
    state_file = open("data/state.json", encoding="utf-8")
    state_dict = jsonn.load(state_file)
    lock_state.release()
except:
    if lock_state.locked():
        lock_state.release()

    lock_state.acquire()
    state_dict = {}
    save_file_no_lock()
    lock_state.release()
