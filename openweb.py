 #!/usr/bin/env python
#-*- coding:UTF-8 -*-
import webbrowser
import time
from selenium import webdriver


mainurls = ['http://www.cnblogs.com/wenBlog/p/8302903.html',
    'https://www.cnblogs.com/wenBlog/p/8297100.html',
                        'http://www.cnblogs.com/wenBlog/p/8193935.html',
                        'http://www.cnblogs.com/wenBlog/p/7833971.html',
                        'http://www.cnblogs.com/wenBlog/p/7685554.html',
                        'http://www.cnblogs.com/wenBlog/p/7474300.html',
                        'http://www.cnblogs.com/wenBlog/p/7459971.html',
                        'http://www.cnblogs.com/wenBlog/p/7451696.html',
                        'http://www.cnblogs.com/wenBlog/p/6888039.html'
                        ]

#driver.maximize_window()  # 最大化浏览器
#driver.implicitly_wait(8) # 设置隐式时间等待
def flushEdge():
    for mainurl in mainurls:
        time.sleep(60)
        driver = webdriver.Edge()
        driver.implicitly_wait(8)
        driver.get(mainurl)

        driver.quit()

def flushChrome():
    driver = webdriver.Chrome()
    # driver.maximize_window()  # 最大化浏览器
    driver.implicitly_wait(8)  # 设置隐式时间等待
    for mainurl in mainurls:
        time.sleep(60)
        driver.get(mainurl)

    driver.quit()

def flushIE():
    driver = webdriver.Ie()
    # driver.maximize_window()  # 最大化浏览器# driver.implicitly_wait(8) # 设置隐式时间等待
    for mainurl in mainurls:
        time.sleep(60)
        driver.implicitly_wait(8)
        driver.maximize_window()
        driver.get(mainurl)

    driver.quit()

def flushFirefox():
    driver = webdriver.Firefox()
    # driver.maximize_window()  # 最大化浏览器
    # driver.implicitly_wait(8) # 设置隐式时间等待
    for mainurl in mainurls:
        # driver.implicitly_wait(8)
        # driver.maximize_window()
        time.sleep(60)
        driver.get(mainurl)

    driver.quit()
if __name__ == "__main__":
    while True:
        try:
            flushFirefox()
            time.sleep(60)
            flushIE()
            time.sleep(60)
            flushChrome()
            time.sleep(60)
            flushEdge()
            time.sleep(60)
        except  :
            print('程序问题继续执行')
            continue
