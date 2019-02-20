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


def donwload_page(link):
    crawl = urllib.request.urlopen(link)
    # print(crawl.read())
    return crawl.read()


def quora_login():
    # TODO: use webdriver to login into quora
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    driver.get("https://www.quora.com/?prevent_redirect=1") #  to use English as the first language
    # wait for 10 seconds before showing exception
    wait = ui.WebDriverWait(driver, 10)
    wait.until(page_is_loaded)
    email_field = driver.find_element_by_xpath("//input[@placeholder='Email']") # メールアドレス
    email_field.send_keys("3181276187@qq.com")
    password_field = driver.find_element_by_xpath("//input[@placeholder='Password']") # パスワード
    password_field.send_keys("15hszhm961203")
    # click submit button to enter into quora
    driver.find_element_by_xpath("//input[@class='submit_button ignore_interaction']").click()
    # password_field.send_keys(Keys.RETURN)
    wait = ui.WebDriverWait(driver, 10)
    wait.until(EC.title_contains('Home - Quora'))
    print (driver.current_url)
    driver.save_screenshot("quora_home0.png")
    soup = BeautifulSoup(driver.page_source,'lxml')
    print(soup.find('title').string)
    return driver


def quora_crawl():
    # crawl Q&A from topic of movies
    driver = quora_login()
    driver.get("https://www.quora.com/topic/Movies")
    wait = ui.WebDriverWait(driver, 10)
    wait.until(EC.title_contains('Movies - Quora'))
    print (driver.current_url)
    driver.save_screenshot("quora_movies0.png")
    soup = BeautifulSoup(driver.page_source,'lxml')
    print(soup.find('title').string)


if __name__ == "__main__":
    quora_crawl()


