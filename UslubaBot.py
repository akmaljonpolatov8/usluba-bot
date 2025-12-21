import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ======================
# ENV TOKEN
# ======================
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable topilmadi!")

# ======================
# DATA
# ======================
TRICKS = [
    "🧠 O‘z usluba",
    "🐊 Krakadil",
    "🍀 Buyog‘i omad"
]

FORMATIONS = [
    "4-4-2",
    "4-3-3",
    "4-2-1-3",
    "3-5-2",
    "5-3-2",
    "3-4-3",
    "4-1-4-1",
    "4-3-1-2"
]

# ======================
# HANDLERS
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🎲 Trick tanlash"],
        ["⚽ Random sxema"]
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "👋 Assalomu alaykum! JIGAR \n\n"
        "🎮 *Usluba bot* ga xush kelibsiz!\n\n"
        "📦 Pack ochishdan oldin trick tanlang yoki\n"
        "⚽ eFootball uchun random sxema oling 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🎲 Trick tanlash":
        trick = random.choice(TRICKS)
        await update.message.reply_text(
            f"🔥 *BUGUNGI USLUBA:*\n\n👉 {trick}\n\n🍀 Omad!",
            parse_mode="Markdown"
        )

    elif text == "⚽ Random sxema":
        formation = random.choice(FORMATIONS)
        await update.message.reply_text(
            f"⚽ *BUGUNGI SXEMA:*\n\n👉 {formation}",
            parse_mode="Markdown"
        )

    else:
        await update.message.reply_text(
            "❗ Tugmalardan foydalaning 👇"
        )

# ======================
# MAIN
# ======================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    print("🤖 Usluba bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
