import asyncio
import json
import requests
import time
import requests




APIKEY = '243c5b58aa7db32f8a20fdb6512cb4a3'


def one_get():
    url = 'http://api.tianapi.com/txapi/one/index?key=' + APIKEY
    try:
        req = requests.get(url)
        text = req.text
        text = json.loads(text)
        print(text)
        text = text['newslist'][0]['word']  # 正文内容
        print(text)
    except:
        pass

async def one_get():
    """
    获取one 一个接口
    :return:
    """
    url = 'http://api.tianapi.com/txapi/one/index?key=' + APIKEY
    try:
        req = requests.get(url)
        text = req.text
        text = json.loads(text)
        print(text)
        text = text['newslist'][0]['word']  # 正文内容
        # print(text)
        return text
    except:
        return 'one一个调用失败'



async def dyvideohot():
    """
    抖音话题榜
    :return:返回数据字典 title shareurl
    """
    url = 'http://api.tianapi.com/txapi/dyvideohot/index?key=' + APIKEY
    try:
        req = requests.get(url)
        text = req.text
        text = json.loads(text)
        # print(text)
        text = text['newslist']  # 正文内容
        # print(text)
        ar = []
        for li in text:
            #  于是明白了,因为每次添加的都是同一个内存到list中去了,dict_1每次写入的时候改变了内存中的value,但是地址不变,即是,创建了一次内存空间,只会不断的改变value了.完善方法:每次遍历时候创建一个新的dic.
            dic = {'title': li['title'], 'shareurl': li['shareurl'],'coverurl':li['coverurl']}
            ar.append(dic)
        return ar
    except:
        pass

import urllib.parse

def urlParse(str:str):
    """
    视频连接转短连接
    :param s:
    :return:
    """
    # fixed_type ='&type=dwzmk&geetest_challenge=0777ac79ac93e2170a1af4066b5308e7d4&geetest_validate=5dfa4f2658e35efa981ed5e1e190496a&geetest_seccode=5dfa4f2658e35efa981ed5e1e190496a%7Cjordan'
    # result = str.replace(':','%3A').replace('/','%2F').replace('?','%3F').replace('=','%3D').replace('&','%26')
    # sss = 'https://www.iesdouyin.com/share/video/6917929247516527875/?region=&mid=6917929343385684750&u_code=0&titleType=title&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1'

    headers = {
        'Host':'www.toer2.com',
        'Connection':'keep-alive',
        'Content-Length':'481',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko)',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin':'https://www.toer2.com',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Dest':'empty',
        'Referer':'https://www.toer2.com/DuanUrl.html',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9'

    }
    url = "https://www.toer2.com/ajax.php"
    form_data ={
        'act':'DuanUrl',
        'link':str,
        'type':'suoim',
        'geetest_challenge':'0777ac79ac93e2170a1af4066b5308e7d4',
        'geetest_validate':'5dfa4f2658e35efa981ed5e1e190496a',
        'geetest_seccode':'5dfa4f2658e35efa981ed5e1e190496a%7Cjordan',
    }
    cookie = {
        '__guid':'170626598.188499921190822050.1625046704778.5623',
        'UM_distinctid':'17a5c54e3c892b-0acd06dcb3e58-3e604809-1fa400-17a5c54e3c935a',
        'PHPSESSID':'uq065mfj94tpjqfplstpq6m5r6',
        'night':'0',
        'USERID': '86e3234d2256081837e9989f0675e6d0',
        'CNZZDATA1279964073':'822574188-1625576197-%7C1625576197',
        'monitor_count':'6'
    }
    response = requests.post(url, data=form_data, headers=headers,cookies = cookie).text.replace('\\','')
    # response = requests.post(url, data=form_data, headers=headers,cookies = cookie).text

    return json.loads(response)['msg']

async def getQqPhoto(qq):
    """
    获取qq头像 返回数据为二进制数据
    :param qq:
    :return:
    """
    url = f'http://q1.qlogo.cn/g?b=qq&nk={qq}&s=100'
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    resp = requests.get(url,headers=headers)
    # with open('photo.jpg','wb') as f:
    #     f.write(resp.content)

    return resp.content


if __name__ == '__main__':

     # a = 'https://www.iesdouyin.com/share/video/6928953754343574787/?region=&mid=6928953805157468935&u_code=0&titleType=title&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1'
     # urlParse(a)

    # ar = asyncio.run(dyvideohot())
    # str = ""
    # print(ar)
    # for link in ar:
    #     title = link['title']
    #     shareurl = urlParse(link['shareurl'])
    #     print('shareurl:',shareurl)
    #     coverurl = urlParse(link['coverurl'])
    #     print('coverurl:',coverurl)
    #
    #     str = str+f"""
    #             [CQ:share,title=抖音热榜,content={title},image={coverurl},url={shareurl}]
    #             """
    # print(str)

    asyncio.run(getQqPhoto(378992731))