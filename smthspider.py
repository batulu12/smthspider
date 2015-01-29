# -*- coding: UTF-8 -*-
import re, urllib, urllib2, requests, time, datetime, random
from bs4 import BeautifulSoup
import json

board_dict = {}

headers = { "User-Agent": " Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
            "Host": "www.newsmth.net",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Cookie":"Hm_lvt_9c7f4d9b7c00cb5aba2c637c64a41567=1421654832,1421728515,1421827791,1421982989; tma=88525828.4893887.1420332716520.1421901287602.1421982989863.14; tmd=91.88525828.4893887.1420332716520.; nforum-left=00100; left-index=00000000000; main[UTMPUSERID]=batulu12; main[UTMPKEY]=41480197; main[UTMPNUM]=16797; Hm_lpvt_9c7f4d9b7c00cb5aba2c637c64a41567=1422001897; main[PASSWORD]=o%257E%257Fi%252C%250D%2528%257C%257D%2504U%255C%2540uKLB%251E%2529%251D%250A%2523%2509%2508; main[XWJOKE]=hoho; bfd_session_id=bfd_g=b56c782bcb75035d00006ef20011174a54a88f0d; tmc=1.88525828.74332260.1421986459313.1421986459313.1421986459313",
            "Referer":"http://www.newsmth.net/nForum/",
            "X-Requested-With":"XMLHttpRequest"
}
def board(page_url,boardname):
    r = requests.get(page_url,headers=headers)
    soup = BeautifulSoup(r.text)
    #print soup.find_all("div", class_="b-head corner").get("span",class_="n-left").text
    result_list = soup("span", class_="n-left")
    p = re.compile(u"[\u4e00-\u9fa5]+(\d+)[\u4e00-\u9fa5]+")
    str2 = str(result_list).decode('utf8')
    res = p.findall(str2)
    if len(res) > 1:
      now = res[0].encode('utf-8')
      max = res[1].encode('utf-8')
      print boardname + "：当前在线人数 "+now+"人，最高在线 "+max+"人"
      board_dict[boardname] = int(now)
    #print soup2.contents[0].encode('utf-8')

def smthspider(page_url,boardname):
    session = requests.session()
    session.proxies = {'http': 'http://218.206.83.89:80',
                       'http': 'http://36.250.74.88:80'}
    try:
        r = session.get(page_url,headers=headers,timeout = 1)
        time.sleep(random.randint(1, 2))
    except Exception , e:
        print e
        return
    if page_url.find('sec') !=-1 and len(r.json()) >0:
      soup = BeautifulSoup(r.json()[0]["t"])
    else:
       #print page_url
       board(page_url,boardname)
       return

    for item in r.json():
        soup =  BeautifulSoup(item["t"])
        uri = soup.a.get("href")
        boardname = soup.a.contents[0].encode('utf-8')
        if uri.split('/')[2] == 'section':
            #print soup.a.contents[0].encode('utf-8')
            nexturi = 'http://www.newsmth.net/nForum/slist.json?uid=guest&root='+'sec-'+uri.split('/')[3]
            smthspider(nexturi,boardname)
        else:
            #print soup.a.contents[0].encode('utf-8')
            nexturi = 'http://www.newsmth.net'+uri
            smthspider(nexturi,boardname)
    #print soup.a
    #print soup.a.get("href")
    #print soup.a.contents[0].encode('utf-8')

smthspider('http://www.newsmth.net/nForum/slist.json?uid=guest&root=list-section','board')
#board_dict = {'w':12,'e':3,'d':15}
#board_dict['r'] = int('127')
board_list = sorted(board_dict.iteritems(),key=lambda d:d[1],reverse = True)
#print board_list
for item in board_list:
    print "%s %d" % (item[0],item[1])
#smthspider('http://www.newsmth.net/nForum/slist.json?uid=guest&root=sec-0')