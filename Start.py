import os
import time
import shutil
import subprocess
from colorama import Fore, Style, init

# Colorama başlat
init(autoreset=True)

# ASCII Sanatı
ascii_art = """
 ██▓    ▄▄▄      ▓█████▄  ▒█████   ██▀███  ▓█████ ▒██   ██▒
▓██▒   ▒████▄    ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒▓█   ▀ ▒▒ █ █ ▒░
▒██░   ▒██  ▀█▄  ░██   █▌▒██░  ██▒▓██ ░▄█ ▒▒███   ░░  █   ░
▒██░   ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▒▓█  ▄  ░ █ █ ▒ 
░██████▒▓█   ▓██▒░▒████▓ ░ ████▓▒░░██▓ ▒██▒░▒████▒▒██▒ ▒██▒
░ ▒░▓  ░▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒ ░ ░▓ ░
░ ░ ▒  ░ ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░ ░ ░  ░░░   ░▒ ░
  ░ ░    ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░░   ░    ░    ░    ░  
    ░  ░     ░  ░   ░        ░ ░     ░        ░  ░ ░    ░  
                  ░                                        
"""

data_text = "Ladorex X PSYCHOLOGY"

def clear_screen():
    os.system("clear")  # Termux için clear komutunu kullanıyoruz

def get_terminal_size():
    """ Terminal genişliğini ve yüksekliğini al """
    size = shutil.get_terminal_size((80, 25))  # Varsayılan genişlik ve yükseklik
    return size.columns, size.lines

def print_centered(text, color):
    """ Terminalin tam ortasına yazı yazdırır """
    width, height = get_terminal_size()
    lines = text.strip().split("\n")
    empty_lines = (height - len(lines)) // 2  # ASCII'yi tam ortalamak için boş satır sayısı

    print("\n" * empty_lines, end="")  # Yukarıya boşluk bırak
    for line in lines:
        print(color + line.center(width) + Style.RESET_ALL)
    
    print(Fore.YELLOW + data_text.center(width) + Style.RESET_ALL)

def main():
    switch = True
    clear_screen()

    print(Fore.CYAN + "5 saniye sonra Başlatılacak..." + Style.RESET_ALL)

    for _ in range(5):  # 5 saniye boyunca yanıp sönme efekti
        clear_screen()
        
        # Mor ve Kırmızı arasında geçiş yap
        if switch:
            print_centered(ascii_art, Fore.MAGENTA)
        else:
            print_centered(ascii_art, Fore.RED)

        switch = not switch
        time.sleep(1)

    clear_screen()
    print(Fore.GREEN + "WebLadorex.py başlatılıyor..." + Style.RESET_ALL)
    time.sleep(1)

    # WebLadorex.py dosyasını çalıştır
    if os.path.exists("WebLadorex.py"):
        subprocess.call(["python", "Webladorex.py"])  # Termux uyumlu subprocess.call
    else:
        print(Fore.RED + "Hata: WebLadorex.py dosyası bulunamadı!" + Style.RESET_ALL)
    
    input("\nDevam etmek için Enter'a bas...")  # CMD'nin otomatik kapanmasını engeller

if __name__ == "__main__":
    main()
