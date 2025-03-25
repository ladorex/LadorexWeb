import os
import socket
import whois
import requests
import random
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse

# User-Agent listesini yükle
def load_user_agents():
    try:
        with open("data/agents.txt", "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except:
        return ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"]

USER_AGENTS = load_user_agents()

# IP listesi
def load_ips():
    try:
        with open("data/ips.txt", "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except:
        return []

IPS = load_ips()

# Menü
def menu():
    print("\n--- LADOREX PSYCHOLOGY BİLGİ TOPLAMA ARACI ---")
    print("1. DNS Bilgisi")
    print("2. IP Adresi ve Lokasyon")
    print("3. Web Teknolojileri")
    print("4. Robots.txt & Sitemap")
    print("5. IP Sorgulama (Detaylı)")
    print("6. Rastgele IP Üret")
    print("7. Rastgele User-Agent Üret")
    print("8. Site Durum Kontrolü")
    print("9. Site Ekran Görüntüsü Al")
    print("10. Yapılandırma")
    print("11. Çıkış")
    return input("\nSeçiminizi yapın (1-11): ")

# Yapılandırma - Settings.py dosyasını çalıştır
def yapılandırma():
    try:
        # settings/settings.py dosyasını çalıştırma
        settings_path = os.path.join(os.getcwd(), "settings", "settings.py")
        if os.path.exists(settings_path):
            exec(open(settings_path).read())
            print("[+] Yapılandırma başarıyla tamamlandı.")
        else:
            print("[-] settings/settings.py dosyası bulunamadı.")
    except Exception as e:
        print(f"[-] Yapılandırma işlemi sırasında hata oluştu: {e}")

# DNS Bilgisi
def dns_info():
    domain = "ladorex.xyz"
    try:
        w = whois.whois(domain)
        print(f"\nDNS Sunucuları: {w.name_servers}")
    except Exception as e:
        print(f"[-] DNS Bilgisi Alınamadı: {e}")

# IP Adresi ve Lokasyon
def ip_info():
    domain = "ladorex.xyz"
    try:
        ip = socket.gethostbyname(domain)
        print(f"\nIP Adresi: {ip}")
    except Exception as e:
        print(f"[-] IP Bilgisi Alınamadı: {e}")

# Web Teknolojileri
def web_technologies():
    domain = "ladorex.xyz"
    try:
        response = requests.get(f"http://{domain}")
        if "WordPress" in response.text:
            print("\n[+] CMS: WordPress")
        elif "Joomla" in response.text:
            print("\n[+] CMS: Joomla")
        else:
            print("\n[-] CMS Tespit Edilemedi")
    except Exception as e:
        print(f"[-] Web Teknolojileri Alınamadı: {e}")

# Robots.txt & Sitemap
def robots_and_sitemap():
    domain = "ladorex.xyz"
    try:
        robots = requests.get(f"http://{domain}/robots.txt")
        sitemap = requests.get(f"http://{domain}/sitemap.xml")
        print("\n[+] Robots.txt Durumu:", "Var" if robots.status_code == 200 else "Yok")
        print("[+] Sitemap.xml Durumu:", "Var" if sitemap.status_code == 200 else "Yok")
    except Exception as e:
        print(f"[-] Robots.txt & Sitemap Alınamadı: {e}")

# IP Sorgulama (Detaylı)
def ip_lookup():
    ip = input("\nSorgulanacak IP adresini girin: ")
    
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    
    try:
        print("\n[*] IP Bilgileri Çekiliyor...\n")
        
        # ipinfo.io API ile veri çekme
        response1 = requests.get(f"https://ipinfo.io/{ip}/json", headers=headers)
        data1 = response1.json()
        
        # ip-api.com API ile veri çekme
        response2 = requests.get(f"http://ip-api.com/json/{ip}?fields=66842623", headers=headers)
        data2 = response2.json()

        # Çıktıyı düzenli gösterme
        print(f"📍 **IP Adresi:** {data1.get('ip', 'Bilinmiyor')}")
        print(f"🌍 **Ülke:** {data1.get('country', 'Bilinmiyor')} ({data2.get('countryCode', 'N/A')})")
        print(f"🏙 **Şehir:** {data1.get('city', 'Bilinmiyor')}")
        print(f"🗺 **Bölge:** {data2.get('regionName', 'Bilinmiyor')} ({data2.get('region', 'N/A')})")
        print(f"⏳ **Zaman Dilimi:** {data2.get('timezone', 'Bilinmiyor')}")
        print(f"📡 **ISP:** {data2.get('isp', 'Bilinmiyor')}")
        print(f"🏢 **Organizasyon:** {data2.get('org', 'Bilinmiyor')}")
        print(f"🔗 **AS:** {data2.get('as', 'Bilinmiyor')}")
        print(f"📌 **Koordinatlar:** {data1.get('loc', 'Bilinmiyor')}")  # Enlem, Boylam
        print(f"🔄 **Ters DNS:** {data2.get('reverse', 'Bilinmiyor')}")
        print(f"🛜 **Mobil Bağlantı:** {'Evet' if data2.get('mobile', False) else 'Hayır'}")
        print(f"🔒 **VPN/Proxy Kullanımı:** {'Evet' if data2.get('proxy', False) else 'Hayır'}")
        print(f"👨‍💻 **Hosting:** {'Evet' if data2.get('hosting', False) else 'Hayır'}")
        
    except Exception as e:
        print(f"[-] IP Sorgulama Başarısız: {e}")

# Rastgele IP Üretme
def random_ip():
    if IPS:
        print(f"\n[+] Rastgele IP: {random.choice(IPS)}")
    else:
        print("[-] IP listesi bulunamadı!")

# Rastgele User-Agent Üretme
def random_user_agent():
    print(f"\n[+] Rastgele User-Agent: {random.choice(USER_AGENTS)}")

# Site Durum Kontrolü
def site_checker():
    url = "https://ladorex.xyz"
    try:
        response = requests.get(url, timeout=5)
        print(f"[+] {url} Durum: {'Açık' if response.status_code == 200 else 'Kapalı'}")
    except:
        print(f"[-] {url} Kapalı!")

# Site Ekran Görüntüsü Alma
def site_screenshot():
    url = "https://ladorex.xyz"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.save_screenshot("screenshot.png")
    driver.quit()
    print("[+] Ekran görüntüsü kaydedildi: screenshot.png")

# Ana Program
while True:
    choice = menu()
    if choice == '10': yapılandırma()  # Yapılandırma seçeneği
    elif choice == '11': break
    else:
        functions = [dns_info, ip_info, web_technologies, robots_and_sitemap, ip_lookup, random_ip, random_user_agent, site_checker, site_screenshot]
        if choice in map(str, range(1, 10)): 
            functions[int(choice)-1]()
        else:
            print("[-] Geçersiz Seçim!")
