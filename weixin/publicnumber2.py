from selenium import webdriver
import time
import json
import requests
import re
import random

publicnumber=['四川大学飞扬俱乐部'] #设置爬取公众号

def weChat_login():
    
    post={}

    print("启动浏览器，打开微信公众号登录界面")
    driver = webdriver.Chrome()
    driver.get('https://mp.weixin.qq.com/')
    time.sleep(50)#手动登陆吧
    driver.get('https://mp.weixin.qq.com/')
    cookie_items = driver.get_cookies()

    for cookie_item in cookie_items:
        post[cookie_item['name']] = cookie_item['value']
    cookie_str = json.dumps(post)
    with open('cookie.txt', 'w+', encoding='utf-8') as f:
        f.write(cookie_str)
    print("cookies信息已保存到本地")

    
def get_content(query):
    url = 'https://mp.weixin.qq.com'
    header = {
        "HOST": "mp.weixin.qq.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
        }
    with open('cookie.txt', 'r', encoding='utf-8') as f:
        cookie = f.read()
    cookies = json.loads(cookie)

    response = requests.get(url=url, cookies=cookies)
    token = re.findall(r'token=(\d+)', str(response.url))[0]

    search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
    query_id = {
        'action': 'search_biz',
        'token' : token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'query': query,
        'begin': '0',
        'count': '5'
        }  
    search_response = requests.get(search_url, cookies=cookies, headers=header, params=query_id)
    lists = search_response.json().get('list')[0]
    fakeid = lists.get('fakeid')

    appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
    query_id_data = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'action': 'list_ex',
        'begin': '0',#不同页，此参数变化，变化规则为每页加5
        'count': '5',
        'query': '',
        'fakeid': fakeid,
        'type': '9'
        }
    appmsg_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
    max_num = appmsg_response.json().get('app_msg_cnt')
    num = int(int(max_num) / 5)
    begin = 0
    while num + 1 > 0 :
        query_id_data = {
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': '{}'.format(str(begin)),
            'count': '5',
            'query': '',
            'fakeid': fakeid,
            'type': '9'
            }
        print('正在翻页：--------------',begin)

        query_fakeid_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
        fakeid_list = query_fakeid_response.json().get('app_msg_list')
        for item in fakeid_list:
            content_link=item.get('link')
            content_title=item.get('title')
            fileName=query+'.txt'
            with open(fileName,'a',encoding='utf-8') as fh:
                fh.write(num)
                fh.write(content_title+":\n"+content_link+"\n")
        num -= 1
        begin = int(begin)
        begin+=5
        time.sleep(2)

if __name__=='__main__':
    try:
        weChat_login()
        for query in publicnumber:
            print("开始爬取公众号："+query)
            get_content(query)
            print("爬取完成")
    except Exception as e:
        print(str(e))