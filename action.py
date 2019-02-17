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

class Action():

    def __init__(self, driver, topictitle, topicurl):
        self.driver = driver
        self.topictitle = topictitle
        self.topicurl = topicurl

    
    def choose_topic(self):
        driver = self.driver
        driver.get(self.topicurl)
        WaitPage(self.topictitle, driver).wait_page()

        print (driver.current_url)
        driver.save_screenshot("./pictures/quora_movies0.png")
        soup = BeautifulSoup(driver.page_source,'lxml')
        print(soup.find('title').string)
        
        return driver



