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

def page_is_loaded(driver):
        return driver.find_element_by_tag_name("body") != None

class WaitPage():

    def __init__(self, titlename, driver):
        self.titlename = titlename
        self.driver = driver


    def wait_common_page(self):
        driver = self.driver
        wait = ui.WebDriverWait(driver, 10)
        wait.until(page_is_loaded)

    def wait_page(self):
        driver = self.driver
        wait = ui.WebDriverWait(driver, 10)
        wait.until(EC.title_contains(self.titlename))





