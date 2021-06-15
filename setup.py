import ctypes, os, pickle, sys, time
import subprocess as sp
from time import sleep
system = None

    
    

if sys.platform == 'win32':
    system = 'Windows'
    admin = ctypes.windll.shell32.IsUserAnAdmin() == 1
    os.system('color a')
elif sys.platform == 'linux':
    system = 'Linux'
if os.path.exists("/data/data/com.termux/"):
    system = 'Termux'
def banner():
    print("""
     ____            _    
    |  _ \ _ __ ___ | | __
    | |_) | '_ ` _ \| |/ /
    |  __/| | | | | |   < 
    |_|   |_| |_| |_|_|\_\ """)
    print("\n****************************************************************")
    print("\n* Copyright of Patan Musthakheem, 2021                         *")
    print("\n* www.github.com/pmk456                                        *")
    print("\n* www.youtube.com/hackerx                                      *")
    print("\n****************************************************************")
if system == 'Termux' or system == "Linux":
    RED = "\033[1;31m"
    GREEN = "\x1b[0;32m"
    if system == 'Linux':
        if os.path.exists("/bin/ssh") or os.path.exists("/usr/bin/ssh"):
            pass
        else:
            print(RED + "[-] SSH IS NOT INSTALLED IN YOU SYSTEM")
            per = input(GREEN + "[+] Install SSH [Y/N]: ")
            if per == 'y' or per == 'Y' or per == "yes" or per == "Yes":
                os.system("sudo apt install openssh-client --yes")
            else:
                banner()
                sys.exit(12)
    elif system == "Termux":
        if not os.path.exists("/data/data/com.termux/files/usr/bin/ssh"):
            print(RED + "[-] SSH IS NOT INSTALLED IN YOU SYSTEM")
            per = input(GREEN + "[+] Install SSH [Y/N]: ")
            if per == 'y' or per == 'Y' or per == "yes" or per == "Yes":
                os.system("pkg install openssh")
            else:
                banner()
                exit(12)
    print(GREEN)
    os.system("clear")
    banner()
    if '.ip.dat' not in os.listdir():
        print("[+] IP File Not Detected")
        ip = input("[+] Enter Ip Of Remote Computer: ")
        un = input("[+] Enter User Name: ")
        ip_un = [ip, un]
        with open('.ip.dat', 'wb') as file:
            try:
                pickle.dump(ip_un, file)
            except Exception:
                print("[-] Can\'t Save IP And User Name")
            else:
                print("[+] Save Success!")
    else:
        with open(".ip.dat", 'rb') as file:
            ip_un = pickle.load(file)
            ssh_ip = ip_un[0]
            ssh_un = ip_un[1]
    if 'ssh' in os.listdir():
        print("[+] Bash Script Exists")
    else:
        with open(".ip.dat", 'rb') as file:
            ip_un = pickle.load(file)
            ssh_ip = ip_un[0]
            ssh_un = ip_un[1]
        print('[*] Generating Bash Script...')
        lines = f"""#!/bin/bash
        IP={ssh_ip}
        echo "[+] Connecting To {ssh_un}..."
        sleep 0.5
        echo "[+] Created By Pmk "
        if ping -q -c 1 -W 1 $IP >/dev/null; then
        echo "[+] Connected To {ssh_un}"
        sleep 1
        clear
        ssh {ssh_un}@{ssh_ip}
        else
        echo "[+] Cant Connect To {ssh_un} No Reply!"
        echo "[+] Exiting..."
        exit
        fi """
        os.system('touch ssh')
        os.system('chmod +x ssh')
        a_file = open("ssh", "w")
        a_file.writelines(lines)
        a_file.close()
        sleep(1.2)
        print('[+] Generated Bash Script!')
if system == "Windows":
    os.system("cls")
    banner()
    if '.ip.dat' not in os.listdir():
        print("[+] IP File Not Detected")
        ip = input("[+] Enter Ip Of Remote Computer: ")
        un = input("[+] Enter User Name: ")
        ip_un = [ip, un]
        with open('.ip.dat', 'wb') as file:
            try:
                pickle.dump(ip_un, file)
            except Exception:
                print("[-] Can\'t Save IP And User Name")
            else:
                print("[+] Save Success!")
    else:
        with open(".ip.dat", 'rb') as file:
            ip_un = pickle.load(file)
            ssh_ip = ip_un[0]
            ssh_un = ip_un[1]
            file.close()
    if 'script.bat' not in os.listdir():
        with open(".ip.dat", 'rb') as file:
            ip_un = pickle.load(file)
            ssh_ip = ip_un[0]
            ssh_un = ip_un[1]
        print('[+] Generating Batch File')
        script = f"""
        @echo off
        echo [+] Connecting To {ssh_un}
        echo [+] Created By Pmk 
        ping -n 1 {ssh_ip} | find "TTL=" >nul
        if errorlevel 1 (
        echo [+] Cant Connect To {ssh_un} No Reply!
        echo [+] Exiting...
        EXIT /B 0
        ) else (
        echo [+] Connected To {ssh_un}
        timeout 1 > nul
        cls
        ssh {ssh_un}@{ssh_ip}
        )
        """
        with open("script.bat", 'w') as file:
            file.writelines(script)
            file.close()
if system != "Windows":
    os.system("clear")
else:
    os.system("cls")
per = input("[+] Create RSA Pair For Password Less Connection [Y/N]: ")
if per == 'y' or per == 'Y' or per == "yes" or per == "Yes":
    print('[+] Creating RSA Keypair For Password Less connection')
    os.system('ssh-keygen -t rsa -b 4096')

if system != 'Windows':
    os.system("clear")
    per1 = input("[+] Copy Public Key To Remote Computer [Y/N]: ")
    if per1 == 'y' or per == 'Y' or per == "yes" or per == "Yes":
        os.system("clear")
        print('[+] Copying Public Key ')
        print('[+] It Will Ask You Password Of Remote Computer Enter It!')
        os.system(f'ssh-copy-id {ssh_un}@{ssh_ip}')
    i = input('[+] Move It To /usr/bin For Accessing It anywhere [Y/N]: ')
    if i == 'y' or i == 'yes' or i == "Y":
        name = input("[+] Enter Name For Accessing It Anywhere From Terminal: ")
        if system == "Termux":
            os.system(f"mv ssh /data/data/com.termux/files/usr/bin/{name}")
        elif system == "Linux":
            print(RED, "[+] This Needs Sudo Permission")
            print(GREEN)
            os.system(f"sudo mv ssh /usr/bin/{name}")
        else:
            pass
    else:
        os.system("clear")
        banner()
else:
    os.system('cls')
    per1 = input("[+] Copy Public Key To Remote Computer [Y/N]: ")
    if per1 == 'y' or per == 'Y' or per == "yes" or per == "Yes":
        print("[+] Copying Public Key File To Remote Computer")
        print('[+] It Will Ask You Password Of Remote Computer Enter It!')
        cmd = f"""type $env:USERPROFILE\.ssh\id_rsa.pub | ssh {ssh_un}@{ssh_ip} "cat >> .ssh/authorized_keys" """
        sp.run(["powershell", "-Command", cmd])
    else:
        os.system("cls")

if system == "Windows":
    i = input('[+] Move The Script To C:\Windows\System32 For Accessing It anywhere [Y/N]: ')
    if i == 'y' or i == 'yes' or i == "Y":
        os.system('color 4')
        print("[+] THIS NEEDS ADMINISTRATOR PERMISSION")
        name = input("[+] Enter Name For Accessing It Anywhere From cmd (or) Powershell: ")
        if admin:
            sp.run(['powershell', '-Command', 'mv', 'script.bat', f'C:\Windows\\System32\\{name}.bat'])
        else:
            print("[+] NOW IT WILL ASK FOR ADMINISTRATOR PERMISSION")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        banner()
