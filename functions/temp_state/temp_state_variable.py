import datetime
import json as jsonn
import time
from threading import Lock, Thread

import variable

state_dict = None
lock_state = Lock()


def delete_state(id_telegram):
    lock_state.acquire()
    try:
        del state_dict[id_telegram]
    except:
        pass
    save_file_no_lock()
    lock_state.release()
    return None


def DeleteMessageStateThread3(s1):
    stato = state_dict[s1]
    time_stato = stato["time"]
    datetime_object = datetime.datetime.strptime(time_stato, "%m/%d/%Y %H:%M:%S %f")
    difference = datetime.datetime.now() - datetime_object
    if difference.total_seconds() > 60 * 5:
        delete_state(s1)
        variable.updater.bot.send_message(chat_id=s1,
                                          text="La tua sessione è scaduta. L'operazione che stavi facendo è stata "
                                               "annullata per tua inattività.")

    return None


def DeleteMessageStateThread2():
    global state_dict

    try:
        for s1 in state_dict.keys():
            try:
                DeleteMessageStateThread3(s1)
            except:
                pass
    except:
        pass

    return None


class DeleteMessageStateThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:

            try:
                DeleteMessageStateThread2()
            except:
                pass

            time.sleep(15)


def save_file_no_lock():
    global state_dict

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

thread = DeleteMessageStateThread()
thread.start()
