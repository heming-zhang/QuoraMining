# -*- coding: utf-8 -*-
import pdb
def debug_signal_handler(signal, frame):
    pdb.set_trace()

import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    pulltime = 3000
    quora_login = Login(homeurl, email, password)
    driver = quora_login.login()
    choose_movies = Action(driver, topictitle, topicurl, pulltime)
    driver = choose_movies.choose_topic()

    # pull the scrollTop to end
    # js="var q=document.documentElement.scrollTop=10000"
    # driver.execute_script(js)
    # # driver.implicitly_wait(10)
    # # wait = ui.WebDriverWait(driver, 10)
    # # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pricerow")))
    # driver.save_screenshot("./pictures/quora_movies1.png")

    pull_bar = Action(driver, topictitle, topicurl, pulltime)
    driver = pull_bar.pull_scrollbar()

if __name__ == "__main__":
    crawl()