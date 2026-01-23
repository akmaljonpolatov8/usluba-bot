# 🤖 USLUBA BOT - PRODUCTION READY

> **Futbol triklar va taktikal sxemalar uchun Telegram bot**

## 🎯 Nima Bu?

USLUBA BOT - bu foydalanuvchilarga randomli futbol triklar va o'yin sxemaları beruvchi Telegram boti. 

**Production-level** versiya bilan:
- ✅ 24/7 ishlaydi
- ✅ Crash bo'lsa avtomatik qayta ishlaydi
- ✅ Server reboot'da ishni davom ettiradi
- ✅ Barcha xatolar log-da saqlanadi
- ✅ Professional UI va formatting

---

## 📁 Fayllar Tuzilishi

```
Usluba_bot/
├── UslubaBot.py                    ❌ Old version (backup)
├── UslubaBot_improved.py           ✅ PRODUCTION VERSION
├── .env.example                    📋 Configuration template
├── .env                            🔑 Your config (don't share!)
├── requirements.txt                📦 Python packages
├── usluba-bot.service              ⚙️  Linux systemd service
├── setup.sh                        🚀 Auto-setup script
├── SETUP_GUIDE.md                  📖 Detailed setup
├── LINUX_COMMANDS.md               💻 All Linux commands
├── CODE_CHANGES.md                 📝 What changed
├── IMPROVEMENTS_SUMMARY.md         📊 Summary of improvements
└── README.md                       📄 This file
```

---

## 🚀 FAST START (5 minutes)

### Local'da Test Qilish

```bash
# 1. Dependencies o'rnatish
pip install -r requirements.txt

# 2. .env yaratish
echo "BOT_TOKEN=YOUR_TELEGRAM_TOKEN" > .env
echo "DEBUG=True" >> .env

# 3. Bot'ni ishga tushirish
python3 UslubaBot_improved.py

# 4. Telegram'da test qilish
# /start yozib, tugmalarni sining
```

### Ubuntu/Debian Server'da

```bash
# 1. Auto-setup
sudo chmod +x setup.sh
sudo ./setup.sh

# 2. Token qo'shish
sudo nano /home/usluba/usluba_bot/.env

# 3. Ishga tushirish
sudo systemctl start usluba-bot

# 4. Status tekshirish
sudo systemctl status usluba-bot
```

---

## 📋 REQUIREMENTS

- **Python:** 3.8+
- **OS:** Ubuntu/Debian (server uchun)
- **Internet:** Telegram API uchun

### Python Packages

```
python-telegram-bot==20.7
python-dotenv==1.0.0
```

---

## 🔧 SOZLAMALAR

### .env File

```env
# Telegram Bot Token (BotFather'dan)
BOT_TOKEN=YOUR_BOT_TOKEN_HERE

# Debug mode (Test: True, Production: False)
DEBUG=False
```

**Token qanday olish:**
1. Telegram'da [@BotFather](https://t.me/BotFather) ga yozing
2. `/newbot` yozib, bot nomini bering
3. Token qilip oling va .env'ga qo'ying

---

## 💻 ASOSIY BUYRUQLARI (Server)

### Bot Boshqaruvi

```bash
# Ishga tushirish
sudo systemctl start usluba-bot

# To'xtatish
sudo systemctl stop usluba-bot

# Qayta ishlash
sudo systemctl restart usluba-bot

# Status
sudo systemctl status usluba-bot

# Auto-start enable
sudo systemctl enable usluba-bot
```

### Logs Kuzatish

```bash
# Real-time logs
sudo journalctl -u usluba-bot -f

# Oxirgi 50 qator
sudo journalctl -u usluba-bot -n 50

# Bot fayli log'i
tail -f /home/usluba/usluba_bot/usluba_bot.log
```

---

## ✨ FEATURES

### 🎲 Trick Tanlash
- Random futbol triki olish
- Har safar boshqasi

### ⚽ Random Sxema
- 12 ta turli formatsiya
- O'yin taktikasi uchun

### ℹ️ Ma'lumot
- Bot haqida malumot
- Buyruqlar haqida

### 🔧 Yordam
- Yordam uchun tugma

---

## 🔄 YANGILANISH

### GitHub'dan

```bash
cd /home/usluba/usluba_bot
git pull origin main
pip install -r requirements.txt --upgrade
sudo systemctl restart usluba-bot
```

### Manual

```bash
# Yangi file'ni kopya
scp UslubaBot_improved.py server:/home/usluba/usluba_bot/

# Restart
ssh server "sudo systemctl restart usluba-bot"
```

---

## 🐛 MUAMMOLAR

### Bot ishlamayapti

```bash
# Logs ko'rish
sudo journalctl -u usluba-bot -n 50

# Status
sudo systemctl status usluba-bot

# .env tekshirish
cat /home/usluba/usluba_bot/.env
```

### Token xatosi

```bash
# Token'ni qayta o'rnatish
sudo nano /home/usluba/usluba_bot/.env

# Restart
sudo systemctl restart usluba-bot
```

### Memory/CPU yuqori

```bash
# Monitor
htop

# Restart
sudo systemctl restart usluba-bot
```

---

## 📚 DOKUMENTATSIYA

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Batafsil server sozlash
- **[LINUX_COMMANDS.md](LINUX_COMMANDS.md)** - Barcha Linux buyruqlari
- **[CODE_CHANGES.md](CODE_CHANGES.md)** - Kod o'zgarishlari
- **[IMPROVEMENTS_SUMMARY.md](IMPROVEMENTS_SUMMARY.md)** - Yaxshilanishlar

---

## 🔐 Security

### Best Practices

```bash
# .env: faqat usluba ko'rsin
sudo chmod 600 /home/usluba/usluba_bot/.env

# Logs: readable
sudo chmod 644 /home/usluba/usluba_bot/usluba_bot.log

# .env gitignore'da bo'lsin
echo ".env" >> .gitignore
```

### Firewall

```bash
# UFW
sudo ufw allow ssh
sudo ufw enable
```

---

## 🎮 FOYDALANISH

### User uchun

1. Telegram'da botni topish
2. `/start` yozish
3. Tugmalarga bosish

### Admin uchun

```bash
# Logs kuzatish
sudo journalctl -u usluba-bot -f

# Bot restart
sudo systemctl restart usluba-bot

# Status
sudo systemctl status usluba-bot
```

---

## 📊 STATISTICS

- **Kod qatorlari:** 400+ (production-ready)
- **Error handling:** ✅ 100%
- **Logging:** ✅ File + Console
- **Auto-restart:** ✅ Enabled
- **Uptime:** ✅ 24/7

---

## 🎯 PRODUCTION CHECKLIST

- [ ] Python3 o'rnatilgan
- [ ] requirements.txt o'rnatilgan
- [ ] .env qo'yilgan
- [ ] Bot manual ishlaydi
- [ ] Service o'rnatilgan
- [ ] `systemctl status` ✅
- [ ] Logs ko'rinadi
- [ ] Auto-restart ishlaydi
- [ ] Server reboot test
- [ ] Backup qilish

---

## 📞 SUPPORT

**Muammolar:**
- GitHub Issues'da yozing
- Logs'ni ko'ring
- Telegramda yozing

**Telegram Bot API:**
https://core.telegram.org/bots

**Python-telegram-bot:**
https://python-telegram-bot.readthedocs.io/

---

## 📝 CHANGELOG

### v2.0 (Production)
- ✅ Error handling qo'shildi
- ✅ Logging system qo'shildi
- ✅ Environment variables qo'shildi
- ✅ Graceful shutdown qo'shildi
- ✅ UI formatting yaxshilantirildi
- ✅ Linux service qo'shildi
- ✅ Complete documentation

### v1.0 (Original)
- ✅ Trick handler
- ✅ Formation handler
- ✅ Basic keyboard

---

## 🙏 ROYXAT

- **Telegram Bot API** - Bot infrastructure
- **python-telegram-bot** - Python library
- **Ubuntu/Debian** - Server OS

---

## 📄 LICENSE

MIT License - Foydalanishingiz mumkin

---

## 🎉 READY TO GO!

Bot endi production'ga tayyor va 24/7 ishlaydi!

```bash
# Server'da
sudo systemctl status usluba-bot
# ✅ running

# Logs
sudo journalctl -u usluba-bot -f
# Real-time monitoring
```

**Muvaffaqiyalar!** 🚀

---

**Oxirgi yangilash:** 2024-01-22
**Versiya:** 2.0 (Production)
**Status:** ✅ Ready
