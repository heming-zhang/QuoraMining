import requests 
from bs4 import BeautifulSoup 

def main(): 
    # 拿到登录页面 
    resp = requests.get('https://quora.com') 
    # 如果没有访问成功, 后面的代码就不需要执行了

    if resp.status_code != 200: 
        return

    # 访问成功以后, 获取网页响应返回的cookies的值, 以json(字典)格式返回. 
    cookies = resp.cookies.get_dict()
    
    # lxml的xpath的语法 -- //div[@class=''] 查找div下面的属性为有class的的标签 
    soup = BeautifulSoup(resp.text, 'lxml')
    
    # 在该页面的表单的隐藏域里面去获取hidden里面的值,包括token(跨站身份伪造) 
    # utf8_value = soup.select_one('form input[name=utf8]').attrs['value']
    # authenticity_token = soup.select_one('form input[name=authenticity_token]').attrs['value'] 
    
    # 表单登录数据 
    data = { 
        # 'utf8':utf8_value, 
        # 'authenticity_token':authenticity_token, 
        'login':'453315984@qq.com', 
        'password':'15hszhm961203' } 

    # requests通过post方法提交表单 
    resp = requests.post('https://quora.com/session', data=data, cookies=cookies) #files=files 上传文件的时候加上这一句 
    
    # 通过查看resp.text是否拿到了登录后的页面就可以确定是否登录成功! 
    # print(resp.text)
    soup = BeautifulSoup(resp.text, 'lxml')
    # print(soup.prettify())
    # get text from the tags with title
    print(soup.find('title').string)

if __name__ == '__main__': 
    main()
