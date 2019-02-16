#coding:utf-8
import urllib.request
######
#爬虫v0.1 利用urlib 和 字符串内建函数
######
def getHtml(url):
    # 获取网页内容
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def content(html):
    # 内容分割的标签
    str0 = '<article class="article-content">'
    content = html.partition(str0)[2]
    str1 = '<div class="article-social">'
    content = content.partition(str1)[0]
    return content # 得到网页的内容
    
def title(content,beg = 0):
    # 匹配title
    # 思路是利用str.index()和序列的切片
    try:
        title_list = []
        while True:   
            num1 = content.index('】',beg)+3
            num2 = content.index('</p>',num1)
            title_list.append(content[num1:num2])
            beg = num2
        
    except ValueError:
         return title_list
         
def get_img(content,beg = 0):
    # 匹配图片的url
    # 思路是利用str.index()和序列的切片
    try:
        img_list = []
        while True:   
            src1 = content.index('http',beg)
            src2 = content.index('/></p>',src1)
            img_list.append(content[src1:src2])
            beg = src2
        
    except ValueError:
         return img_list

def many_img(data,beg = 0):
    #用于匹配多图中的url
    try:
        many_img_str = ''
        while True:
            src1 = data.index('http',beg)
            src2 = data.index(' /><br /> <img src=',src1)
            many_img_str += data[src1:src2]+'|' # 多个图片的url用"|"隔开
            beg = src2
    except ValueError:
        return many_img_str              
         
def data_out(title, img):
    #写入文本
    with open("C:/VS code files/Quora-Crawling/data.txt", "a+") as fo:
        fo.write('\n')
        for size in range(0, len(title)):
            # 判断img[size]中存在的是不是一个url
            if len(img[size]) > 70: 
                img[size] = many_img(img[size])# 调用many_img()方法
            fo.write(title[size]+'$'+img[size]+'\n')
        
   
                   
content = content(getHtml("http://bohaishibei.com/post/10475/"))
title = title(content)
img = get_img(content)
data_out(title, img)
# 实现了爬的单个页面的title和img的url并存入文本