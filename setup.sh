#!/bin/bash

###############################################################################
# 🤖 USLUBA BOT - Quick Setup Script for Ubuntu/Debian
# Ushbu script avtomatik server'ni sozlab beradi
###############################################################################

set -e  # Xatoga chiqsa, to'xta

echo "🚀 USLUBA BOT - Ubuntu/Debian Setup Script"
echo "============================================="

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Foydalanuvchi tekshirish
if [[ $EUID -ne 0 ]]; then
   echo -e "${RED}❌ Bu script root sifatida ishga tushishi kerak!${NC}"
   echo "Qayta urinib ko'ring: sudo ./setup.sh"
   exit 1
fi

echo -e "${GREEN}✅ Root sifatida running${NC}"

# 2. System yangilash
echo -e "${YELLOW}📦 System paketlarini yangilayabdi...${NC}"
apt update && apt upgrade -y

# 3. Python va kerakli paketlar
echo -e "${YELLOW}📦 Python3 va git o'rnatilmoqda...${NC}"
apt install -y python3 python3-pip python3-venv git curl wget

# 4. Usluba foydalanuvchi yaratish
if id "usluba" &>/dev/null; then
    echo -e "${YELLOW}⚠️  Foydalanuvchi 'usluba' allaqachon mavjud${NC}"
else
    echo -e "${YELLOW}👤 Foydalanuvchi 'usluba' yaratilmoqda...${NC}"
    useradd -m -s /bin/bash usluba
fi

# 5. Direktoriya yaratish va permission
echo -e "${YELLOW}📁 Direktoriya yaratilmoqda...${NC}"
mkdir -p /home/usluba/usluba_bot
chown -R usluba:usluba /home/usluba/usluba_bot

# 6. Bot kod nusxasi
echo -e "${YELLOW}📝 Bot fayllarini kopya qilish...${NC}"
# Bu yerda siz fayllarni kopya qilishingiz kerak yoki git clone qilishingiz kerak

# 7. Virtual environment
echo -e "${YELLOW}🐍 Virtual environment yaratilmoqda...${NC}"
sudo -u usluba python3 -m venv /home/usluba/usluba_bot/venv

# 8. Dependencies o'rnatish
echo -e "${YELLOW}📦 Python dependencies o'rnatilmoqda...${NC}"
sudo -u usluba /home/usluba/usluba_bot/venv/bin/pip install --upgrade pip
sudo -u usluba /home/usluba/usluba_bot/venv/bin/pip install -r /home/usluba/usluba_bot/requirements.txt

# 9. Systemd service
echo -e "${YELLOW}⚙️  Systemd service o'rnatilmoqda...${NC}"
cp /home/usluba/usluba_bot/usluba-bot.service /etc/systemd/system/
chmod 644 /etc/systemd/system/usluba-bot.service

systemctl daemon-reload
systemctl enable usluba-bot

# 10. Tugallash
echo -e "${GREEN}=============================================${NC}"
echo -e "${GREEN}✅ O'RNATISH TUGALLANDI!${NC}"
echo -e "${GREEN}=============================================${NC}"

echo ""
echo -e "${YELLOW}📌 Keyingi qadamlar:${NC}"
echo ""
echo "1️⃣  .env faylni qo'shish:"
echo "   sudo nano /home/usluba/usluba_bot/.env"
echo ""
echo "   Quyidagilarni qo'ying:"
echo "  8200442437:AAE6mnp35xPcvXdwFVd_qwJsEGwb_R5f-z4"
echo "   DEBUG=False"
echo ""
echo "2️⃣  Botni ishga tushirish:"
echo "   sudo systemctl start usluba-bot"
echo ""
echo "3️⃣  Status tekshirish:"
echo "   sudo systemctl status usluba-bot"
echo ""
echo "4️⃣  Loglarni kuzatish:"
echo "   sudo journalctl -u usluba-bot -f"
echo ""
echo -e "${GREEN}🎉 Tayyor! Bot 24/7 ishlaydi!${NC}"
