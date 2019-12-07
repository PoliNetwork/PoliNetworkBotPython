from time import sleep

import autoit as autoit
import selenium
from selenium import webdriver

from functions.instagram import instagram_config

driver = None


def login():
    try:
        login_button = driver.find_element_by_xpath("//button[contains(text(),'Log In')]")
        login_button.click()
    except Exception as e:
        try:
            login_button = driver.find_element_by_xpath("//button[contains(text(),'Accedi')]")
            login_button.click()
        except Exception as e:
            pass

    sleep(2)
    username_input = driver.find_element_by_xpath("//input[@name='username']")
    username_input.send_keys(instagram_config.username)
    password_input = driver.find_element_by_xpath("//input[@name='password']")
    password_input.send_keys(instagram_config.password)
    password_input.submit()


def close_reactivated():
    sleep(1)
    try:
        not_now_btn = driver.find_element_by_xpath("//a[contains(text(),'Not Now')]")
        not_now_btn.click()
    except:
        try:
            not_now_btn = driver.find_element_by_xpath("//a[contains(text(),'Non ora')]")
            not_now_btn.click()
        except:
            try:
                not_now_btn = driver.find_element_by_xpath("//button[contains(text(),'Non ora')]")
                not_now_btn.click()
            except:
                try:
                    close_noti_btn = driver.find_element_by_xpath("//button[contains(text(),'Annulla')]")
                    close_noti_btn.click()
                except:
                    try:
                        close_noti_btn = driver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
                        close_noti_btn.click()
                    except:
                        pass


def send_photo(image_path, caption):
    global driver

    image_path = "C:\\Users\\Arme\\Desktop\\41DPbW0fPzL.jpg"
    caption = "Test caption"  # Enter the caption

    try:
        mobile_emulation = {"deviceName": "Pixel 2"}
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("mobileEmulation", mobile_emulation)

        driver = webdriver.Chrome(executable_path="C:\\Users\\Arme\\Desktop\\chromedriver.exe",
                                  options=opts)  # you must enter the path to your driver

    except Exception as e:
        pass

    sleep(2)

    main_url = "https://www.instagram.com"
    driver.get(main_url)

    sleep(4)

    login()

    sleep(4)

    close_reactivated()
    close_reactivated()

    sleep(3)

    close_reactivated()

    new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']").click()
    sleep(1.5)
    autoit.win_active("Open")
    sleep(2)
    autoit.control_send("Open", "Edit1", image_path)
    sleep(1.5)
    autoit.control_send("Open", "Edit1", "{ENTER}")

    sleep(2)

    try:
        next_btn = driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
    except:
        next_btn = driver.find_element_by_xpath("//button[contains(text(),'Avanti')]").click()

    sleep(1.5)

    caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
    caption_field.send_keys(caption)

    try:
        share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()
    except:
        share_btn = driver.find_element_by_xpath("//button[contains(text(),'Condividi')]").click()

    sleep(25)

    driver.close()


send_photo("", "")
