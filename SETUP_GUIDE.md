# 🤖 USLUBA BOT - Ubuntu/Debian Server Setup Guide

## 📋 Qadam bo'yma Tavsiyanomasi

### **1️⃣ QADAM - Server tayyorlash**

```bash
# System yangilash
sudo apt update && sudo apt upgrade -y

# Kerakli paketlar o'rnatish
sudo apt install -y python3 python3-pip python3-venv git curl wget

# Foydalanuvchi yaratish (usluba)
sudo useradd -m -s /bin/bash usluba
sudo usermod -aG sudo usluba

# Direktoryani yaratish
sudo mkdir -p /home/usluba/usluba_bot
sudo chown -R usluba:usluba /home/usluba/usluba_bot
```

---

### **2️⃣ QADAM - Bot kodi yuklab olish**

```bash
# Usluba foydalanuvchiga o'tish
sudo su - usluba

# GitHub yoki local'dan kodni kopya qilish
cd /home/usluba/usluba_bot
# Agar GitHub da bo'lsa:
# git clone <your-repo-url> .

# Yoki fayllarni manual nusxalash:
# scp UslubaBot.py usluba@server:/home/usluba/usluba_bot/
# scp requirements.txt usluba@server:/home/usluba/usluba_bot/
# scp .env usluba@server:/home/usluba/usluba_bot/
```

---

### **3️⃣ QADAM - Virtual Environment yaratish**

```bash
# Virtual environment yaratish
python3 -m venv venv

# Faollashtirish
source venv/bin/activate

# Pip yangilash
pip install --upgrade pip

# Dependencies o'rnatish
pip install -r requirements.txt

# Tekshirish (chiqadi: ✅ Bot muvaffaqiyatli ishga tushdi!)
python3 UslubaBot.py &
```

---

### **4️⃣ QADAM - .env fayl sozlash**

```bash
# .env faylni yaratish va token qo'shish
nano .env
```

**Quyidagi matnni qo'ying:**
```
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
DEBUG=False
```

Token olish: [@BotFather](https://t.me/BotFather) ga /newbot yozib token oling.

---

### **5️⃣ QADAM - Systemd Service o'rnatish**

```bash
# Root bo'lib, service faylini kopya qilish
sudo cp /home/usluba/usluba_bot/usluba-bot.service /etc/systemd/system/

# Permissions o'rnatish
sudo chmod 644 /etc/systemd/system/usluba-bot.service

# Systemd yangilash
sudo systemctl daemon-reload

# Serveni ishga tushirish
sudo systemctl start usluba-bot

# Boot-da avtomatik ishlash uchun
sudo systemctl enable usluba-bot

# Status tekshirish
sudo systemctl status usluba-bot
```

---

### **6️⃣ QADAM - Loglarni kuzatish**

```bash
# Real-time log kuzatish
sudo journalctl -u usluba-bot -f

# Oxirgi 50 log qatorini ko'rish
sudo journalctl -u usluba-bot -n 50

# Bot faylining logini ko'rish
cat /home/usluba/usluba_bot/usluba_bot.log
```

---

### **7️⃣ QADAM - Bot foydalanuvchiga admin huquqlari**

```bash
# Bot loglarini o'qiy oladigan qilish
sudo chmod 755 /home/usluba/usluba_bot
sudo chmod 644 /home/usluba/usluba_bot/usluba_bot.log
```

---

## 🔧 Foydalanish Buyruqlari

### **Sozlamalar va boshqaruv:**

```bash
# Bot holatini tekshirish
sudo systemctl status usluba-bot

# Bot ishini to'xtatish
sudo systemctl stop usluba-bot

# Bot qayta ishga tushirish
sudo systemctl restart usluba-bot

# Logs o'qish (real-time)
sudo journalctl -u usluba-bot -f

# Botni o'chirib, qayta ishga tushirish (xatolik uchun)
sudo systemctl restart usluba-bot

# Server reboot bo'lsa, bot avtomatik ishlashini tekshirish
sudo systemctl is-enabled usluba-bot
# Chiqadi: enabled ✅
```

---

## ⚠️ Muammolarni hal qilish

### **Bot ishlamayotgan bo'lsa:**

```bash
# 1. Logs tekshirish
sudo journalctl -u usluba-bot -n 100

# 2. Token to'g'ri kelganini tekshirish
cat /home/usluba/usluba_bot/.env

# 3. Virtual environment faol ekanini tekshirish
ls -la /home/usluba/usluba_bot/venv/bin/

# 4. Manual ishga tushirish (xatolikni ko'rish uchun)
cd /home/usluba/usluba_bot
source venv/bin/activate
python3 UslubaBot.py

# 5. Service faylini tekshirish
cat /etc/systemd/system/usluba-bot.service
```

---

### **Memory yoki CPU masalasi bo'lsa:**

```bash
# Monitoring
htop
# Yoki:
top

# Resource limitlarini sozlash (usluba-bot.service fayl):
# MemoryLimit=200M
# CPUQuota=50%
```

---

### **Auto-restart test qilish (5 soniyada qayta ishlashini):**

```bash
# Service faylini tahrirla
sudo nano /etc/systemd/system/usluba-bot.service

# Quyidagilarni tekshirish:
# Restart=always
# RestartSec=10  (10 soniyada qayta ishlaydi)

# Saqlash va qayta boshlash
sudo systemctl daemon-reload
sudo systemctl restart usluba-bot
```

---

## 🚀 Yangilanishi bo'lsa:

```bash
# 1. Yangi kodni git pull qilish
cd /home/usluba/usluba_bot
git pull origin main

# 2. Requirements yangilash
source venv/bin/activate
pip install -r requirements.txt --upgrade

# 3. Bot qayta ishga tushirish
sudo systemctl restart usluba-bot

# 4. Status tekshirish
sudo systemctl status usluba-bot
```

---

## 🔐 Xavfsizlik Maslahatlar

1. **Token ochiq bo'lmasin**: .env fayl `.gitignore` da bo'lsin
2. **Foydalanuvchi huquqlari**: Faqat kerakli huquqlarni ber
3. **Firewall**: 5000+ portni yopib qol (bot polling ishlatadi)
4. **Backup**: Bot fayllarini doming backup qil

---

## ✅ Tekshirish Checklist

- [ ] Python3 o'rnatilgan
- [ ] requirements.txt o'rnatilgan
- [ ] .env fayl qo'yilgan va token to'g'ri
- [ ] Virtual environment ishga tushdi
- [ ] Bot manual ishga tushdi
- [ ] Systemd service o'rnatilgan
- [ ] `sudo systemctl status usluba-bot` ✅ runing
- [ ] Logs ko'rinadi
- [ ] Auto-restart enabled
- [ ] Server reboot'da bot qayta ishlaydi

---

## 📞 Qo'shimcha Yordam

Bot uchun qo'llanma: [Telegram Bot API](https://core.telegram.org/bots)
Python-telegram-bot: [Docs](https://python-telegram-bot.readthedocs.io/)
