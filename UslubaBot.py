from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import os

TOKEN = os.getenv("BOT_TOKEN")


# 🎲 TRICKLAR (sening berganlaring)
TRICKS = [
    "🧠 O‘z usluba\n\n👉",
    "🐊 Krakadil\n\n👉 ",
    "🍀 Buyog‘i omad\n\n👉"
]

# ⚽ SXEMALAR
FORMATIONS = [
    "4-4-2", "4-3-3", "4-2-1-3", "3-5-2",
    "5-3-2", "3-4-4", "4-3-1-2", "4-3-2-1",
    "3-1-4-2", "3-4-3", "4-1-4-1", "3-2-4-1"
]

# 🎛 ASOSIY MENYU
MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        ["🎲 Trick tanlash"],
        ["⚽ Random sxema"]
    ],
    resize_keyboard=True
)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Assalomu alaykum! JIGA\n\n"
        "🎮 Welcom to *Usluba bot*\n\n"
        "📌 Pack ochishdan oldin:\n"
        "• Trick tanla\n"
        "• Random sxema ol\n\n"
        "👇 Tugmalardan birini bos",
        reply_markup=MAIN_KEYBOARD,
        parse_mode="Markdown"
    )

# 🎲 Trick tanlash
async def trick_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    selected = random.choice(TRICKS)
    await update.message.reply_text(
        f"🔥 *BUGUNGI TRICK*\n\n{selected}\n\n🍀 Omad!",
        parse_mode="Markdown"
    )

# ⚽ Random sxema
async def formation_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    scheme = random.choice(FORMATIONS)
    await update.message.reply_text(
        f"⚽ *BUGUNGI SXEMA*\n\n👉 `{scheme}`\n\n🔥 GO JIGAR",
        parse_mode="Markdown"
    )

# 🧠 Matnlarni ushlash (tugmalar uchun)
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🎲 Trick tanlash":
        await trick_handler(update, context)
    elif text == "⚽ Random sxema":
        await formation_handler(update, context)
    else:
        await update.message.reply_text(
            "❗ Iltimos, pastdagi tugmalardan foydalan 👇",
            reply_markup=MAIN_KEYBOARD
        )

# ▶️ BOTNI ISHGA TUSHIRISH
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("🤖 Usluba bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
