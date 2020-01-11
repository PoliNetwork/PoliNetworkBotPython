def messageFromObject(message_object):
    if message_object is None:
        return None

    html = None
    try:
        html = str(message_object.caption_html)
    except:
        pass

    r = {
        "message_id": message_object.message_id,
        "reply_to_message": messageFromObject(message_object.reply_to_message),
        "photo": getPhotosFromObject(message_object.photo),
        "audio": getAudioFromObject(message_object.audio),
        "video": getVideoFromObject(message_object.video),
        "voice": getVoiceFromObject(message_object.voice),
        "caption_html": html,
        "text": message_object.text,
        "date": str(message_object.date),
        "from_user": getUserFromObject(message_object.from_user),
        "chat": getChatFromObject(message_object.chat)
    }

    return r


def getUserFromObject(message_from_user):
    if message_from_user is None:
        return None

    lc = None
    try:
        lc = message_from_user.language_code
    except:
        pass

    r = {"id": message_from_user.id, "first_name": message_from_user.first_name,
         "last_name": message_from_user.last_name, "username": message_from_user.username,
         "language_code": lc}
    return r


def getPhotosFromObject(photo):
    if photo is None:
        return None

    if len(photo) == 0:
        return []

    photos = []
    for photo_s in photo:
        photo_j = {"file_id": photo_s.file_id,
                   "file_size": photo_s.file_size,
                   "height": photo_s.height,
                   "width": photo_s.width}
        photos.append(photo_j)

    return photos


def getAudioFromObject(audio):
    if audio is None:
        return None

    return {"file_id": audio.file_id}


def getVideoFromObject(video):
    if video is None:
        return None

    return {"file_id": video.file_id}


def getVoiceFromObject(voice):
    if voice is None:
        return None

    return {"file_id": voice.file_id}


def getChatFromObject(chat):
    r = {"id": chat.id, "type": chat.type}
    return r
