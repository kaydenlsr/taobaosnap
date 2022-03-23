'''
Function:
    淘宝抢购脚本
Author:
    仰望·星空，K龙，Charles
微信公众号:
    红客突击队
邮箱：
    hsc_2019@163.com
'''
import requests
import re
import time
import datetime
import json
import urllib
import pyttsx3
import sys
from selenium import webdriver
from prettytable import PrettyTable
from requests.packages.urllib3 import disable_warnings
from requests.cookies import cookiejar_from_dict

def help_info():
    help = """
usage : python {0}
    --time        Buying time and format: 00:00:00:00000000.
    --interval    Buying time interval.
    --l           Buying frequency.
""".format(sys.argv[0])
    print(help)

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

'''淘宝抢购脚本'''
class TaobaoSnap():
    def __init__(self, trybuy_interval=None, Seconds_kill_time=None, number=None):
        self.session = requests.Session()
        self.cookie = cookie_info()
        self.session.cookies = cookiejar_from_dict(self.cookie)
        self.trybuy_interval = float(trybuy_interval)
        self.Seconds_kill_time = Seconds_kill_time
        self.number = int(number)
    def run_info(self):
        # 获得购物车信息
        cart_infos, user_id = self.buycartinfo()
        # 解析购物车信息
        if not cart_infos['success']:
            raise RuntimeError('获取购物车信息失败, 请尝试删除cookie缓存文件后重新扫码登录')
        if len(cart_infos['list']) == 0:
            raise RuntimeError('购物车是空的, 请在购物车中添加需要抢购的商品')
        good_infos = {}
        for idx, item in enumerate(cart_infos['list']):
            good_info = {
                'title': item['bundles'][0]['orders'][0]['title'],
                'cart_id': item['bundles'][0]['orders'][0]['cartId'],
                'cart_params': item['bundles'][0]['orders'][0]['cartActiveInfo']['cartBcParams'],
                'item_id': item['bundles'][0]['orders'][0]['itemId'],
                'sku_id': item['bundles'][0]['orders'][0]['skuId'],
                'seller_id': item['bundles'][0]['orders'][0]['sellerId'],
                'to_buy_info': item['bundles'][0]['orders'][0]['toBuyInfo'],
            }
            good_infos[str(idx)] = good_info
        # 打印并选择想要抢购的商品信息
        title, items = ['id', 'title'], []
        for key, value in good_infos.items():
            items.append([key, value['title']])
        self.printTable(title, items)
        good_id = input('请选择想要抢购的商品编号(例如"0"): ')
        assert good_id in good_infos, '输入的商品编号有误'
        # 根据选择尝试购买商品
        print(f'[{time.strftime("%H:%M:%S", time.localtime())} INFO]: 正在尝试抢购商品***{good_infos[good_id]["title"]}***')
        #time_seckill = "2022-00-00 00:00:00:00000000"
        # 对比时间，时间到的话就点击结算
        while True:
            r1 = requests.get(url='http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp', headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'})
            x = eval(r1.text)
            timeNum = int(x['data']['t'])
            ret = datetime.datetime.fromtimestamp(timeNum / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
            if ret > self.Seconds_kill_time:
                for i in range(self.number):
                    try:
                        is_success = self.buygood(good_infos[good_id], user_id)
                    except Exception as err:
                        crawler = re.findall("'NoneType' object has no attribute 'group'",str(err))
                        if "'NoneType' object has no attribute 'group'" in crawler:
                            print("已触发反爬虫机制，请稍后尝试! 错误信息如下：\n{0}\n".format(err))
                            # is_success = False
                            break
                        else:
                            print(f'[{time.strftime("%H:%M:%S", time.localtime())} INFO]: 抢购失败, 错误信息如下: \n{err}\n将在{self.trybuy_interval}秒后重新尝试.')
                            is_success = False
                    if i == self.number-1 and is_success == False:
                        print("很遗憾，抢购失败，下次继续加油~")
                        break
                    elif is_success == True:
                        print(f'[{time.strftime("%H:%M:%S", time.localtime())} INFO]: 抢购***{good_infos[good_id]["title"]}***成功, 已为您自动提交订单, 请尽快前往淘宝完成付款.')
                        # 电脑语音提示
                        for _ in range(5):
                            pyttsx3.speak('已经为您抢购到你所需的商品, 请尽快前往淘宝完成付款.')
                            time.sleep(self.trybuy_interval)
                        break
                break
    '''打印表格'''
    def printTable(self, title, items):
        assert isinstance(title, list) and isinstance(items, list), 'title and items should be list...'
        table = PrettyTable(title)
        for item in items: table.add_row(item)
        print(table)
        return table
    # 获取购物车
    def buycartinfo(self):
        url = 'https://cart.taobao.com/cart.htm'
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0'
        }
        response = self.session.get(url, headers=headers)
        # print(response.text)
        response_json = re.search('try{var firstData = (.*?);}catch', response.text).group(1)
        response_json = json.loads(response_json)
        user_id = re.search('\|\^taoMainUser:(.*?):\^', response.headers['s_tag']).group(1)
        return response_json, user_id

    # 购买商品
    def buygood(self, info, user_id):
        # 发送结算请求
        url = 'https://buy.taobao.com/auction/order/confirm_order.htm?spm=a1z0d.6639537.0.0.undefined'
        headers = {
            'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'origin': 'https://cart.taobao.com', 'content-type': 'application/x-www-form-urlencoded',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document', 'referer': 'https://cart.taobao.com/',
            'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
        cart_id, item_id, sku_id, seller_id, cart_params, to_buy_info = info['cart_id'], info['item_id'], info['sku_id'], info['seller_id'], info['cart_params'], info['to_buy_info']
        data = {
            'item': f'{cart_id}_{item_id}_1_{sku_id}_{seller_id}_0_0_0_{cart_params}_{urllib.parse.quote(str(to_buy_info))}__0',
            'buyer_from': 'cart',
            'source_time': ''.join(str(int(time.time() * 1000)))
        }
        disable_warnings()
        response = self.session.post(url = url, data = data, headers = headers, verify = False)
        order_info = re.search('orderData= (.*?);\n</script>', response.text).group(1)
        order_info = json.loads(order_info)
        # 发送提交订单请求
        token = self.session.cookies['_tb_token_']
        endpoint = order_info['endpoint']
        data = order_info['data']
        structure = order_info['hierarchy']['structure']
        hierarchy = order_info['hierarchy']
        linkage = order_info['linkage']
        linkage.pop('url')
        submitref = order_info['data']['submitOrderPC_1']['hidden']['extensionMap']['secretValue']
        sparam1 = order_info['data']['submitOrderPC_1']['hidden']['extensionMap']['sparam1']
        input_charset = order_info['data']['submitOrderPC_1']['hidden']['extensionMap']['input_charset']
        event_submit_do_confirm = order_info['data']['submitOrderPC_1']['hidden']['extensionMap']['event_submit_do_confirm']
        url = f'https://buy.taobao.com/auction/confirm_order.htm?x-itemid={item_id}&x-uid={user_id}&submitref={submitref}&sparam1={sparam1}'
        data_submit = {}
        for key, value in data.items():
            if value.get('submit') == 'true' or value.get('submit'):
                data_submit[key] = value
        data = {
            'action': '/order/multiTerminalSubmitOrderAction',
            '_tb_token_': token,
            'event_submit_do_confirm': '1',
            'praper_alipay_cashier_domain': 'cashierrz54',
            'input_charset': 'utf-8',
            'endpoint': urllib.parse.quote(json.dumps(endpoint)),
            'data': urllib.parse.quote(json.dumps(data_submit)),
            'hierarchy': urllib.parse.quote(json.dumps({"structure": structure})),
            'linkage': urllib.parse.quote(json.dumps(linkage))
        }
        headers = {
            'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': 'https://buy.taobao.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://buy.taobao.com/auction/order/confirm_order.htm?spm=a1z0d.6639537.0.0.undefined',
            'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
        response = self.session.post(url, data=data, headers=headers, verify = False)
        if response.status_code == 200:
            return True
        return False

if __name__ == '__main__':
    args = help_info()
    print("请输入对应参数，格式为：--interval [time interval] --time [Starting time] -l [frequency]\n"
          "示例：--interval 0.1 --time 15:59:59.90000000 --l 5")
    parameter = input("\n参数：")
    parameter_list = []
    for i in parameter.split(' '):
        parameter_list.append(i)
    for j in range(len(parameter_list)):
        if parameter_list[j] == "--interval":
            interval = float(parameter_list[j + 1])
        elif parameter_list[j] == "--time":
            kill_time = parameter_list[j + 1]
        elif parameter_list[j] == "--l":
            number = int(parameter_list[j + 1])
    client = TaobaoSnap(trybuy_interval=interval ,Seconds_kill_time=kill_time ,number=number)
    # client = TaobaoSnap(trybuy_interval=1)
    client.run_info()