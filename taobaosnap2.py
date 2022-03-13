# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Function:
    淘宝抢购脚本
Author:
    SWHL，仰望·星空，K龙
微信公众号:
    红客突击队
'''
from selenium import webdriver
import datetime
import time
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option("useAutomationExtension", False)

url = 'https://www.taobao.com'
browser = webdriver.Chrome(options=chrome_options)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
        """,
    })
browser.get(url)
browser.maximize_window()

browser.find_element(By.LINK_TEXT,"请登录").click()

print("请扫码登录")
time.sleep(10)
browser.get("https://cart.taobao.com/cart.htm")
time.sleep(3)

# 是否全选购物车
while True:
    try:
        if browser.find_element(By.XPATH,'//*[@id="J_SelectAll1"]/div/label'):
            browser.find_element(By.XPATH,'//*[@id="J_SelectAll1"]/div/label').click()
            break
    except:
        print(f"找不到购买按钮")


times = "2022-03-11 19:00:00.00000000"

while True:
    #获取电脑现在的时间,                      year month day
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    # 对比时间，时间到的话就点击结算
    print(now)

    #判断是不是到了秒杀时间?
    if now > times:
        # 点击结算按钮
        while True:
            try:
                if browser.find_element(By.LINK_TEXT,"结 算"):
                    print("here")
                    browser.find_element(By.LINK_TEXT,"结 算").click()
                    print(f"锁定商品,结算成功")
                    break
            except:
                pass
        # 点击提交订单按钮
        while True:
            try:
                if browser.find_element(By.XPATH,'//*[@id="submitOrderPC_1"]/div/a[2]'):
                    browser.find_element(By.XPATH,'//*[@id="submitOrderPC_1"]/div/a[2]').click()
                    print(f"抢购成功，请尽快付款")
                    break
            except:
                print(f"已抢到商品,请尽快支付")
                pass
        time.sleep(0.01)