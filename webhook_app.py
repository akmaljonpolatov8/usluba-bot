#!/usr/bin/env python3
"""
🌐 USLUBA BOT - Webhook Server for Render Deployment
✅ aiohttp-based webhook with secret token validation
"""

import logging
import os
import sys
import json
from aiohttp import web
from dotenv import load_dotenv
from telegram import Update

# Import create_app from the bot module
from UslubaBot_improved import create_app

# ============================================================================
# 🔧 CONFIGURATION
# ============================================================================

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
PUBLIC_URL = os.getenv("PUBLIC_URL")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
PORT = int(os.getenv("PORT", "8000"))

# ============================================================================
# 📋 LOGGING SETUP
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('webhook.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# ============================================================================
# 🌐 WEBHOOK HANDLERS
# ============================================================================

app_instance = None  # Global Application instance


async def health_check(request):
    """
    GET / - Health check endpoint
    """
    return web.Response(text="OK", status=200)


async def webhook_handler(request):
    """
    POST /telegram - Webhook endpoint for Telegram updates
    Validates X-Telegram-Bot-Api-Secret-Token header
    """
    try:
        # Validate secret token
        secret_token = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
        if secret_token != WEBHOOK_SECRET:
            logger.warning(f"❌ Invalid secret token: {secret_token}")
            return web.Response(status=403, text="Forbidden")

        # Parse update
        data = await request.json()
        update = Update.de_json(data, app_instance.bot)

        # Process update
        await app_instance.process_update(update)

        return web.Response(status=200, text="OK")

    except Exception as e:
        logger.error(f"❌ Webhook error: {e}", exc_info=True)
        return web.Response(status=500, text="Internal Server Error")


# ============================================================================
# 🚀 SERVER STARTUP
# ============================================================================

async def on_startup(app):
    """
    Initialize bot and set webhook on startup
    """
    global app_instance
    
    try:
        logger.info("🚀 WEBHOOK SERVER STARTING...")

        # Validate configuration
        if not TOKEN:
            logger.critical("❌ BOT_TOKEN belgilanmagan!")
            sys.exit(1)
        if not PUBLIC_URL:
            logger.critical("❌ PUBLIC_URL belgilanmagan!")
            sys.exit(1)
        if not WEBHOOK_SECRET:
            logger.critical("❌ WEBHOOK_SECRET belgilanmagan!")
            sys.exit(1)

        # Create application
        app_instance = create_app()
        await app_instance.initialize()
        await app_instance.start()

        # Set webhook
        webhook_url = f"{PUBLIC_URL}/telegram"
        await app_instance.bot.set_webhook(
            url=webhook_url,
            secret_token=WEBHOOK_SECRET,
            allowed_updates=["message", "callback_query"]
        )

        logger.info(f"✅ Webhook set to: {webhook_url}")
        logger.info(f"📡 Webhook server running on port {PORT}")

    except Exception as e:
        logger.critical(f"❌ Startup error: {e}", exc_info=True)
        sys.exit(1)


async def on_shutdown(app):
    """
    Cleanup on shutdown
    """
    try:
        logger.warning("🛑 WEBHOOK SERVER SHUTTING DOWN...")
        
        if app_instance:
            await app_instance.stop()
            await app_instance.shutdown()

        logger.info("✅ Webhook server stopped gracefully")

    except Exception as e:
        logger.error(f"❌ Shutdown error: {e}", exc_info=True)


# ============================================================================
# 🎯 MAIN ENTRY POINT
# ============================================================================

def main():
    """
    Start webhook server
    """
    try:
        logger.info("🤖 USLUBA BOT WEBHOOK SERVER BOSHLANMOQDA...")

        # Create web app
        app = web.Application()

        # Add routes
        app.router.add_get("/", health_check)
        app.router.add_post("/telegram", webhook_handler)

        # Add startup/shutdown handlers
        app.on_startup.append(on_startup)
        app.on_shutdown.append(on_shutdown)

        # Run server
        logger.info(f"🌐 Server running on 0.0.0.0:{PORT}")
        web.run_app(app, host="0.0.0.0", port=PORT)

    except Exception as e:
        logger.critical(f"❌ Server error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
