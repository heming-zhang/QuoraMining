#coding:utf-8
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
import urllib.request
from bs4 import BeautifulSoup
from quoralogin import Quoralogin
from action import Action

import pymysql 

def page_is_loaded(driver):
        return driver.find_element_by_tag_name("body") != None

def donwload_page(link):
    crawl = urllib.request.urlopen(link)
    # print(crawl.read())
    return crawl.read()

def extract_info():
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    initial_link = 'https://www.quora.com/If-you-were-to-make-a-movie-where-would-you-make-it'
    driver.get(initial_link)
#     html = str(html)
#     str1 = 'If you had an opportunity to star in a movie made after your favorite book, would you?'
#     print(html.find(str1))
    pull_bar = Action(driver, "0", "0", 1000)
    driver = pull_bar.pull_scrollbar()
    # use fast and powerful tool of lxml instead of html.parser
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # print(soup.prettify())
    # get text from the tags with title
    link1 = soup.find('div', class_='prompt_title')
    if link1 == None:
        answercount1 = soup.find('div', class_='answer_count')
        answercount = answercount1.get_text()
        print(answercount)
        pulltime = int(answercount.strip(' Answers')) * 50
        print(pulltime)

        question1 = soup.find('title').string
        print(question1)

        answertext = ''
        answertext1 = soup.find_all('p', class_='ui_qtext_para u-ltr')
        for answertext2 in answertext1:
            answertext = answertext + answertext2.get_text()
        print(answertext)

    else:
        tag = link1.get_text()
        print(tag)


#     for link2 in link1:
#         link = link2.get('href')
#         print(link)
#         text = link2.get_text()
#         print(text)


def select_record():
      # Open database connection
      db = pymysql.connect(user = "root", password = "root",
                           host = "127.0.0.1",
                           database = "quora" )
      # prepare a cursor object using cursor() method
      cursor = db.cursor()
      sql = """select * from movielinks1 order by rank"""
      cursor.execute(sql)
      movielinks = cursor.fetchall()
      db.close()
      print(movielinks)
      return movielinks


if __name__ == "__main__":
        # select_record()
        extract_info()




