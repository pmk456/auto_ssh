import os
from time import sleep
RED = "\033[1;31m"
GREEN = "\033[0;32m"
if 'SUDO_UID' not in os.environ.keys():
    print(RED, 'Run it As Root!')
    exit(0)
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
    f = open('.ip.txt', 'a')
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
if 'ssh' not in os.listdir():
    print('[*] Generating Bash Script...')
    lines = f"""
    #!/bin/bash
    IP={ssh_ip}
    echo "\[*] Connecting To {ssh_un}..."
    sleep 0.5
    echo "\[*] Generated With Auto_SSH"
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
else:
    print('[*] Bash Script Exists')
    print('[*] Delete Everything In Directory Except Setup.py and compile.sh If You want to reset')
print('[*] Now We Have Some Important Stuff To Do')
print('[*] Let\'s Create An SSH Pair For Password Less Connection To Your Remote Computer')
print('[*] Just Put It Default In Location And Just Press Enter')
print('[*] For Password You Can Use anything')
print('[*] Creating RSA Keypair')
os.system('ssh-keygen -t rsa -b 4096')
print('[*] Copying Public Key ')
print('[*] It Will Ask You Password Of Remote Computer Enter It!')
os.system(f'ssh-copy-id {ssh_un}@{ssh_ip}')
print('[*] DONE!')
print('[*] You can Change Username And ip Address In ip.txt or Delete it and Re Run The Script')
print('[*] EXITING...')
# Power Of Python
print('[*] Testing Script...')
print('[*] If It Login Without Asking Password Then Everything Is Working Correctly!')
i = input('[*] Compile And Move It To /bin [Y/N]: ')
if i == 'y' or i == 'yes':
    print(GREEN, '[*] Starting Compile Script')
    #Pmk
    os.system("sh compile.sh")
else:
    os.system('clear')
    print("""
                              ____            _    
                             |  _ \ _ __ ___ | | __
                             | |_) | '_ ` _ \| |/ /
                             |  __/| | | | | |   < 
                             |_|   |_| |_| |_|_|\_\  """)
    exit(12)
                                                   


