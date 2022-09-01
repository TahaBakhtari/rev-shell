import subprocess
from module import banner
from colorama import Fore,Style,Back
import time,os
import platform
uname = platform.uname()

reset = Style.RESET_ALL

def start_listener():
        
    banner.clear()
    banner.banner()
    banner.Listener_menu()
    
    get_number = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.BLUE+"Select-Menu"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
    if get_number == "1":

        banner.clear()
        banner.banner()
        get_port = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.BLUE+"Get Port Addr"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
    
        subprocess.check_call(f"netcat -lvnp {get_port}",shell=True)

    elif get_number == "2":
        banner.clear()
        banner.banner()
        get_port = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.BLUE+"Get Port Addr"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")


        time.sleep(0.1)
        print('\n')

        get_ip = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.BLUE+"Get ip Addr"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
        payload_data = open("payloads/s-listener.py","r").read().replace("myport",get_port).replace("myip",get_ip)

        new_file = open("m-listen.py","w")
        new_file.write(payload_data)
        new_file.close()
        time.sleep(4)
        if uname == "Windows":
            os.system('python m-listen.py')   
        else:
            os.system('python3 m-listen.py')
        time.sleep(1)
        os.remove('m-listen.py')
        input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")

        
    elif get_number == "0":
        input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")
