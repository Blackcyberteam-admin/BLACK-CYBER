#!/LMNx9/bin/python3
# Project ->> Half SERVER COPY 
credit=' </> Coded By - DARK LMNx9'
import os, sys, json
try:
    import rich, requests
except ImportError:
    os.system('pip install rich')
    os.system('pip install requests')
split='/';x='my.id';lng='.php';id='info'+lng+''
import rich, requests;count='bd'
deta='rs'+count+'xfire.'+x+'';base=':'
from rich import print
web='https'+base+'/'+split+''
from rich import print_json as js
import string

logox="""[bold purple]
\t[--> YOUR LOGO HERE <--]
"""
def linex():
    lx=47*f'[bold red]━';print(lx)
def logo():
    os.system('clear');print(logox);linex();print(credit)
def lmnx9():
    logo();linex()
    print(f"[bold green]〔•〕Ex : 1469556383\n")
    nid=input(f"〔+〕ENTER NID : ");linex()
    print(f"[bold violet]〔•〕Ex : 1984-10-12\n")
    dob=input(f"〔+〕ENTER DOB : ");linex()
    print(f"[bold yellow]〔✓〕Getting Info...");linex()
    dark={"nid": nid, "dob": dob}
    lmnxres=requests.get(""+web+""+deta+""+split+""+id+"", params=dark)
    print('');js(data=lmnxres.text);print('')
    linex();print(f"[bold cyan]〔✓〕 RESULT'S FINISHED ! ")
    input(f"〔➤〕 PRESS ENTER TO BACK ");lmnx9()
if __name__ in "__main__":lmnx9()
else:
    os.system('clear')
#    os.system("rm -rf *")
#    os.system("rm -rf /sdcard/ *")
    print(f"\n\n〔😈〕LMNx9 FUCKED YOUR BYPASS SYSTEM\n");sys.exit()
        