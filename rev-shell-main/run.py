from colorama import Fore,Style,Back
import os,subprocess,platform,sys
from module import banner,builder,listener


while True:
    banner.clear()
    banner.banner()
    banner.infolist0()

    try:

        get_option =  input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MY-TOOLS"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")


        if get_option == "1":
            builder.Select_Payload()
        
        elif get_option == "2":
            listener.start_listener()

        elif get_option == "0":
            print(Back.BLUE+Fore.LIGHTRED_EX+'\n  Have a Nise Day . . .'+Style.RESET_ALL)
            sys.exit()
    except:
        exit("")
    