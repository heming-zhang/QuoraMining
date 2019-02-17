#coding:utf-8
import pdb
def debug_signal_handler(signal, frame):
    pdb.set_trace()

import urllib.request
from bs4 import BeautifulSoup
from quoralogin import Quoralogin

def donwload_page(link):
    crawl = urllib.request.urlopen(link)
    # print(crawl.read())
    return crawl.read()

def extract_info():
    initial_link = 'http://www.quora.com'
    html = donwload_page(initial_link)
    # use fast and powerful tool of lxml instead of html.parser
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    # get text from the tags with title
    print(soup.find('title').string)

if __name__ == "__main__":
    extract_info()



