from colorama import Fore,Style,Back
import time
import os
import platform


reset = Style.RESET_ALL

def banner():
    print(Fore.RED+"""
    )                         )         (     
 ( /(     (         (      ( /(         )\ )  
 )\())    )\        )\     )\())  (    (()/(  
((_)\  ((((_)(    (((_)  |((_)\   )\    /(_)) 
 _((_)  )\ _ )\   )\___  |_ ((_) ((_)  (_))   
| || |  (_)_\(_) ((/ __| | |/ /  | __| | _ \  
| __ |   / _ \    | (__    ' <   | _|  |   /  
|_||_|  /_/ \_\    \___|  _|\_\  |___| |_|_\\
    
    """+reset)


def infolist0():
    time.sleep(0.1)
    print(Fore.RED+" ["+Fore.WHITE+"*"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options below \n")
    time.sleep(0.1)
    print(Fore.RED+" [1]"+Fore.WHITE+" Build Payload \n")
    time.sleep(0.1)
    print(Fore.RED+" [2]"+Fore.WHITE+" Start Listener\n") 
    time.sleep(0.1)
    print(Fore.RED+" [0]"+Fore.WHITE+" Exit . . .\n"+reset)

def builer_menu():
    time.sleep(0.1)
    print(Fore.RED+" [1]"+Fore.WHITE+" Build C Payload\n")
    time.sleep(0.1)
    print(Fore.RED+" [2]"+Fore.WHITE+" Build Python Payload [Windows]\n")
    time.sleep(0.1)
    print(Fore.RED+" [0]"+Fore.WHITE+" Back To Menu\n"+reset)
    time.sleep(0.1)


def platform_menu():
    time.sleep(0.1)
    print(Fore.RED+" [1]"+Fore.WHITE+" Linux\n")
    time.sleep(0.1)
    print(Fore.RED+" [2]"+Fore.WHITE+" Back To Menu\n") 



def Listener_menu():
    time.sleep(0.1)
    print(Fore.RED+" [1]"+Fore.WHITE+" Start listener (netcat -> Linux/Mac) \n")
    time.sleep(0.1)
    print(Fore.RED+" [2]"+Fore.WHITE+" Start listener (python -> windows) \n")
    time.sleep(0.1)
    print(Fore.RED+" [0]"+Fore.WHITE+" Back To Menu\n") 

def clear():
    osname = platform.uname()[0]
    if osname == "Windows":

        os.system("cls")

    else:
        os.system("clear")

