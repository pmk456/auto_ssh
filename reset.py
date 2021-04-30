#!/usr/bin/python
import os
ip_file = ".ip.txt"
ssh_file = "ssh"
if ip_file in os.listdir():
  print("[*] Deleting ip.txt File")
  os.system("rm .ip.txt")
else:
  print("[*] Ip File Not Detected")
if ssh_file in os.listdir():
  print("[*] Deleting SSH File")
  os.system("rm ssh")
else:
  print("[*] SSH File Not Found")
if ip_file not in os.listdir() and ssh_file not in os.listdir():
  print("[*] No Files Detected")
  print("[*] So Nothing Deleted")
else:
  print("[*] Reset Success")
print("Created By Pmk")
