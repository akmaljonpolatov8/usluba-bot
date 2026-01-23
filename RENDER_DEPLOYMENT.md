# 🚀 USLUBA BOT - Render Webhook Deployment Guide

## 📋 Overview

This guide explains how to deploy USLUBA BOT on **Render** using **webhook mode** (event-driven, not polling).

**Polling vs Webhook:**
- **Polling** (old): Bot asks Telegram "any messages?" every 1-2 seconds. ❌ Inefficient
- **Webhook** (new): Telegram pushes messages to your server. ✅ Efficient, serverless-friendly

---

## 🔧 Prerequisites

1. **Telegram Bot** (created via BotFather): `BOT_TOKEN` ready
2. **Render Account**: Free tier available at [render.com](https://render.com)
3. **Git Repository**: Your code pushed to GitHub
4. **Random Secret Token**: For webhook validation (use online UUID generator)

---

## 📝 Step 1: Prepare Environment Variables

### Create `.env.production` (for Render):

```env
BOT_TOKEN=YOUR_ACTUAL_BOT_TOKEN_HERE
PUBLIC_URL=https://your-app-name.render.com
WEBHOOK_SECRET=your-random-secret-token-here
PORT=10000
```

**How to get values:**
- `BOT_TOKEN`: From BotFather on Telegram
- `PUBLIC_URL`: Will be assigned by Render (e.g., `https://usluba-bot.render.com`)
- `WEBHOOK_SECRET`: Generate random string: [uuidgenerator.net](https://www.uuidgenerator.net/)
- `PORT`: Any port in 10000-10100 range (Render requirement)

---

## 🌐 Step 2: Deploy on Render

### 2.1 Create New Web Service

1. Log in to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Select your GitHub repository containing the bot code
4. Fill in details:
   - **Name**: `usluba-bot` (or your preferred name)
   - **Environment**: `Python 3.11`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python webhook_app.py`
   - **Instance Type**: Free tier (sufficient for bot)

### 2.2 Add Environment Variables

In Render dashboard:
1. Go to your Web Service settings
2. Click **"Environment"**
3. Add these environment variables:

```
BOT_TOKEN                   → Your actual bot token
PUBLIC_URL                  → https://YOUR_SERVICE_NAME.render.com
WEBHOOK_SECRET              → Your random secret token
PORT                        → 10000
```

### 2.3 Deploy

1. Click **"Deploy"** button
2. Wait for build to complete (2-3 minutes)
3. Service URL will appear: `https://your-app-name.render.com`

---

## ✅ Step 3: Verify Webhook is Set

After deployment, webhook should automatically set on startup.

**To manually verify:**

```bash
curl -X GET https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getWebhookInfo
```

Expected response:
```json
{
  "ok": true,
  "result": {
    "url": "https://your-app-name.render.com/telegram",
    "has_custom_certificate": false,
    "pending_update_count": 0,
    "ip_address": "..."
  }
}
```

---

## 🧪 Step 4: Test Bot

1. Open Telegram
2. Search for your bot (by username from BotFather)
3. Send `/start`
4. Bot should respond with welcome message + emoji keyboard

---

## 📊 Monitoring & Logs

### View Logs in Render:

1. Go to your Web Service in Render Dashboard
2. Click **"Logs"** tab
3. Real-time logs appear:
   ```
   2024-01-15 10:23:45 - INFO - ✅ Webhook set to: https://usluba-bot.render.com/telegram
   2024-01-15 10:24:12 - INFO - 📥 Received message from user_id: 123456789
   ```

### Local Testing:

Test webhook locally before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export BOT_TOKEN="your_token"
export PUBLIC_URL="http://localhost:8000"
export WEBHOOK_SECRET="test_secret"
export PORT=8000

# Run webhook server
python webhook_app.py
```

Then in another terminal, test health endpoint:
```bash
curl http://localhost:8000/
# Output: OK
```

---

## 🔐 Security Best Practices

1. **Never commit `.env`** - Keep it in `.gitignore`
2. **Use strong `WEBHOOK_SECRET`** - Generate random 32+ character string
3. **Validate all headers** - webhook_app.py checks `X-Telegram-Bot-Api-Secret-Token`
4. **Monitor logs** - Watch Render logs for suspicious activity
5. **Limit handler scopes** - Only necessary handlers are registered

---

## 📁 File Structure for Render

```
Usluba_bot/
├── webhook_app.py           ✅ Main entry point for Render
├── UslubaBot_improved.py    ✅ Bot logic (imported by webhook_app.py)
├── requirements.txt         ✅ Dependencies (includes aiohttp)
├── .env.example             ✅ Template (copy to .env for local testing)
├── README.md
└── (documentation files)
```

---

## 🛠️ Troubleshooting

### **Problem: "BOT_TOKEN belgilanmagan"**
- **Solution**: Set `BOT_TOKEN` in Render environment variables

### **Problem: "PUBLIC_URL belgilanmagan"**
- **Solution**: Set `PUBLIC_URL` to your Render service URL

### **Problem: Bot not responding**
- **Solution**: 
  1. Check logs: `curl https://api.telegram.org/bot<TOKEN>/getWebhookInfo`
  2. Verify webhook URL matches `PUBLIC_URL`
  3. Restart service in Render Dashboard

### **Problem: 403 Forbidden on webhook**
- **Solution**: `WEBHOOK_SECRET` in Render ≠ sent by Telegram. Verify exact match.

---

## 🎯 File Explanations

### **webhook_app.py**
- **Purpose**: aiohttp web server for webhook
- **Endpoints**:
  - `GET /` → Returns "OK" (health check)
  - `POST /telegram` → Receives Telegram updates, validates secret, processes them
- **On Startup**: Sets webhook via Telegram API
- **On Shutdown**: Graceful cleanup

### **UslubaBot_improved.py**
- **Purpose**: All bot handler logic
- **create_app()**: Factory function returning configured Application
- **Handlers**: /start, /help, trick selection, formation selection, messages, errors
- **Imported by**: webhook_app.py

### **requirements.txt**
```
python-telegram-bot==20.7     ← Telegram API wrapper
python-dotenv==1.0.0          ← Environment variable loading
aiohttp==3.9.0                ← Async HTTP server
```

---

## 📞 Support

If bot stops responding:
1. Check Render logs for errors
2. Verify environment variables are set
3. Restart the service (free tier may auto-sleep after 15 min inactivity)

---

## ✨ Next Steps

1. ✅ Push code to GitHub
2. ✅ Create Render account
3. ✅ Deploy web service
4. ✅ Set environment variables
5. ✅ Test bot in Telegram
6. ✅ Monitor logs

**Your bot will now run 24/7 on Render! 🎉**
