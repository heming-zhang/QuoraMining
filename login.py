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
from wait import WaitPage

class Login():

    def __init__(self, homeurl, email, password):
        self.homeurl = homeurl
        self.email = email
        self.password = password


    def login(self):
        # TODO: use webdriver to open login into Quora
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        driver.get(self.homeurl)
        WaitPage("None", driver).wait_common_page()
        email_field = driver.find_element_by_xpath("//input[@placeholder='Email']") # メールアドレス
        email_field.send_keys(self.email)
        password_field = driver.find_element_by_xpath("//input[@placeholder='Password']") # パスワード
        password_field.send_keys(self.password)
        # click submit button to enter into quora
        # driver.find_element_by_xpath("//input[@class='submit_button ignore_interaction']").click()
        password_field.send_keys(Keys.RETURN)
        WaitPage("Home - Quora", driver).wait_page()

        print (driver.current_url)
        driver.save_screenshot("./pictures/quora_home0.png")
        soup = BeautifulSoup(driver.page_source,'lxml')
        print(soup.find('title').string)

        return driver
