#!/usr/bin/python3
#!/coded/by/@DARK_LMNx999

# PROJECT -> GEMINI AI 🔥
# FOR API KEY -> t.me/@DARK_LMNx999

import json,os,sys,requests,urllib

os.system('clear')
os.system('xdg-open https//t.me/DARK_TEAM_LMNx9')

lmn = input('(+) ENTER QUESTION : ')
key = input('(+) ENTER API KEY : ')

lmnXua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
url = f"https://geminigptai.com/api?prompt={key}"
payload = {"content": lmn, "role": "user"}

headers = {
    "Host": "geminigptai.com",
    "content-length": str(len(payload)),
    'sec-ch-ua': '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-platform': '"Android"',
    "sec-ch-ua-mobile": "?1",
    "user-agent": lmnXua,
    "content-type": "text/plain;charset=UTF-8",
    "accept": "*/*",
    "origin": "https://geminigptai.com",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://geminigptai.com/chat",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "priority": "u=1, i"
}

try:
    lmnXreq = requests.post(url, data=payload, headers=headers)
except Exception as x:
    os.system('xdg-open https//t.me/DARK_LMNx999')
    sys.exit('\n(/) API KEY INVALID ! \n')
    
print(lmnXreq)
