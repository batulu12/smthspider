__author__ = 'batulu'
import re, urllib, urllib2, requests, time, datetime, random
from bs4 import BeautifulSoup
def get_back_csdn_jifen():
    headers = {"User-Agent": "    Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
                "Host": "tianjin.jujiaonet.com",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'http://tianjin.jujiaonet.com/xfqxk/6/6_20151122338.html?from=singlemessage&isappinstalled=0',
                'X-Requested-With': 'XMLHttpRequest'
    }



f = open('c:\\code\\ip.txt')
iplist = f.readlines()
for ip in iplist:
    session = requests.session()
    if len(ip) ==0:
      pass
    print ip
    session.proxies = {'http': 'http://'+ip.strip('\r\n')}
    url = 'http://tianjin.jujiaonet.com/xfqxk/ip.php'

    #payload = {'cid': 6, 'ip': '122.96.59.106:80', 'tid':331}
    payload = {'cid': 6, 'ip': ip.strip('\r\n'), 'tid':331}

    try:
      req = session.post(url, data=payload, headers=headers)
    except:
      print 'error'

get_back_csdn_jifen()