# -*- coding:utf8 -*-
import multiprocessing
import threading as thd
import time
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import pymssql
import os
import sys
import ProxyIP
import random
from agents import AGENTS_ALL
if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # print '\xa0'.decode('utf-8')
    for i in range(10000):
        time.sleep(60)


        proips=['36.26.254.44:808']
        print proips
        for proip in proips:
            UserAgent = random.choice(AGENTS_ALL)
            print UserAgent
            header = {
                'User-Agent': UserAgent
            }
            proxies={'https': proip }
            mainurls = ['https://www.cnblogs.com/wenBlog/p/8297100.html',
                       
                        'http://www.cnblogs.com/wenBlog/p/7833971.html',
                        'http://www.cnblogs.com/wenBlog/p/7685554.html',
                        'http://www.cnblogs.com/wenBlog/p/7474300.html',
                        'http://www.cnblogs.com/wenBlog/p/7459971.html',
                        'http://www.cnblogs.com/wenBlog/p/7451696.html',
                        'http://www.cnblogs.com/wenBlog/p/6888039.html'
                        ]
            for mainurl in mainurls:
                try:

                    req = urllib2.Request(mainurl, headers=header)
                    response = urllib2.urlopen(req)
                    # req = requests.get(mainurl, headers=header, proxies=proxies, timeout=30)
                    # print req.status_code,mainurl,proxies
                except requests.HTTPError as e:
                    print("HTTPError!" + proip)
                # 如果url不存在会抛出ConnectionError错误，这个情况不做重试
                except requests.exceptions.ConnectionError as e:
                    print(e.message)
                except requests.exceptions.ReadTimeout as e:
                    print("ReadTimeout!" + proip)
                #web_data.encoding = "gb2312"

