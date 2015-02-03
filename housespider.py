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

def smthspider(page_url):
    session = requests.session()
    #session.proxies = {'http': 'http://218.206.83.89:80'}
    try:
        r = session.get(page_url,headers=headers,timeout = 3)
        #print r.text
        p = re.compile('(\d+-\d+-\d+)|(\d+:\d+:\d+)')
        soup = BeautifulSoup(r.text)
        for ac in soup.find_all('a'):
            time_list = p.findall(ac.get_text())
            if len(time_list) > 0:
                print time_list[0]


        time.sleep(random.randint(1, 2))
    except Exception , e:
        print e
        return

smthspider('http://www.newsmth.net/nForum/board/RealEstate?ajax')