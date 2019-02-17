# -*- coding: utf-8 -*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

def page_is_loaded(self, driver):
        return driver.find_element_by_tag_name("body") != None

class Quoralogin():
    def __init__(self):
        self.url = "https://www.quora.com/"

    def quora_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        driver.get("https://www.quora.com/")
        wait = ui.WebDriverWait(driver, 10)
        # wait for 10 seconds before showing exception
        wait.until(page_is_loaded)
        email_field = driver.find_element_by_css_selector("input[placeholder=Email]") # メールアドレス
        email_field.send_keys("453315984@qq.com")
        password_field = driver.find_element_by_css_selector("input[placeholder=Password]") # パスワード
        password_field.send_keys("15hszhm961203")
        password_field.send_keys(Keys.RETURN)

