#!/usr/bin/python3
import os
from time import sleep
from sys import exit

RED = "\033[1;31m"
GREEN = "\033[0;32m"
os.system('clear')
print(GREEN, """
 ____            _    
|  _ \ _ __ ___ | | __
| |_) | '_ ` _ \| |/ /
|  __/| | | | | |   < 
|_|   |_| |_| |_|_|\_\ """)
print(GREEN, "\n****************************************************************")
print(GREEN, "\n* Copyright of Patan Musthakheem, 2021                         *")
print(GREEN, "\n* www.github.com/pmk456                                        *")
print(GREEN, "\n* www.youtube.com/hackerx                                      *")
print(GREEN, "\n****************************************************************")
if '.ip.txt' not in os.listdir():
    print('[*] Ip File Not Detected!')
    i = input('[*] Enter Ip: ')
    n = input('[*] Enter UserName: ')
    with open('.ip.txt', 'a') as f:
        f.write(i)
        f.write('\n')
        f.write(n)
        print('[*] Ip And Username Has Been Saved To Ip.txt')
        f.close()
else:
    print('[*] Ip File Detected!')
po = open('.ip.txt', 'r')
po1 = po.readlines()
ssh_ip = po1[0]
ssh_un = po1[1]
ssh_ip1 = ssh_ip
if 'ssh' in os.listdir():
    print('[*] Bash Script Exists')
    print('[*] Delete Everything In Directory Except Setup.py and compile.sh If You want to reset')
else:
    print('[*] Generating Bash Script...')
    lines = f"""#!/bin/bash
    IP={ssh_ip}
    echo "[*] Connecting To {ssh_un}..."
    sleep 0.5
    echo "[*] Created By Pmk "
    if ping -q -c 1 -W 1 $IP >/dev/null; then
    echo "[*] Connected To {ssh_un}"
    sleep 1
    clear
    ssh {ssh_un}@{ssh_ip}
    else
    echo "[*] Cant Connect To {ssh_un} No Reply!"
    echo "[*] Exiting..."
    exit
    fi """
    os.system('touch ssh')
    os.system('chmod +x ssh')
    a_file = open("ssh", "w")
    a_file.writelines(lines)
    a_file.close()
    sleep(1.5)
    print('[*] Generated Bash Script!')
    os.system("clear")
print('[*] Creating RSA Keypair For Password Less connection')
os.system('ssh-keygen -t rsa -b 4096')
print('[*] Copying Public Key ')
print('[*] It Will Ask You Password Of Remote Computer Enter It!')
os.system(f'ssh-copy-id {ssh_un}@{ssh_ip}')
i = input('[*]Move It To /bin For Accessing It anywhere [Y/N]: ')
if i == 'y' or i == 'yes' or i == "Y":
    print(RED, "[*] This Needs Sudo Permission")
    name = input("[*] Enter Name For Accessing It Anywhere From Terminal: ")
    os.system(f"sudo mv ssh /bin/{name}")
else:
    os.system('clear')
    print(GREEN, """
     ____            _    
    |  _ \ _ __ ___ | | __
    | |_) | '_ ` _ \| |/ /
    |  __/| | | | | |   < 
    |_|   |_| |_| |_|_|\_\ """)
    print(GREEN, "\n****************************************************************")
    print(GREEN, "\n* Copyright of Patan Musthakheem, 2021                         *")
    print(GREEN, "\n* www.github.com/pmk456                                        *")
    print(GREEN, "\n* www.youtube.com/hackerx                                      *")
    print(GREEN, "\n****************************************************************")
    exit(12)
