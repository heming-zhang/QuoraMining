#coding:utf-8
import pdb
def debug_signal_handler(signal, frame):
    pdb.set_trace()

import urllib.request
from bs4 import BeautifulSoup
from quoralogin import Quoralogin

import pymysql 

def donwload_page(link):
    crawl = urllib.request.urlopen(link)
    # print(crawl.read())
    return crawl.read()

def extract_info():
    initial_link = 'http://www.baidu.com'
    html = donwload_page(initial_link)
    # use fast and powerful tool of lxml instead of html.parser
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    # get text from the tags with title
    link1 = soup.find_all('a')
    for link2 in link1:
        link = link2.get('href')
        print(link)
        text = link2.get_text()
        print(text)

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
        select_record()
        # extract_info()




