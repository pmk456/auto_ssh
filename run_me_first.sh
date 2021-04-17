#!/bin/bash
clear
echo "\e[32m"
                     
echo "\e[32m[*] Checking For Root..."
if [ $USER != "root" ]
 then
        echo "\e[31m[*] This Script Must Run As Root"
        echo "\e[31m[*] Created By Pmk"
        exit
else
	echo "\e[32m[*] Root Detected!"
fi
echo "\e[32m[*] Checking For Internet..."
sleep 3
if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
  echo "\e[32m[*] Connected!"
  sleep 2
else
  echo "\e[31m[*] This Script Requires Internet To Run!"
  echo "\e[31m[*] Exiting..."
  exit
fi
echo "\e[32m[*] Checking For Python3..."
sleep 3
if ! hash python; then
        echo "\e[31m[*] Python 3 Not Detected"
        echo "\e[31m[*] Installing Python3..."
        sleep 1 
        apt-get install python3
else
        echo "\e[32m[*] Python3 Detected"
fi
