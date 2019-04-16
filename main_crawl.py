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
from pythondb import DataBase
from extract import ExtractInfo

def create_db():
    DataBase(0, '0', '0', 0, '0', '0', 0).create_link_database()
    DataBase(0, '0', '0', 0, '0', '0', 0).create_final_database()


def crawl_links():
    homeurl = "https://www.quora.com/?prevent_redirect=1" # to use English as first language
    email = "3181276187@qq.com"
    password = "15hszhm961203"
    # topictitle = "All Questions on Movies - Quora" 
    topictitle = "All Questions on Film and Television - Quora"
    # topictitle = "All Questions on TV Sitcoms - Quora"
    # topictitle = "All Questions on Television Series - Quora"
    # topicurl = "https://www.quora.com/topic/Movies/all_questions"
    topicurl = "https://www.quora.com/topic/Film-and-Television/all_questions"
    # topicurl = "https://www.quora.com/topic/TV-Sitcoms/all_questions"
    # topicurl = "https://www.quora.com/topic/Television-Series/all_questions"
    pulltime = 15000
    quora_login = Login(homeurl, email, password)
    driver = quora_login.login()
    choose_movies = Action(driver, topictitle, topicurl, pulltime)
    driver = choose_movies.choose_topic()
    pull_bar = Action(driver, topictitle, topicurl, pulltime)
    driver = pull_bar.pull_scrollbar()
    extract_links = ExtractInfo(driver)
    driver = extract_links.extract_questionlinks()
    return driver


def crawl_content():
    # driver = webdriver.Firefox(executable_path='./geckodriver-v0.24.0-win64/geckodriver.exe') 
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    extract_text = ExtractInfo(driver)
    driver = extract_text.extract_content()
    return driver


if __name__ == "__main__":
    # create_db()
    # crawl_links()
    crawl_content()

