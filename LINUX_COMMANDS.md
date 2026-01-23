# 🤖 USLUBA BOT - EXACT LINUX COMMANDS

## 🎯 SERVER'DA BOT ISHGA TUSHIRISH (Qadam bo'yma)

### **1️⃣ QADAM - SSH bilan server'ga ulanish**

```bash
# SSH orqali server'ga kirish
ssh -i /path/to/key.pem user@your_server_ip

# Yoki parol bilan
ssh user@your_server_ip
```

---

### **2️⃣ QADAM - System yangilash**

```bash
# Update package lists
sudo apt update

# Upgrade existing packages
sudo apt upgrade -y

# Install required packages
sudo apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    wget \
    nano
```

---

### **3️⃣ QADAM - Foydalanuvchi yaratish**

```bash
# Usluba foydalanuvchisini yaratish
sudo useradd -m -s /bin/bash usluba

# Qo'shimcha: sudo access berish (ixtiyoriy)
sudo usermod -aG sudo usluba

# Foydalanuvchiga o'tish
sudo su - usluba
```

---

### **4️⃣ QADAM - Bot direktoriyasini yaratish**

```bash
# Direktoriyani yaratish
sudo mkdir -p /home/usluba/usluba_bot

# Permissions o'rnatish
sudo chown -R usluba:usluba /home/usluba/usluba_bot

# Tekshirish
ls -la /home/usluba/
```

---

### **5️⃣ QADAM - Bot kodi yuklab olish**

#### **A. GitHub'dan (Git bilan):**

```bash
# Usluba foydalanuvchiga o'tish (agar o'tmagan bo'lsangiz)
sudo su - usluba

# GitHub'dan clone qilish
cd /home/usluba/usluba_bot
git clone https://github.com/YOUR_USERNAME/YOUR_BOT_REPO.git .

# Yoki fork qilgan bo'lsa
git clone https://github.com/YOUR_USERNAME/usluba_bot.git .
```

#### **B. Local'dan file'larni kopya qilish:**

```bash
# Lokal kompyutardan server'ga transfer (Windows PowerShell):
scp -r "c:\path\to\Usluba_bot\*" usluba@YOUR_SERVER_IP:/home/usluba/usluba_bot/

# Yoki Linux/Mac:
scp -r /path/to/Usluba_bot/* usluba@YOUR_SERVER_IP:/home/usluba/usluba_bot/
```

---

### **6️⃣ QADAM - Virtual Environment yaratish va activate**

```bash
# Server'da usluba bo'ling
sudo su - usluba

# Virtual environment yaratish
python3 -m venv /home/usluba/usluba_bot/venv

# Faollashtirish (Bash shell'da)
source /home/usluba/usluba_bot/venv/bin/activate

# Pip yangilash
pip install --upgrade pip setuptools wheel
```

---

### **7️⃣ QADAM - Dependencies o'rnatish**

```bash
# Virtual environment faol bo'lishi kerak
source /home/usluba/usluba_bot/venv/bin/activate

# Requirements o'rnatish
pip install -r /home/usluba/usluba_bot/requirements.txt

# Tekshirish
pip list | grep -E "telegram|dotenv"
```

---

### **8️⃣ QADAM - .env faylni sozlash**

```bash
# Root bo'lib, .env yaratish
sudo nano /home/usluba/usluba_bot/.env
```

**Quyidagilarni yozing va Ctrl+X, Y, Enter:**

```ini
# 🔑 BOT TOKEN (BotFather'dan olingan)
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN_HERE

# 🐛 DEBUG MODE
DEBUG=False
```

**Token olish uchun:**
1. Telegram'da [@BotFather](https://t.me/BotFather) ga yozing
2. `/newbot` yozib, bot nomini bering
3. Token qilip oling va yuqoriga qo'ying

---

### **9️⃣ QADAM - Manual Test (xatirgina burja)**

```bash
# Usluba foydalanuvchiga o'tish
sudo su - usluba

# Direktoriyaga o'tish
cd /home/usluba/usluba_bot

# Virtual environment active qilish
source venv/bin/activate

# Bot'ni ishga tushirish (test uchun)
python3 UslubaBot.py

# Telegram'da /start yozib test qilish
# Bot'ni to'xtatish: Ctrl+C
```

---

### **🔟 QADAM - Systemd Service o'rnatish**

#### **A. Service faylini server'ga kopya qilish:**

```bash
# Usluba bo'ling
sudo su - usluba

# Bot fayllarini tekshirish
ls -la /home/usluba/usluba_bot/

# Service faylini root bo'lib kopya qilish
sudo cp /home/usluba/usluba_bot/usluba-bot.service /etc/systemd/system/
```

#### **B. Permissions o'rnatish:**

```bash
# Service faylining permissions
sudo chmod 644 /etc/systemd/system/usluba-bot.service

# Tekshirish
ls -la /etc/systemd/system/usluba-bot.service
```

#### **C. Service'ni enable qilish:**

```bash
# Systemd yangilash
sudo systemctl daemon-reload

# Service'ni enable qilish (boot'da auto-start)
sudo systemctl enable usluba-bot

# Tekshirish
sudo systemctl is-enabled usluba-bot
# Chiqadi: enabled
```

---

### **1️⃣1️⃣ QADAM - Bot'ni ishga tushirish**

```bash
# Bot'ni ishga tushirish
sudo systemctl start usluba-bot

# Status ko'rish (running bo'lishi kerak)
sudo systemctl status usluba-bot

# Ctrl+Q bilan chiqish
```

---

### **1️⃣2️⃣ QADAM - Logs kuzatish**

```bash
# Real-time logs (live kuzatish)
sudo journalctl -u usluba-bot -f

# Oxirgi 100 qator
sudo journalctl -u usluba-bot -n 100

# Faqat ERRORS
sudo journalctl -u usluba-bot -p err

# Bot file log'ni ko'rish
tail -f /home/usluba/usluba_bot/usluba_bot.log
```

---

## 📋 ASOSIY BOSHQARUV BUYRUQLARI

### **Bot Lifecycle**

```bash
# Bot'ni ishga tushirish
sudo systemctl start usluba-bot

# Bot'ni to'xtatish
sudo systemctl stop usluba-bot

# Bot'ni qayta ishga tushirish (yangilanish uchun)
sudo systemctl restart usluba-bot

# Bot status'ini ko'rish
sudo systemctl status usluba-bot

# Bot'ni boot'da auto-start qilish
sudo systemctl enable usluba-bot

# Bot'ni boot'da auto-start'dan o'chirish
sudo systemctl disable usluba-bot

# Hozirgi holat tekshirish
sudo systemctl is-active usluba-bot
```

### **Logs va Monitoring**

```bash
# Hozirgi logs (real-time)
sudo journalctl -u usluba-bot -f

# Oxirgi N qator
sudo journalctl -u usluba-bot -n 50

# Faqat ERROR level logs
sudo journalctl -u usluba-bot -p err

# Vaqt oralig'ida logs
sudo journalctl -u usluba-bot --since "1 hour ago"
sudo journalctl -u usluba-bot --since "2024-01-22" --until "2024-01-23"

# Bot file log (service direktoryasida)
tail -100 /home/usluba/usluba_bot/usluba_bot.log
```

### **System Monitoring**

```bash
# CPU, RAM usage
htop
# Yoki
top

# Disk space
df -h

# Process info
ps aux | grep usluba

# Network connections
netstat -an | grep ESTABLISHED
```

---

## 🔄 BOT YANGILANISHI

```bash
# GitHub'dan yangi code'ni pull qilish
sudo su - usluba
cd /home/usluba/usluba_bot
git pull origin main

# Yoki manual kopya
sudo scp new_file.py usluba@server:/home/usluba/usluba_bot/

# Dependencies yangilash (agar kerak bo'lsa)
source venv/bin/activate
pip install -r requirements.txt --upgrade

# Bot qayta ishlash
sudo systemctl restart usluba-bot

# Tekshirish
sudo systemctl status usluba-bot
```

---

## 🛠️ MUAMMOLARNI HAL QILISH

### **Bot crash bo'lsa yoki ishlap turmasa:**

```bash
# 1. Status ko'rish
sudo systemctl status usluba-bot

# 2. Logs ko'rish (oxirgi 50 qator)
sudo journalctl -u usluba-bot -n 50

# 3. .env tekshirish (token to'g'rimi?)
cat /home/usluba/usluba_bot/.env

# 4. Virtual environment tekshirish
ls -la /home/usluba/usluba_bot/venv/bin/

# 5. Manual ishga tushirish (xatolikni ko'rish uchun)
sudo su - usluba
cd /home/usluba/usluba_bot
source venv/bin/activate
python3 UslubaBot.py

# 6. Restart qilish
sudo systemctl restart usluba-bot
```

### **CPU/Memory yuqori bo'lsa:**

```bash
# Real-time monitoring
htop

# Process qidirish
ps aux | grep UslubaBot

# Restart qilish (resource free bo'ladi)
sudo systemctl restart usluba-bot
```

### **Port xatosi bo'lsa:**

```bash
# Port'dan ishlatilayotganini tekshirish
sudo lsof -i :5000  # polling uchun kerak emas, shunchaki info

# Restart service
sudo systemctl restart usluba-bot
```

---

## 🚀 AUTOMATED SETUP (Bitta quyun script bilan)

```bash
# Download setup script
sudo su - usluba
wget https://raw.githubusercontent.com/YOUR_USERNAME/usluba_bot/main/setup.sh

# Executable qilish
sudo chmod +x setup.sh

# Ishga tushirish
sudo ./setup.sh

# Token qo'shish
sudo nano /home/usluba/usluba_bot/.env

# Restart
sudo systemctl restart usluba-bot
```

---

## 🔐 SECURITY TIPS

```bash
# .env fayl permissions (faqat usluba ko'rsin)
sudo chmod 600 /home/usluba/usluba_bot/.env

# Bot direktoriyasi permissions
sudo chmod 755 /home/usluba/usluba_bot

# Log fayli permissions
sudo chmod 644 /home/usluba/usluba_bot/usluba_bot.log

# Firewall: 22 (SSH) o'chiq bo'lsin, boshqa port'lar yopiq
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow out 443  # HTTPS uchun
sudo ufw enable
```

---

## 📊 SERVER'DA BOT MONITORING SETUP

```bash
# Har kuni log tozalash (crontab)
crontab -e

# Quyidagi qatorni qo'ying:
# 0 3 * * * tail -1000 /home/usluba/usluba_bot/usluba_bot.log > /home/usluba/usluba_bot/usluba_bot.log.tmp && mv /home/usluba/usluba_bot/usluba_bot.log.tmp /home/usluba/usluba_bot/usluba_bot.log
```

---

## ✅ FINAL CHECKLIST

```bash
# 1. Python3 o'rnatilganmi?
python3 --version

# 2. Requirements o'rnatilganmi?
pip list | grep telegram

# 3. .env tayyor?
cat /home/usluba/usluba_bot/.env

# 4. Bot manual ishlayabdi?
cd /home/usluba/usluba_bot && source venv/bin/activate && python3 UslubaBot.py &

# 5. Service o'rnatilganmi?
systemctl list-unit-files | grep usluba

# 6. Service running?
sudo systemctl status usluba-bot

# 7. Logs ko'rinibdi?
sudo journalctl -u usluba-bot -n 10

# 8. Auto-start enabled?
sudo systemctl is-enabled usluba-bot
```

---

## 🎯 QISQA SUMMARY

```bash
# Server tayyorlash va bot ishga tushirish (minimal):

# 1. Dependencies
sudo apt update && sudo apt install -y python3 python3-pip python3-venv git

# 2. User va direktory
sudo useradd -m -s /bin/bash usluba
sudo mkdir -p /home/usluba/usluba_bot

# 3. Kodni kopya
scp -r bot_files/* usluba@server:/home/usluba/usluba_bot/

# 4. Virtual env va dependencies
sudo su - usluba
cd /home/usluba/usluba_bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. .env sozlash
nano /home/usluba/usluba_bot/.env
# BOT_TOKEN=YOUR_TOKEN

# 6. Service
sudo cp usluba-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable usluba-bot
sudo systemctl start usluba-bot

# 7. Tekshirish
sudo systemctl status usluba-bot
```

---

**🎉 Bot 24/7 ishlaydi va server reboot'da avtomatik ishlayb tashlanadi!**
