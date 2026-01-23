#!/usr/bin/env python3
"""
🤖 USLUBA BOT - Professional Telegram Bot
✅ Production-ready version with logging, error handling, and 24/7 support
"""

import logging
import os
import signal
import sys
import asyncio
from contextlib import asynccontextmanager
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import random

# ============================================================================
# 🔧 CONFIGURATION
# ============================================================================

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"

# ============================================================================
# 📋 LOGGING SETUP
# ============================================================================

logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('usluba_bot.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# ============================================================================
# 🎲 DATA CONFIGURATION
# ============================================================================

TRICKS = [
    "🧠 O'z usluba\n\n👉 Yordamga tayanmay O'ziz ishlashni boshlang",
    "🐊 Krakadil\n\n👉 Bahtsiz holatdan ciqish uchun asosiy",
    "🍀 Buyog'i omad\n\n👉 Omadni kuzatib yurmas, ishlangiz"
]

FORMATIONS = [
    "4-4-2", "4-3-3", "4-2-1-3", "3-5-2",
    "5-3-2", "3-4-4", "4-3-1-2", "4-3-2-1",
    "3-1-4-2", "3-4-3", "4-1-4-1", "3-2-4-1"
]

# ============================================================================
# ⌨️ KEYBOARDS
# ============================================================================

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["🎲 Trick tanlash", "⚽ Random sxema"],
        ["ℹ️ Ma'lumot", "🔧 Yordam"]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)

# ============================================================================
# 🎯 COMMAND HANDLERS
# ============================================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /start - Bot boshlanishi
    """
    try:
        user = update.effective_user
        logger.info(f"👤 New user started: {user.id} ({user.first_name})")
        
        await update.message.reply_text(
            "✅ *USLUBA BOT* 🎯\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "👋 Assalomu alaykum! JIGA\n\n"
            "🎮 Futbol triklar va taktikal sxemalar\n\n"
            "📌 *Asosiy funktsiyalar:*\n"
            "🎲 Randomli trick tanlash\n"
            "⚽ Futbol sxemalariga o'rin\n"
            "ℹ️ Bot haqida ma'lumot\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "👇 Quyidagi tugmalardan birini tanlang:",
            reply_markup=MAIN_KEYBOARD,
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"❌ Error in start handler: {e}", exc_info=True)
        await update.message.reply_text(
            "❌ Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring."
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    /help - Yordam va ma'lumot
    """
    try:
        logger.info(f"📖 Help requested by {update.effective_user.id}")
        
        await update.message.reply_text(
            "ℹ️ *BOT HAQIDA MA'LUMOT* 🤖\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🎯 *Maqsadi:*\n"
            "Futbol o'yinchaklari va taktikali sxemalar\n\n"
            "🎲 *Trick tanlash:*\n"
            "Bugun uchun randomli trick olish\n\n"
            "⚽ *Random sxema:*\n"
            "O'yin uchun turli formatsiyalar\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "💡 Tugmalarga bosib funksiyalardan foydalaning.\n"
            "🆘 Muammo bo'lsa /help ni foydalaning",
            reply_markup=MAIN_KEYBOARD,
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"❌ Error in help handler: {e}", exc_info=True)


async def trick_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    🎲 Random trick tanlash
    """
    try:
        user_id = update.effective_user.id
        selected = random.choice(TRICKS)
        logger.info(f"🎲 Trick requested by user {user_id}")
        
        await update.message.reply_text(
            f"🔥 *BUGUNGI TRICK* 🎯\n\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"{selected}\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🍀 Omad sizga samolyor! 💪",
            parse_mode="Markdown",
            reply_markup=MAIN_KEYBOARD
        )
    except Exception as e:
        logger.error(f"❌ Error in trick_handler: {e}", exc_info=True)
        await update.message.reply_text(
            "❌ Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.",
            reply_markup=MAIN_KEYBOARD
        )


async def formation_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    ⚽ Random futbol sxemasi
    """
    try:
        user_id = update.effective_user.id
        scheme = random.choice(FORMATIONS)
        logger.info(f"⚽ Formation requested by user {user_id}")
        
        await update.message.reply_text(
            f"⚽ *BUGUNGI SXEMA* 🏆\n\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"📍 Formatsiya: `{scheme}`\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🔥 GO JIGAR! G'alaba sizga! 💪⚽",
            parse_mode="Markdown",
            reply_markup=MAIN_KEYBOARD
        )
    except Exception as e:
        logger.error(f"❌ Error in formation_handler: {e}", exc_info=True)
        await update.message.reply_text(
            "❌ Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.",
            reply_markup=MAIN_KEYBOARD
        )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Matnli xabarlarni ushlash va tugmalarga javob berish
    """
    try:
        text = update.message.text
        user_id = update.effective_user.id
        logger.debug(f"📨 Message from {user_id}: {text}")

        handlers = {
            "🎲 Trick tanlash": trick_handler,
            "⚽ Random sxema": formation_handler,
            "ℹ️ Ma'lumot": help_command,
            "🔧 Yordam": help_command,
        }

        handler = handlers.get(text)
        if handler:
            await handler(update, context)
        else:
            await update.message.reply_text(
                "❓ Bu buyruq tanilmadi.\n\n"
                "👇 Iltimos, quyidagi tugmalardan birini tanlang:",
                reply_markup=MAIN_KEYBOARD
            )
    except Exception as e:
        logger.error(f"❌ Error in message_handler: {e}", exc_info=True)
        await update.message.reply_text(
            "❌ Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.",
            reply_markup=MAIN_KEYBOARD
        )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """
    Umumiy xatolik handler
    """
    logger.error(f"⚠️ Update {update} caused error {context.error}", exc_info=context.error)


# ============================================================================
# 🛑 GRACEFUL SHUTDOWN
# ============================================================================

# ============================================================================
# 📦 CREATE_APP FUNCTION (For webhook + polling)
# ============================================================================

def create_app() -> Application:
    """
    Create and configure the Application with all handlers.
    
    Returns:
        Application: Configured telegram Application
    """
    if not TOKEN:
        logger.critical("❌ BOT_TOKEN belgilanmagan! .env faylni tekshiring.")
        sys.exit(1)

    # Application builder
    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Message handler
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    )

    # Error handler
    app.add_error_handler(error_handler)

    logger.info("✅ Application configured with all handlers")
    return app


# ============================================================================
# ▶️ POLLING MODE (Local Testing)
# ============================================================================

async def main():
    """
    Botni ishga tushirish (Polling mode for local testing)
    """
    try:
        logger.info("🚀 USLUBA BOT ISHGA TUSHMOQDA... (Polling Mode)")
        logger.info(f"⏰ Vaqti: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        app = create_app()
        
        logger.info("📡 Polling rejimida ishlayabdi...")
        logger.info("✅ Bot ishga tushgan!")
        
        await app.run_polling(allowed_updates=Update.ALL_TYPES)

    except Exception as e:
        logger.critical(f"❌ KRITIK XATOLIK: {e}", exc_info=True)
        sys.exit(1)



# ============================================================================
# 🎯 ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        logger.info("🤖 USLUBA BOT BOSHLANMOQDA...")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("⌨️ Keyboard interrupt. Shutting down...")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"❌ Boshlanishda xatolik: {e}", exc_info=True)
        sys.exit(1)
