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
        "chat":getChatFromObject(message_object.chat)
    }

    return r
