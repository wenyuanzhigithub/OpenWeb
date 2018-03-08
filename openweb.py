 #!/usr/bin/env python
#-*- coding:UTF-8 -*-
import webbrowser
import time
from selenium import webdriver


mainurls = ['http://www.cnblogs.com/wenBlog/p/8302903.html']

#driver.maximize_window()  # 最大化浏览器
#driver.implicitly_wait(8) # 设置隐式时间等待
def flushEdge():
    for mainurl in mainurls:
        driver = webdriver.Edge()
        driver.implicitly_wait(8)
        driver.get(mainurl)
        time.sleep(2)
        driver.quit()

def flushChrome():
    print 4
    driver = webdriver.Chrome()
    # driver.maximize_window()  # 最大化浏览器  # 设置隐式时间等待
    for mainurl in mainurls:
        try:
            driver.implicitly_wait(8)
            driver.get(mainurl)
            time.sleep(2)
        except:
            print("explore bug")
            continue
    driver.quit()

def flushIE():
    print 1
    driver = webdriver.Ie()
    # driver.maximize_window()  # 最大化浏览器# driver.implicitly_wait(8) # 设置隐式时间等待
    for mainurl in mainurls:
        try:
            driver.implicitly_wait(8)
            driver.maximize_window()
            driver.get(mainurl)
            time.sleep(2)
        except:
            print("explore bug")
            continue
    driver.quit()

def flushFirefox():
    driver = webdriver.Firefox()
    # driver.maximize_window()  # 最大化浏览器
    # driver.implicitly_wait(8) # 设置隐式时间等待
    for mainurl in mainurls:
        # driver.implicitly_wait(8)
        # driver.maximize_window()
        driver.get(mainurl)
        time.sleep(2)
    driver.quit()
if __name__ == "__main__":
    while True:
        try:
            flushFirefox()
            flushIE()
            flushChrome()
            flushEdge()
            
        except  :
            print('程序问题继续执行')
            continue
