import json

import requests
from flask import Flask, request

from sub_bots.fb_messenger.fb_messenger_config import VERIFY_TOKEN, PAT

app = Flask(__name__)


@app.route('/', methods=['GET'])
def handle_verification():
    """
    Verifies facebook webhook subscription
    Successful when verify_token is same as token sent by facebook app
    """
    if request.args.get('hub.verify_token', '') == VERIFY_TOKEN:
        print("successfully verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong verification token!")
        return "Wrong validation token"


@app.route('/', methods=['POST'])
def handle_message():

    data = request.get_json()

    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    message_text = messaging_event["message"]["text"]
                    send_message_response(sender_id, message_text)

    return "ok"


def send_message(sender_id, message_text):
    """
    Sending response back to the user using facebook graph API
    """
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",

                      params={"access_token": PAT},

                      headers={"Content-Type": "application/json"},

                      data=json.dumps({
                          "recipient": {"id": sender_id},
                          "message": {"text": message_text}
                      }))


def send_message_response(sender_id, message_text):
    message_text_lower = str(message_text).lower()
    if message_text_lower == "help" or message_text_lower == "info" or message_text_lower == "aiuto":
        send_message(sender_id, "Messaggio di aiuto!")
        return None

    send_message(sender_id, message_text)


if __name__ == '__main__':
    app.run()
