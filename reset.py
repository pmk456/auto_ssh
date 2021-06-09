import os, sys

if "ssh.bat" not in os.listdir() and ".ip.dat" not in os.listdir() and "ssh" not in os.listdir():
    print("[*] No Files Detected, So Nothing Deleted!")
    print("[*] Created By Pmk")
    sys.exit(1)

if "ssh.bat" in os.listdir():
    os.remove("ssh.bat")
    print("[+] Removed ssh.bat File")
if ".ip.dat" in os.listdir():
    os.remove(".ip.dat")
    print("[+] Removed Ip File")
if "ssh" in os.listdir():
    os.remove("ssh")
    print("[+] Removed SSH File")
print("[*] Reset Success")
print("[*] Created By Pmk")
