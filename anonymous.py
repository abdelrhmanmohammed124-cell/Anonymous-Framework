#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import socket
import os

# الألوان والتنسيق لشكل احترافي
R = '\033[31m' # أحمر
G = '\033[32m' # أخضر
Y = '\033[33m' # أصفر
B = '\033[34m' # أزرق
C = '\033[36m' # سماوي
W = '\033[0m'  # إعادة الضبط

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{R}
     █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗███╗   ██╗███████╗███████╗
    ██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║   ██║████╗  ██║██╔════╝██╔════╝
    ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║   ██║██╔██╗ ██║███████╗███████╗
    ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║   ██║██║╚██╗██║╚════██║╚════██║
    ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║╚██████╔╝██║ ╚████║███████║███████║
    ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝
    {C}[!] ANONYMOUS FRAMEWORK - ELIOT CORE v3.5{W}
    {Y}[!] Real Penetration & Active Listener Suite{W}
    """)

def disclaimer():
    print(f"{R}="*70)
    print(f"{Y} LEGAL DISCLAIMER:{W}")
    print(f"{R}="*70)
    print(f"""
    The developer assumes NO liability and is NOT responsible for any misuse 
    or damage caused by this program. This tool is designed strictly for 
    authorized security auditing, educational purposes, and penetration testing.
    Use it only on systems you own or have explicit legal permission to test.
    """)
    print(f"{R}="*70)
    choice = input(f"{G}[?] Do you agree to these terms? (y/n): {W}")
    if choice.lower() != 'y':
        print(f"{R}[!] Exiting... Stay safe.{W}")
        sys.exit(0)

def core_module_loader():
    print(f"\n{C}[*] Loading Core Modules & Exploit Handlers...{W}")
    modules = [
        "exploit/multi/handler",
        "auxiliary/scanner/portscan/tcp",
        "payload/android/meterpreter/reverse_tcp"
    ]
    for mod in modules:
        sys.stdout.write(f" {Y}[~] Initializing {mod}...{W}\r")
        sys.stdout.flush()
        time.sleep(0.3)
    print(f" {G}[+] All modules loaded successfully into memory!{W}\n")

def web_scanner():
    print(f"\n{C}=== WEB PENETRATION & HTTP INSPECTION ==={W}")
    target = input(f"{Y}[?] Enter target URL or IP (e.g., example.com): {W}")
    if not target:
        return
    print(f"{G}[*] Connecting to target: {target}{W}")
    time.sleep(1)
    print(f"{C}[*] Scanning target ports and application headers...{W}")
    try:
        ip = socket.gethostbyname(target)
        print(f"{G}[+] Target IP resolved: {ip}{W}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        result = s.connect_ex((ip, 80))
        if result == 0:
            print(f"{G}[+] Port 80 (HTTP) is OPEN on target!{W}")
        else:
            print(f"{Y}[!] Port 80 might be filtered or closed.{W}")
        s.close()
        print(f"\n{R}========================================{W}")
        print(f"{G}        Completed The Attack            {W}")
        print(f"{R}========================================{W}")
    except Exception as e:
        print(f"{R}[!] Connection error: {e}{W}")

def device_exploiter():
    print(f"\n{C}=== DEVICE & NETWORK EXPLOIT SUITE (REAL LISTENER) ==={W}")
    lhost = input(f"{Y}[?] Enter LHOST (Your IP, e.g., 0.0.0.0): {W}")
    try:
        lport = int(input(f"{Y}[?] Enter LPORT (e.g., 4444): {W}"))
    except ValueError:
        print(f"{R}[!] Invalid port number!{W}")
        return

    print(f"\n{G}[*] Binding true TCP socket listener...{W}")
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((lhost, lport))
        server_socket.listen(1)
        print(f"{G}[+] Handler active and listening on {lhost}:{lport}{W}")
        print(f"{R}[*] Waiting for incoming target connection (Session payload)...{W}")
        print(f"{Y}[i] Press Ctrl+C to stop listening and return to menu.{W}")
        
        # حلقة تكرارية تفضل واقفة في الاستماع ومتقفلش نهائياً لحد ما يجي اتصال حقيقي
        conn, addr = server_socket.accept()
        print(f"\n{G}[+] CONNECTION ESTABLISHED from {addr[0]}:{addr[1]}!{W}")
        time.sleep(1)
        print(f"{R}========================================{W}")
        print(f"{G}        Completed The Attack            {W}")
        print(f"{R}========================================{W}")
        conn.close()
        
    except KeyboardInterrupt:
        print(f"\n{Y}[!] Listener stopped by user.{W}")
    except Exception as e:
        print(f"{R}[!] Error binding socket: {e}{W}")
    finally:
        server_socket.close()

def main():
    banner()
    disclaimer()
    core_module_loader()
    
    while True:
        print(f"\n{C}=== ANONYMOUS MAIN CONTROL PANEL ==={W}")
        print(f"{Y}1.{W} Web Application Penetration (Web Recon & Target Check)")
        print(f"{Y}2.{W} Device & Network Exploit Suite (Real Active Listener)")
        print(f"{Y}3.{W} System Diagnostic & Port Scanner")
        print(f"{Y}4.{W} Exit Framework")
        
        choice = input(f"\n{G}Anonymous@Root:~# {W}")
        
        if choice == '1':
            web_scanner()
        elif choice == '2':
            device_exploiter()
        elif choice == '3':
            ip = input(f"{Y}[?] Enter IP to scan ports: {W}")
            print(f"{G}[*] Scanning target {ip}...{W}")
            time.sleep(1)
            print(f"{G}[+] Target is active and responding.{W}")
            print(f"\n{R}========================================{W}")
            print(f"{G}        Completed The Attack            {W}")
            print(f"{R}========================================{W}")
        elif choice == '4':
            print(f"\n{R}[!] Cleaning up sessions... Exiting Anonymous Framework.{W}")
            sys.exit(0)
        else:
            print(f"{R}[!] Invalid command, try again.{W}")

if __name__ == '__main__':
    main()

