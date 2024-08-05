#--[ CODE BY - @DARK_LMNx999 ]--
#--[ SCRIPT - NUMBER TO FULL INFO ]-
#--[ TYPE - PREMIUM ONLY ]--

import os,sys,requests
import json,string
os.system('clear')
def LMNx9_INFO(number):
    url = f"https://api.ubatube.com/api/v2/company/{number}/?key={api_key}"
    try:
        response = requests.get(url)
    except:
        print("Invalid API Key !!! .")
        os.system('xdg-open https://t.me/DARK_LMNx999')
        sys.exit()
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None
number = input("\n[>] YOUR NUMBER : ")
api_key = input("[>] YOUR API KEY : ")
info = LMNx9_INFO(number)
if info is not None:
    print(f"Information : {info['data']['name']}")
else:
    print("Invalid API Key !!! .")
    os.system('xdg-open https://t.me/DARK_LMNx999')
    sys.exit()