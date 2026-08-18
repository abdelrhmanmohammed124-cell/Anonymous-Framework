#!/bin/bash
pkg update && pkg upgrade -y
pkg install python git nmap apache2 dsniff -y
pip install requests urllib3
cp anonymous.py /data/data/com.termux/files/usr/bin/anonymous
chmod +x /data/data/com.termux/files/usr/bin/anonymous
chmod +x anonymous.py
echo "[+] Setup Complete! Type 'anonymous' to launch."

