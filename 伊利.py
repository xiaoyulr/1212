import time
import urllib
import requests
from urllib.parse import quote, urlencode
import urllib.parse

activityId = "dz54e8229b41be9ed871eeb8572007"
url_activityid = 'https://lzdz1-isv.isvjcloud.com/dingzhi/may/yili/activity/3029899'
host = 'https://lzdz1-isv.isvjcloud.com/dingzhi/may/yili'
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
        # 'Content-Length': '159',
        'Accept': 'application/json',
        # 'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653880802941%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://lzdz1-isv.isvjcloud.com',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cook,
    }

    response = requests.post(url=url, headers=headers).text
    print(response)

##获取登录确认
def accessLog(cook,shopid,venderid):
    url = f"https://lzdz1-isv.isvjcloud.com/common/accessLogWithAD?venderId={venderid}"+f"&code=99&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&activityId={activityId}&pageUrl="+urllib.parse.quote(f"{url_activityid}?activityId={activityId}&shareUuid=27f1a578aee24dc0a2e4d3de6445657a&adsource=null&shareuserid4minipg=XleAaua/0tRV9Bre9XqbOfkaL5GGqMTUc8u/otw2E+a7Ak3lgFoFQlZmf45w8Jzw&shopid={shopid}&sid=f85cdf5113ede1338d544e266c2997cw&un_area=", 'utf-8')+"1_2812_51142_0&subType=app&adSource=null"
    print(url)
    headers = {
        'Host': 'lzdz1-isv.isvjcloud.com',
        'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653901529537%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://lzdz1-isv.isvjcloud.com',
        'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
        'Cookie': cook,
    }
    response = requests.post(url=url, headers=headers)
    print(response.status_code)


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
    print(cookie_t)
    cookies_str = ''
    for cookie in cookie_t:
        cookies_str += cookie + "=" + cookies[cookie] + ";"
    print(cookies_str)
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
    print(response)
    shopId = response["data"]['shopId']
    venderId = response["data"]["venderId"]
    print(shopId,venderId)
    return shopId,venderId


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
    print(response)
    return token


##获取pin
def get_mypin(userid2, cook, token):
    """userid,token"""
    url = f'https://lzdz1-isv.isvjcloud.com/customer/getMyPing?userId={userid2}&token={token}&fromType=APP'
    print(url)
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
    print(response)
    return mypin


##兑换列表
def exchange(cook, pin):
    """XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw"""
    url = f"{host}/exchange?activityId={activityId}&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&actorUuid=27f1a578aee24dc0a2e4d3de6445657a&prizeId=2"
    print(url)
    headers = {
        'Host': 'lzdz1-isv.isvjcloud.com',
        'Connection': 'keep-alive',
        # 'Content-Length': '159',
        'Accept': 'application/json',
        # 'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653880802941%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://lzdz1-isv.isvjcloud.com',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
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
    data=['taskType=14&taskValue=1000366442','taskValue=1000361242','taskType=14&taskValue=1000013402','taskType=70&taskValue=70','taskType=71&taskValue=71','taskType=72&taskValue=72','taskType=73&taskValue=73','taskType=12&taskValue=1','taskType=12&taskValue=2']
    for i in data:
        url = f'{host}/saveTask?activityId={activityId}&actorUuid=27f1a578aee24dc0a2e4d3de6445657a&pin=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&{i}'
        headers = {
            'Host': 'lzdz1-isv.isvjcloud.com',
            'Connection': 'keep-alive',
            # 'Content-Length': '159',
            'Accept': 'application/json',
            # 'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'jdapp;android;10.5.4;;;appBuild/96906;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1653880802941%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DJSnY2S1YJK3DzumZwZvEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://lzdz1-isv.isvjcloud.com',
            # 'Sec-Fetch-Site': 'same-origin',
            # 'Sec-Fetch-Mode': 'cors',
            # 'Sec-Fetch-Dest': 'empty',
            'Referer': f'https://lzdz1-isv.isvjcloud.com/dingzhi/lanyueliang/sakura/activity/434150?activityId={activityId}&shareUuid=e950d6953128416bb9e6443621a9a597&adsource=null&shareuserid4minipg=XleAaua%2F0tRV9Bre9XqbOfkaL5GGqMTUc8u%2Fotw2E%2Ba7Ak3lgFoFQlZmf45w8Jzw&shopid=1000001195&sid=a163e62bbe279c886359d18d4d43152w&un_area=1_2812_51142_0',
            # 'Accept-Encoding': 'gzip, deflate',
            # 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': cook,
        }
        response = requests.post(url=url, headers=headers).text
        print(response)
        time.sleep(5)


if __name__ == '__main__':
    cook = cookie()
    userid2,venderid= userid(cook)
    if userid2 == 0:
        accessLog(cook,venderid,venderid)
        token = get_token()
        pin = get_mypin(venderid, cook, token)
    elif venderid== 0:
        accessLog(cook,userid2,userid2)
        token = get_token()
        pin = get_mypin(userid2, cook, token)
    else:
        accessLog(cook,userid2,venderid)
        token = get_token()
        pin = get_mypin(userid2, cook, token)
    price_list(cook)

    time.sleep(10)
    # exchange(cook, pin)
    activity_reward(cook)