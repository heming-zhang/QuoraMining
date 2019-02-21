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
from pythondb import DataBase


class ExtractInfo():

    def __init__(self, driver):
        self.driver = driver
    

    def extract_questionlinks(self):
        # use bs4 to parse question links and questions
        crawledquestions = 0
        driver = self.driver
        soup = BeautifulSoup(driver.page_source,'lxml')
        link1 = soup.find_all('a', class_='question_link')
        timestamp1 = soup.find_all('span', class_='question_timestamp')
        for link2, timestamp2 in zip(link1, timestamp1):
            crawledquestions = crawledquestions + 1                                          
            link = 'https://www.quora.com' + link2.get('href')
            print(link)
            timestamp = timestamp2.get_text()
            print(timestamp)
            DataBase(crawledquestions, link, timestamp).insert_link()
        print(crawledquestions)

        return driver

    def extract_content(self):
        driver = self.driver
        questionlinks = DataBase(0, "0", "0").select_links()
        for links in questionlinks:
            print(links[1])
            driver.get(links[1])
            # use driver to parse html to extract content
            # insert question and answers into table movie
        
        return driver





