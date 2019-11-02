import datetime
import json as jsonn
import time
from threading import Thread
import telegram.ext

import variable
from config import db_associazioni
from functions import utils


def errore_no_associazione(update):
    utils.send_in_private_or_in_group("Non fai parte di nessuna associazione, scrivi agli admin di @PoliNetwork",
                                      update.message.chat.id, update.message.from_user)
    pass


def get_associazione_name_from_user(x):
    for ass in db_associazioni.json.keys():
        for user in db_associazioni.json.get(ass).get("users"):
            if user == x:
                return ass
    return None


def get_associazione_json_from_associazione_name(name):
    for ass in db_associazioni.json.keys():
        if ass is name:
            return db_associazioni.json.get(ass)
    return None


# prendi il messaggio dell'associazione dal nome dell'associazione
def get_message_from_associazione_name(name):
    assoc = None
    for associ in db_associazioni.json.keys():
        if associ is name:
            assoc = associ

    if db_associazioni.messages_dict.__contains__(assoc):
        return db_associazioni.messages_dict.get(assoc)

    return None


def get_message_from_associazione_json(json):
    assoc = None
    for associ in db_associazioni.json.keys():
        if associ is json:
            assoc = associ

    if db_associazioni.messages_dict.__contains__(assoc):
        return db_associazioni.messages_dict.get(assoc)

    return None


def CreatePhotoFromJson(read_message):
    try:
        return telegram.PhotoSize(file_id=read_message["message_to_send_photo_file_id"],
                                  width=read_message["message_to_send_photo_width"],
                                  height=read_message["message_to_send_photo_height"],
                                  file_size=read_message["message_to_send_photo_file_size"])
    except Exception as e:
        pass

    return None


def assoc_read(update, context):
    # leggi ed inoltra
    associazione = get_associazione_name_from_user(update.message.from_user.id)

    if associazione is None:
        errore_no_associazione(update)
        return None

    error1 = "Nessun messaggio in coda!"

    try:
        read_message = get_message_from_associazione_name(associazione)
        if read_message is None:
            utils.send_in_private_or_in_group(error1, update.message.chat.id, update.message.from_user)
            pass
        else:
            inviato, messaggio_inviato = invia_anon(update.message.chat.id,
                                                    caption=read_message.get("message_to_send_caption"),
                                                    text=read_message.get("message_to_send_text"),
                                                    photo=CreatePhotoFromJson(read_message),
                                                    audio_file_id=read_message.get("message_to_send_audio_file_id"),
                                                    voice_file_id=read_message.get("message_to_send_voice_file_id"),
                                                    video_file_id=read_message.get("message_to_send_video_file_id"))

            if inviato is False:
                utils.send_in_private_or_in_group(error1, update.message.chat.id, update.message.from_user)
                assoc_delete2(update, True)
                return None

    except:
        utils.send_in_private_or_in_group(error1, update.message.chat.id, update.message.from_user)
        pass
    return None


def check_message_associazioni(update):
    # todo: controllare che il messaggio rispetti i requisiti, inviare all'utente eventuali errori, e poi tornare True se il messaggio è valido, False altrimenti

    message2 = update.message.reply_to_message

    if message2 is None:
        return False

    if message2.text is None:
        return True

    if len(message2.text) > 0:
        return False
    return True


def GetLargerPhoto(photo):
    larger = None
    for photo2 in photo:
        if larger is None:
            larger = photo2

        if photo2.width > larger.width:
            larger = photo2

    return larger


def GetAudioFileID(messaggio_originale):
    try:
        return messaggio_originale.audio.file_id
    except:
        return None


def GetVoiceFileID(messaggio_originale):
    try:
        return messaggio_originale.voice.file_id
    except:
        return None


def GetVideoFileID(messaggio_originale):
    try:
        return messaggio_originale.video.file_id
    except:
        return None


def assoc_write(update, context):
    associazione = get_associazione_name_from_user(update.message.from_user.id)

    if associazione is None:
        errore_no_associazione(update)
        return None

    if update.message.reply_to_message is None:
        utils.send_in_private_or_in_group(
            "Devi scrivere il comando rispondendo al messaggio che vuoi inviare!",
            update.message.chat.id, update.message.from_user)
        return

    messaggio_valido = check_message_associazioni(update)
    if messaggio_valido:
        if get_message_from_associazione_name(associazione) is not None:
            utils.send_in_private_or_in_group("Messaggio già in coda. Rimuovilo con /assoc_delete.",
                                              update.message.chat.id, update.message.from_user)
            return

        else:
            messaggio_originale = update.message.reply_to_message
            if messaggio_originale is None:
                utils.send_in_private_or_in_group("Devi rispondere ad un messaggio per aggiungerlo alla coda",
                                                  update.message.chat.id, update.message.from_user)
                return

            photo2 = GetLargerPhoto(messaggio_originale.photo)
            audio_file_id = GetAudioFileID(messaggio_originale)
            voice_file_id = GetVoiceFileID(messaggio_originale)
            video_file_id = GetVideoFileID(messaggio_originale)
            dict1 = {"message_to_send_caption": messaggio_originale.caption,
                     "message_to_send_text": messaggio_originale.text,
                     "message_to_send_photo_file_id": photo2.file_id,
                     "message_to_send_photo_file_size": photo2.file_size,
                     "message_to_send_photo_height": photo2.height,
                     "message_to_send_photo_width": photo2.width,
                     "message_to_send_audio_file_id": audio_file_id,
                     "message_to_send_voice_file_id": voice_file_id,
                     "message_to_send_video_file_id": video_file_id,
                     "time": datetime.datetime.now().strftime(
                         '%d-%m-%Y %H:%M:%S')
                     }
            db_associazioni.messages_dict.__setitem__(associazione, dict1)
            save_ass_messages()
            utils.send_in_private_or_in_group("Messaggio aggiunto alla coda correttamente",
                                              update.message.chat.id, update.message.from_user)
        pass
    else:
        utils.send_in_private_or_in_group(
            "Il messaggio non rispetta i requisiti richiesti! Contatta gli admin di @PoliNetwork!",
            update.message.chat.id, update.message.from_user)

    return None


def assoc_delete2(update, nascondi_messaggi):
    associazione = get_associazione_name_from_user(update.message.from_user.id)

    if associazione is None:
        errore_no_associazione(update)
        return None

    read_message = get_message_from_associazione_name(associazione)
    if read_message is None:
        if nascondi_messaggi is False:
            utils.send_in_private_or_in_group("Nessun messaggio in coda",
                                              update.message.chat.id, update.message.from_user)
        pass
    else:
        db_associazioni.messages_dict.pop(associazione, None)
        if nascondi_messaggi is False:
            utils.send_in_private_or_in_group("Messaggio rimosso con successo",
                                              update.message.chat.id, update.message.from_user)
        save_ass_messages()
    pass


def assoc_delete(update, context):
    assoc_delete2(update, False)
    return None


class start_check_Thread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            start_check()
            time.sleep(60 * 5)


def invia_anon(destination, caption, text, photo, audio_file_id, voice_file_id, video_file_id):
    try:

        if text is not None:
            message_sent = variable.updater.bot.send_message(chat_id=destination,
                                                             text=text)
        elif photo:
            message_sent = variable.updater.bot.send_photo(chat_id=destination,
                                                           photo=photo,
                                                           caption=caption)
        elif audio_file_id:
            message_sent = variable.updater.bot.send_audio(chat_id=destination,
                                                           audio=audio_file_id,
                                                           caption=caption)
        elif voice_file_id is not None:
            message_sent = variable.updater.bot.send_voice(chat_id=destination,
                                                           voice=voice_file_id,
                                                           caption=caption)
        elif video_file_id is not None:
            message_sent = variable.updater.bot.send_video(chat_id=destination,
                                                           video=video_file_id,
                                                           caption=caption)
        #
        # elif video_note is not None:
        #    message_sent = variable.updater.bot.send_video_note(chat_id=destination,
        #                                                        video_note=video_note.file_id,
        #                                                        caption=caption)
        # elif document is not None:
        #    message_sent = variable.updater.bot.send_document(chat_id=destination,
        #                                                      document=document.file_id,
        #                                                      caption=caption)
        # elif sticker is not None:
        #    message_sent = variable.updater.bot.send_sticker(chat_id=destination,
        #                                                     sticker=sticker.file_id,
        #                                                     caption=caption)
        # elif location is not None:
        #    message_sent = variable.updater.bot.send_location(chat_id=destination,
        #                                                      latitude=location.latitude,
        #                                                      longitude=location.longitude,
        #                                                      caption=caption)
        else:
            return False, None

        return True, message_sent
    except Exception as e:
        utils.notify_owners(e)
        return False, None


def send_scheduled_messages():
    for associazione in db_associazioni.messages_dict:
        try:
            associazione2 = db_associazioni.messages_dict.get(associazione)

            inviato, forse_inviato = invia_anon(db_associazioni.group,
                                                caption=associazione2['message_to_send_caption'],
                                                text=associazione2['message_to_send_text'],
                                                photo=CreatePhotoFromJson(associazione2),
                                                audio_file_id=associazione2["message_to_send_audio_file_id"],
                                                voice_file_id=associazione2["message_to_send_voice_file_id"],
                                                video_file_id=associazione2["message_to_send_video_file_id"])

            if inviato is True:
                # todo: inviare un messaggio a quelli dell'associazione dicendo che hanno preso parte a questa
                #  data di pubblicazione
                pass
            else:
                # todo: inviare un messaggio a quelli dell'associazione dicendo che non hanno preso parte a questa
                #  data di pubblicazione
                pass

        except Exception as e:
            pass

    db_associazioni.date = "00:00:00:00:00"
    db_associazioni.config_json.update({"date": db_associazioni.date})
    save_date()

    for associazione in db_associazioni.messages_dict:
        try:
            associazione2 = db_associazioni.messages_dict.get(associazione)
            associazione2['message_to_send_caption'] = None
            associazione2['message_to_send_text'] = None
            associazione2['message_to_send_photo_file_id'] = None
            associazione2['message_to_send_photo_file_size'] = None
            associazione2['message_to_send_photo_height'] = None
            associazione2['message_to_send_photo_width'] = None
            associazione2["message_to_send_audio_file_id"] = None
            associazione2["message_to_send_voice_file_id"] = None
            associazione2["message_to_send_video_file_id"] = None
            associazione2['time'] = None
            db_associazioni.messages_dict[associazione] = associazione2
        except Exception as e:
            pass

    save_ass_messages()
    pass


def start_check():
    if db_associazioni.date == "00:00:00:00:00":
        return

    time2 = db_associazioni.date.split(":")
    day = time2[2]
    month = time2[1]
    year = time2[0]
    hour = time2[3]
    minute = time2[4]

    scheduled_time = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
    dt_now = datetime.datetime.now()
    if dt_now > scheduled_time:  # i.e. is the scheduled time over?
        send_scheduled_messages()


def save_ass_messages():
    try:
        with open("data/ass_messages.json", 'w', encoding="utf-8") as file:
            jsonn.dump(db_associazioni.messages_dict, file)
    except Exception as e:
        pass


def save_date():
    with open("data/date.json", 'w', encoding="utf-8") as file:
        jsonn.dump(db_associazioni.config_json, file)
