#!/usr/bin/python3
import os
ip_file = ".ip.txt"
ssh_file = "ssh"
if ip_file not in os.listdir ( ) and ssh_file not in os.listdir ( ):
    print ("[*] No Files Detected, So Nothing Deleted!")
if ip_file in os.listdir():
    print ("[*] Deleting ip.txt File")
    os.system ("rm .ip.txt")
    print("Removed Ip File")
if ssh_file in os.listdir ( ):
    print ("[*] Deleting SSH File")
    os.system ("rm ssh")
    print("[*] Removed SSH File")
print("[*] Reset Success")
print ("[*] Created By Pmk")
