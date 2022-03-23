import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def cookie_info():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--disable-gpu")
    firefox_options.set_preference("dom.webdriver.enabled", False)
    service = Service("driver/geckodriver")
    driver = webdriver.Firefox(service=service,options=firefox_options)
    login_url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua.201864-2.d1.5af911d9lhGWni&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F'
    driver.maximize_window()
    print("请尽快扫码！")
    driver.get(login_url)
    script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
    driver.execute_script(script)
    time.sleep(20)  # 预留了安全验证的时间
    driver.refresh()    # 刷新页面
    c = driver.get_cookies()
    sessions = dict()
    for cookie in c:
        sessions[cookie['name']] = cookie['value']
    driver.quit()
    return sessions

