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
from action import Action

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
            DataBase(crawledquestions, link, timestamp, 0, "0", "0", 0).insert_link()
        print(crawledquestions)

        return driver


    def extract_content(self):
        driver = self.driver
        questionlinks = DataBase(0, "0", "0", 0, "0", "0", 0).select_links() # all parsed links are here
        for links in questionlinks:
            print('----------------------------------------------')
            rank = int(links[0]) # into table
            questionlink = links[1] # into table
            timestamp = str(links[2]) # into table
            answertext = '' # into table
            view = 0
            print(rank)
            print(timestamp)
            driver.get(questionlink)
            questionlink = str(questionlink)
            print(questionlink)
            # use driver to parse html to extract content
            # insert question and answers into table movie
            soup = BeautifulSoup(driver.page_source,"lxml")
            title = soup.find("title").string
            if title == "Error 404 - Quora": continue
            question = str(title.strip(" - Quora"))
            print(question) # into table
            sign = soup.find("div", class_="prompt_title")
            if sign == None:
                answercount1 = soup.find("div", class_="answer_count")
                answercount2 = answercount1.get_text()
                answercount = int(answercount2.strip(" Answers"))
                pulltime = answercount * 50
                print(pulltime)
                pull_bar = Action(driver, "0", "0", pulltime)
                driver = pull_bar.pull_scrollbar()
                soup = BeautifulSoup(driver.page_source, "lxml")

                # find every answer block and extract text + answertime(substitute timestamp) + upvote + view
                blocks = soup.find_all('div', class_='Answer AnswerBase')
                for block in blocks:
                    answertext = ''
                    answertext1 = block.find_all('p', class_='ui_qtext_para u-ltr')
                    for answertext2 in answertext1:
                        answertext = answertext + " " + answertext2.get_text()
                    print(answertext) # into table
                    time = block.find('a', class_='answer_permalink')
                    timestamp = time.get_text()
                    views = block.find('span', class_='meta_num')
                    view0 = views.get_text()
                    kilo = view0.find('k')
                    if kilo == -1 : view = int(view0)
                    else:
                        view0 = view0.strip('k')
                        view = int(float(view0) * 1000)
                    DataBase(rank, questionlink, timestamp, answercount, question, answertext, view).insert_content()
            else:
                tag = sign.get_text()
                answercount = 0
                print(tag)
                print(answercount) # into table
                DataBase(rank, questionlink, timestamp, answercount, question, answertext, view).insert_content()

        return driver

