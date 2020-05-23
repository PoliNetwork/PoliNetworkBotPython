
from functions.instagram import instagram_config
from functions.instagram.InstagramAPI import PyInstagramAPI

InstagramAPI = PyInstagramAPI(username= instagram_config.username,
                              password=instagram_config.password,
                              debug=False, IGDataPath='/home/arme')
InstagramAPI.login()  # login

photo_path = "/home/arme/Pictures/a.jpg"
caption = "Sample photo"

try:
    InstagramAPI.uploadPhoto(photo=photo_path, caption=caption)
except Exception as e:
    pass
