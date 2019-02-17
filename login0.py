# -*- coding: utf-8 -*-
import pdb
def debug_signal_handler(signal, frame):
    pdb.set_trace()

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

def page_is_loaded(driver):
        return driver.find_element_by_tag_name("body") != None

def donwload_page(link):
    crawl = urllib.request.urlopen(link)
    # print(crawl.read())
    return crawl.read()

def quora_login():
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    driver.get("https://www.quora.com/")
    wait = ui.WebDriverWait(driver, 10)
    # wait for 10 seconds before showing exception
    wait.until(page_is_loaded)
    email_field = driver.find_element_by_css_selector("input[placeholder=Email]") # メールアドレス
    email_field.send_keys("453315984@qq.com")
    password_field = driver.find_element_by_css_selector("input[placeholder=Password]") # パスワード
    password_field.send_keys("ccnu15zhm4533")
    # password_field.send_keys(Keys.RETURN)
    
    driver.find_element_by_xpath("//input[@class='submit_button ignore_interaction']").click()

    driver.save_screenshot("quora_home0.png")
    print (driver.current_url)

    soup = BeautifulSoup(driver.page_source,'lxml')
    print(soup.find('title').string)

if __name__ == "__main__":
    quora_login()


# <input class="submit_button ignore_interaction" type="submit" value="Login" tabindex="4" data-group="js-editable" w2cid="wQZ1KLty18" id="__w2_wQZ1KLty18_submit_button">