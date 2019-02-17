# -*- coding: utf-8 -*-
import pdb
def debug_signal_handler(signal, frame):
    pdb.set_trace()

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from login import Login
from wait import WaitPage
from action import Action

def crawl():
    homeurl = "https://www.quora.com/?prevent_redirect=1" # to use English as first language
    email = "3181276187@qq.com"
    password = "15hszhm961203"
    topictitle = "Movies - Quora"
    topicurl = "https://www.quora.com/topic/Movies"
    quora_login = Login(homeurl, email, password)
    driver = quora_login.login()
    choose_movies = Action(driver, topictitle, topicurl)
    driver = choose_movies.choose_topic()

if __name__ == "__main__":
    crawl()