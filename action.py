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

    def __init__(self, driver, topictitle, topicurl, pulltime):
        self.driver = driver
        self.topictitle = topictitle
        self.topicurl = topicurl
        self.pulltime = pulltime

    
    def choose_topic(self):
        driver = self.driver
        driver.get(self.topicurl)
        WaitPage(self.topictitle, driver).wait_page()

        print (driver.current_url)
        driver.save_screenshot("./pictures/quora_movies0.png")
        soup = BeautifulSoup(driver.page_source,'lxml')
        print(soup.find('title').string)

        return driver


    def pull_scrollbar(self):
        driver = self.driver
        for i in range(1, self.pulltime):
            # tune variable scrollTop to update the length of pulling action
            js="var q=document.documentElement.scrollTop=200000000"
            driver.execute_script(js)
            # wait function need more exactitude
            WaitPage("None", driver).wait_common_page()
        driver.save_screenshot("./pictures/quora_movies2.png")
        return driver



