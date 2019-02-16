#coding:utf-8
import pdb
def debug_signal_handler(signal, frame):
    pdb.set_trace()


from bs4 import BeautifulSoup
import urllib.request

def donwload_page(link):
    crawl = urllib.request.urlopen(link)
    # print(crawl.read())
    return crawl.read()

def extract_text():
    html = donwload_page('http://www.google.com')
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    print(soup.find('title').string)

if __name__ == "__main__":
    extract_text()



