# -*- coding:utf8 -*-
import sys
import time
from bs4 import BeautifulSoup
import requests
import random
from agents import AGENTS_ALL
def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'html.parser')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list
def get_ip_listi(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'html.parser')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        proxy_list = []
        time2=  tds[9].text+":00"
        a2time = time.mktime(time.strptime(time2, '%y-%m-%d %H:%M:%S'))

        localtime = time.time()
        if  (localtime-a2time) <= 600:
            print str(localtime-a2time)
            urli = "http://www.aibang.com/beijing/qichezulin/"
            headersi = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
            }
            proxyi=('http://' + tds[1].text + ':' + tds[2].text)
            proxies = {'http': proxyi}

            try:
                req = requests.get(urli, headers=headersi, proxies=proxies, timeout=10)
                if req.status_code == 200:
                    ip_list.append(tds[1].text + ':' + tds[2].text)
            except requests.HTTPError as e:
                print("HTTPError!" + proxyi)
                # 如果url不存在会抛出ConnectionError错误，这个情况不做重试
            except requests.exceptions.ConnectionError as e:
                print("url不存在!"+proxyi)
            except requests.exceptions.ReadTimeout as e:
                print("ReadTimeout!" + proxyi)

    return ip_list
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    print proxy_list
    proxy_ip = random.choice(proxy_list)
    proxies = proxy_ip
    print proxy_ip
    return proxy_ip

def get_ip():
    reload(sys)
    sys.setdefaultencoding("utf-8")
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': random.choice(AGENTS_ALL)
    }
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    return proxies
if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    url = 'http://www.xicidaili.com/wt/'
    headers = {
    'User-Agent': random.choice(AGENTS_ALL)
    }
    ip_list = get_ip_listi(url, headers=headers)
    print  ip_list
