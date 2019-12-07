from InstagramAPI import InstagramAPI

from functions.instagram import instagram_config

InstagramAPI = InstagramAPI(instagram_config.username, instagram_config.password)
InstagramAPI.login()  # login

photo_path = "C:\\Users\\Arme\\Desktop\\bianco.jpg"
caption = "Sample photo"

try:
    InstagramAPI.uploadPhoto(photo=photo_path, caption=caption)
except Exception as e:
    pass
