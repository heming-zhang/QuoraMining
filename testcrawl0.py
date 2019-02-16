#coding:utf-8
import urllib.request

def run_demo():
    crawl = urllib.request.urlopen('http://www.baidu.com')
    print(crawl.read())

if __name__=='__main__':
    run_demo()