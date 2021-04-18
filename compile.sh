#!/bin/bash
if [ $USER != "root" ] ; then
  echo "Run it As Root!"
  exit
fi
echo "Enter A Name For Naming The Environment Variable: "
#Pmk
read name
REQUIRED_PKG="shc"
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "installed")
echo Checking for $REQUIRED_PKG: $PKG_OK
if [ "" = "$PKG_OK" ]; then
  echo "[*] $REQUIRED_PKG Not Detected"

  echo "[*] Installing $REQUIRED_PKG "
  apt-get --yes install $REQUIRED_PKG
fi
shc -f ssh
echo "[*] Compiled Successfully"
mv ssh.x /bin/$name
echo "[*] Moved To Bin Directory"
echo "[*] Creating Environment Variable"
export $name=/bin/"$name"
echo "[*] Done!"
echo "[*] Created By Pmk"