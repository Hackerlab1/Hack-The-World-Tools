from abc import abstractmethod
from gettext import install
import os
import sys
import subprocess
import json
import sysconfig
from tkinter import N

print("Welcome to hackers lab whetre all the hacking talk place!! ")
hackerlab = input("[+] Do you have a hacker lab account y/n >>: ")
if hackerlab == "n":
    while True:
        username = input("[+] Create hackerlab username >>: ")
        password = input("[+] Create hackerlab password >>: ")
        password1 = input("[+] Confirm password >>: ")
        if password == password1:
            file = open(username+".txt", "w")
            file.write(username+":"+password)
            file.close()
            hackerlab = "y"
            break
        print("[!] Passwords dont match")

if hackerlab == "y":
    while True:
        login1 = input("[+] Hacker login >>: ")
        login2 = input("[+] Hacker Password >>: ")
        file = open(login1+".txt", "r")
        data = file.readline(login1+":"+login2)
        file.close()
        if data == login1+":"+login2:
            print("[+] Welcome to the hacking world ")
            break
        print("[!] Uncoorect username or password")

print("*************")
print("****TOOLS****")
print("*************")

print("")

tools = {
    "[+] WireShark",
    "[+] Gobuster",
    "[+] Routersploit",
    "[+] BurpSuit",
    "[+] Xerosploit",
    "[+] SetoolKit",
    "[+] Airmon-ng",
    "[+] Dirb",
    "[+] NetCat",
    "[+] airodump-ng"
}

for x in tools:
    print(x)

print("")

print("*************")
print("**Wireshark**")
print("*************")
print("")

def WireShark():
    install = input("[!] Do you want to install wireshark y/n >>: ")
    if install == "n":
        pass
    else:
        print("[+] Now installing wireshark")
    
    Wireinstall = subprocess.run(["sudo","apt", "install", "wireshark"])
    print("[+] Installation Finish")

WireShark()

print("")

print("*************")
print("**Go-buster**")
print("*************")
print("")

def gobuster():
    goinstall = input("[!] Do you want to install gobuster y/n >>: ")
    if goinstall == "n":
        pass
    else:
        print("[+] Now installing gobuster")

        go = subprocess.run(["sudo", "apt", "install", "gobuster"])
        print("Installation Finish")

gobuster()

print("")

print("**************")
print("*Routersploit*")
print("**************")
print("")

def Router():
    sploit = input("[!] Do you want to install rouersploit y/n >>: ")
    if sploit == "n":
        pass
    else:
        print("[+] Now installing routersploit")

    routersploit = subprocess.run(["sudo", "apt", "install", "routersploit"])
    print("[+] Installation Finish")

Router()

print("")

print("*************")
print("**Burpsuit **")
print("*************")
print("")

def burp():
    bu = input("[+] Do you want to install burpsuit y/n >>: ")
    if bu == "n":
        pass
    else:
        print("[+] Now installing burpsuit")

    suit = subprocess.run(["sudo", "apt", "install", "burpsuit"])
    print("[+] Installation Finish")

burp()

print("")
print("*************")
print("**Xerosploit**")
print("*************")
print("")

def xero():
    do = input("[+] Do you want to install xerosploit y/n >>: ")
    if do == "n":
        pass
    else:
        print("[+] Now installing xersploit")

    xersploit = subprocess.run(["clone", "https://github.com/LionSec/xerosploit"])
    print("[+] Now open the xersploit folder and continue")

xero()

print("")

print("")
print("*************")
print("**Setoolkit**")
print("*************")
print("")

def set():
    u = input("[+] Do you want to install setoolkit y/n >>: ")
    if u == "n":
        pass
    else:
        print("[+] Now installing setookit")
    
    setoolkit = subprocess.run(["sudo", "apt", "install", "setoolkit"])
    print("[+] Installation Finish")

set()

print("")

print("")
print("*************")
print("**Airmon-ng**")
print("*************")
print("")

def air():
    r = input("[+] Do you want to install airmon-ng y/n >>: ")
    if r == "n":
        pass
    else:
        print("[+] Now Installing airmon-ng")\

    airmong = subprocess.run(["sudo", "apt", "install", "airmon-ng"])
    print("[+] Installation Finish")

air()

print("")


print("*************")
print("****Dirb*****")
print("*************")
print("")

def di():
    p = input("[+] Do you want to install dirb y/n >>: ")
    if p == "n":
        pass
    else:
        print("[+] Now installing dirb")

    dirb = subprocess.run(["sudo", "apt", "install", "dirb"])
    print("[+] Installation Finish")

di()

print("")

print("*************")
print("***Netcat****")
print("*************")
print("")

def net():
    q = input("[+] Do you want to install netcat y/n >>: ")
    if q == "n":
        pass
    else:
        print("[+] Now installing netcat")

    netcat = subprocess.run(["sudo", "apt", "install", "netcat"])
    print("[+] Installation finish")

net()

print("")

print("*************")
print("*Airodump-ng**")
print("*************")
print("")

def airo():
    t = input("[+] Do you want to install Airodump-ng y/n >>: ")
    if t == "n":
        pass
    else:
        print("[+] Now installing airodum-ng")

    airodump = subprocess.run(["sudo", "apt", "install", "airodump-ng"])
    print("[+] Installation Finish")

airo()

print("")

print("[+] Start hacking with these hacking tool for professionals hackers")