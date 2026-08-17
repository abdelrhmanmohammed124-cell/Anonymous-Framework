#!/bin/bash
echo "[*] Setting up Anonymous Framework..."
pkg update -y
pkg install python git nmap apache2 -y
pkg install unstable-repo -y
pkg install dsniff -y
cp anonymous.py /data/data/com.termux/files/usr/bin/anonymous
chmod +x /data/data/com.termux/files/usr/bin/anonymous
chmod +x anonymous.py
echo "[+] Done! You can now type 'anonymous' from anywhere."

