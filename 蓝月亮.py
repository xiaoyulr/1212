import json
import pprint
import time
import urllib
import requests
from urllib.parse import quote, urlencode
import urllib.parse

activityId = "dzb59b96a34f89841f64a4a7f91b5b"
url_activityid = 'https://lzdz1-isv.isvjcloud.com/dingzhi/may/yiliPlant/activity/5428982'
host = 'https://lzdz1-isv.isvjcloud.com/dingzhi/may/yiliPlant'
actor_uuid = '8129a180ad244ca081d18e33e481fbca'


##获取登录确认
def accessLog(cook, shopid, venderid):
    url = f"https://lzdz1-isv.isvjcloud.com/common/accessLogWithAD?venderId={venderid}" + f"&code=99&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&activityId={activityId}&pageUrl=" + urllib.parse.quote(
        f"{url_activityid}?activityId={activityId}&shareUuid=27f1a578aee24dc0a2e4d3de6445657a&adsource=null&shareuserid4minipg=XleAaua/0tRV9Bre9XqbOfkaL5GGqMTUc8u/otw2E+a7Ak3lgFoFQlZmf45w8Jzw&shopid={shopid}&sid=f85cdf5113ede1338d544e266c2997cw&un_area=",
        'utf-8') + "1_2812_51142_0&subType=app&adSource=null"
    # print(url)
    headers = {
        'Host': 'lzdz1-isv.isvjcloud.com',
        'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653901529537%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://lzdz1-isv.isvjcloud.com',
        'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
        'Cookie': cook,
    }
    response = requests.post(url=url, headers=headers)
    # print(response.status_code)


##获取活动cookie
def cookie():
    url = f"{url_activityid}?activityId={activityId}&shareUuid=27f1a578aee24dc0a2e4d3de6445657a"
    headers = {

        'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653829132082%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
    }
    session = requests.session()
    cookies = session.get(url=url, headers=headers).cookies
    cookie_t = requests.utils.dict_from_cookiejar(cookies)
    # 将cookies转为cookie字符串
    # print(cookie_t)
    cookies_str = ''
    for cookie in cookie_t:
        cookies_str += cookie + "=" + cookies[cookie] + ";"
    # print(cookies_str)
    return cookies_str


##获得userid
def userid(cook):
    url = f"https://lzdz1-isv.isvjcloud.com/dz/common/getSimpleActInfoVo?activityId={activityId}"
    headers = {
        'Host': 'lzdz1-isv.isvjcloud.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653880802941%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://lzdz1-isv.isvjcloud.com',
        'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?{activityId}=dz104dd67036768d845d5ced9fb277&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cook,
    }
    response = requests.post(url=url, headers=headers).json()
    # print(response)
    shopId = response["data"]['shopId']
    venderId = response["data"]["venderId"]
    # print(shopId, venderId)
    return shopId, venderId


##获得token
def get_token():
    url = 'https://api.m.jd.com/client.action?functionId=isvObfuscator&body=%7B%22url%22%3A%22https%3A//lzdz1-isv.isvjcloud.com%22%2C%22id%22%3A%22%22%7D&uuid=ab640b5dc76b89426f72115f5b2e06e934a5fbe9&client=apple&clientVersion=10.1.4&st=1650250640876&sv=102&sign=7ea66dcb2969eff53c43b5b8a4937dbe'
    headers = {
        'user-agent': 'okhttp/3.12.1;jdmall;android;version/10.5.4;build/96906;',
        # 'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'content-length': '87',

        'Cookie': 'pt_key=AAJihXdbADBxIUOi_Bpxbp8PgZSOC_1akQG7Zg4KuA6H9LwZci5Tr5c5Jz4GzAqtj93Vexmtbkw;pt_pin=jd_OlkdoeEggWKd;',
    }

    response = requests.post(url=url, headers=headers).json()
    # print(response)
    token = response['token']
    # print(response)
    return token


##获取pin
def get_mypin(userid2, cook, token):
    """userid,token"""
    url = f'https://lzdz1-isv.isvjcloud.com/customer/getMyPing?userId={userid2}&token={token}&fromType=APP'
    # print(url)
    headers = {
        'Host': 'lzdz1-isv.isvjcloud.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653880802941%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://lzdz1-isv.isvjcloud.com',
        'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cook,
    }
    response = requests.post(url=url, headers=headers).json()

    mypin = response["data"]["secretPin"]
    # print(response)
    return mypin


##活动兑换列表
def price_list(cook):
    """
    https://lzdz1-isv.isvjcloud.com/dingzhi/may/yili/getPrize
    """
    url = f"{host}/getPrize?activityId={activityId}" \
          "&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw" \
          "&actorUuid=27f1a578aee24dc0a2e4d3de6445657a"
    headers = {
        'Host': 'lzdz1-isv.isvjcloud.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653880802941%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://lzdz1-isv.isvjcloud.com',
        'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
        'Cookie': cook,
    }

    response = requests.post(url=url, headers=headers).json()
    for i in response['data']['exchangePriceList']:
        prizeName = i['prizeName']
        priceNum  =i['priceNum']
        prizeScore = i['prizeScore']

        print(f"目前{prizeName}库存还有{priceNum}需要{prizeScore}清饮币")


##目前积分
def total_score(cook):
    url = f'{host}/activityContent?activityId={activityId}&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&pinImg=https%3A%2F%2Fimg10.360buyimg.com%2Fimgzone%2Fjfs%2Ft1%2F7020%2F27%2F13511%2F6142%2F5c5138d8E4df2e764%2F5a1216a3a5043c5d.png&nick=jd_OlkdoeEggWKd&cjyxPin=&cjhyPin=&shareUuid={actor_uuid}'
    # print(url)
    headers = {
        'Host': 'lzdz1-isv.isvjcloud.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653880802941%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://lzdz1-isv.isvjcloud.com',
        'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cook,
    }
    response = requests.post(url=url, headers=headers).json()
    # pprint.pprint(response)
    if response['result'] == True:
        name = response["data"]["nick"]
        score = response["data"]["score"]

        return name, score


##兑换
def exchange(cook, pin):
    """XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw"""
    url = f"{host}/exchange?activityId={activityId}&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&actorUuid={actor_uuid}&prizeId=2"
    headers = {
        'Host': 'lzdz1-isv.isvjcloud.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json',
        'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653880802941%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://lzdz1-isv.isvjcloud.com',
        'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid={actor_uuid}&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
        'Cookie': cook,
    }

    """
    {activityId}=dz104dd67036768d845d5ced9fb277&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&actorUuid=e950d6953128416bb9e6443621a9a597&prizeId=3
    ?{activityId}=dz104dd67036768d845d5ced9fb277&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&actorUuid=e950d6953128416bb9e6443621a9a597&prizeId=3
    """
    response = requests.post(url=url, headers=headers).text
    print(response)


##获取活动次数奖励
def activity_reward(cook):
    print('开始做积分任务')
    data = ['taskType=0&taskValue=0', 'taskType=5&taskValue=100019565932', 'taskType=21&taskValue=21']
    for i in data:
        url = f'{host}/saveTask?activityId={activityId}&actorUuid={actor_uuid}&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&{i}'
        """
        https://lzdz1-isv.isvjcloud.com/dingzhi/may/yiliPlant/saveTask?activityId=dzb59b96a34f89841f64a4a7f91b5b&actorUuid=8129a180ad244ca081d18e33e481fbca&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&taskType=21&taskValue=21
        https://lzdz1-isv.isvjcloud.com/dingzhi/may/yiliPlant/saveTask?activityId=dzb59b96a34f89841f64a4a7f91b5b&actorUuid=27f1a578aee24dc0a2e4d3de6445657a&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&taskType=0&taskValue=0

        """
        headers = {
            'Host': 'lzdz1-isv.isvjcloud.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653880802941%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://lzdz1-isv.isvjcloud.com',
            'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
            'Cookie': cook,
        }
        response = requests.post(url=url, headers=headers).json()
        if response["result"]:
            print('此任务已做完,获得积分')
        else:
            print(response)
            time.sleep(5)


##制作产品
def make_drink():
    data = [['taskValue=1&count=15', 'taskValue=3&count=1', 'taskValue=1&count=1'],
            ['taskValue=2&count=10', 'taskValue=4&count=1', 'taskValue=2&count=1']]
    for i in data:
        url = f"https://lzdz1-isv.isvjcloud.com/dingzhi/may/yiliPlant/make?activityId=dzb59b96a34f89841f64a4a7f91b5b&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&{i[0]}"
        headers = {
            'Host': 'lzdz1-isv.isvjcloud.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653880802941%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://lzdz1-isv.isvjcloud.com',
            'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
            'Cookie': cook,
        }
        response = requests.post(url=url, headers=headers).json()
        print(response)
        time.sleep(5)
        url = f"https://lzdz1-isv.isvjcloud.com/dingzhi/may/yiliPlant/make?activityId=dzb59b96a34f89841f64a4a7f91b5b&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&{i[1]}"
        response = requests.post(url=url, headers=headers).json()
        print(response)
        time.sleep(5)
        url = f"https://lzdz1-isv.isvjcloud.com/dingzhi/may/yiliPlant/sell?activityId=dzb59b96a34f89841f64a4a7f91b5b&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&{i[2]}"
        response = requests.post(url=url, headers=headers).json()
        print(response)
        if response["result"] == "True":
            total_score = response["data"]["result"]
            print(f'目前总青饮币为{total_score}')
        else:
            print(response["errorMessage"])
        time.sleep(5)


if __name__ == '__main__':
    cook = cookie()
    userid2, venderid = userid(cook)
    if userid2 == 0:
        accessLog(cook, venderid, venderid)
        token = get_token()
        pin = get_mypin(venderid, cook, token)
    elif venderid == 0:
        accessLog(cook, userid2, userid2)
        token = get_token()
        pin = get_mypin(userid2, cook, token)
    else:
        accessLog(cook, userid2, venderid)
        token = get_token()
        pin = get_mypin(userid2, cook, token)
    name, score = total_score(cook)
    print(f"开始账号{name}植护清雅任务,目前积分{score}")
    price_list(cook)

    # time.sleep(10)
    # exchange(cook, pin)
    activity_reward(cook)
    make_drink()
    name, score = total_score(cook)
    print(f"账号{name}植护清雅任务已完成,目前积分{score}")
"""
制作燕麦
activityId=dzb59b96a34f89841f64a4a7f91b5b&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&
activityId=dzb59b96a34f89841f64a4a7f91b5b&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&
activityId=dzb59b96a34f89841f64a4a7f91b5b&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&
"""
