from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

class twitterbot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefix() #opens up link bot.get(url)

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)

chiz = twitterbot('ur_UserName', 'ur_Password')
chiz.login()            