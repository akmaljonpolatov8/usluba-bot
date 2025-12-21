import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

TRICKS = [
    "🧠 O‘z usluba",
    "🐊 Krakadil",
    "🍀 Buyog‘i omad"
]

FORMATIONS = [
    "4-4-2", "4-3-3", "4-2-1-3", "3-5-2", "5-3-2",
    "3-4-3", "4-3-1-2", "4-3-2-1", "4-1-4-1"
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🎲 Trick tanlash"],
        ["⚽ Random sxema"]
    ]
    await update.message.reply_text(
        "👋 Assalomu alaykum! JIGAR\n\n"
        "🎮 *Usluba bot* ga xush kelibsiz!\n\n"
        "👇 Quyidan tanla JIGAR:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
        parse_mode="Markdown"
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🎲 Trick tanlash":
        trick = random.choice(TRICKS)
        await update.message.reply_text(f"🔥 BUGUNGI TRICK:\n\n👉 *{trick}*", parse_mode="Markdown")

    elif text == "⚽ Random sxema":
        formation = random.choice(FORMATIONS)
        await update.message.reply_text(f"⚽ BUGUNGI SXEMA:\n\n👉 *{formation}*", parse_mode="Markdown")


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN topilmadi!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("🤖 Usluba bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
