# import os
# import telebot
# TOKEN = "8143686052:AAFz7AYSIkgT5-MF_1eUvgWy62EvudUxfPk"
# bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, 'Привет этот бот для фильмов которые вы посмотрели или хотите посмотреть')

# @bot.message_handler(func=lambda mgs: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

# def __init__(self, name):
#     self.name = name

# bot.infinity_polling()

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager # type: ignore


USERNAME = "admin"
PASSWORD = "admin"
URL = f"https://{USERNAME}:{PASSWORD}@the-internet.herokuapp.com/basic_auth"

class TestBasicAuthLogin(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument("--headless")  
        options.add_argument("--disable-gpu") 
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
    
    def test_basic_auth_page(self):
        self.driver.get(URL)
        success_message = self.driver.find_element(By.TAG_NAME, "p").text
        self.assertIn("Congratulations!", success_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
