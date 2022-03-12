'''
Function:
    淘宝抢购脚本
Author:
    仰望·星空，K龙
微信公众号:
    红客突击队
'''
import time
from selenium import webdriver

def cookie_info():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("start-maximized")

    login_url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.201864-2.d1.5af911d9lhGWni&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F'
    driver = webdriver.Chrome(options=chrome_options)
    print("请尽快扫码！")
    driver.get(login_url)
    time.sleep(15)  # 预留了安全验证的时间
    driver.refresh()    # 刷新页面
    c = driver.get_cookies()
    sessions = dict()
    for cookie in c:
        sessions[cookie['name']] = cookie['value']
    #driver.quit()
    return sessions

