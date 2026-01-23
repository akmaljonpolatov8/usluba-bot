# ⚡ USLUBA BOT - Quick Start: Deploy to Render in 5 Minutes

## 🎯 The Goal
Deploy your Telegram bot on **Render** so it runs **24/7 without your computer**.

---

## ⏱️ 5-Minute Deployment

### Step 1: GitHub (1 minute)
```bash
git add .
git commit -m "add webhook deployment"
git push
```

### Step 2: Get Render Account (1 minute)
- Go to https://render.com
- Sign up with GitHub account
- Authorize GitHub access

### Step 3: Create Service on Render (2 minutes)

1. Log in to Render Dashboard
2. Click **"New +"** → **"Web Service"**
3. Select your GitHub repo
4. Fill in:
   - **Name**: `usluba-bot`
   - **Environment**: `Python 3.11`
   - **Build**: `pip install -r requirements.txt`
   - **Start**: `python webhook_app.py`
   - **Plan**: Free tier (select free)
5. Click **"Create Web Service"**

### Step 4: Add Environment Variables (1 minute)

In Render Dashboard, go to your service → **Environment** tab. Add:

```
BOT_TOKEN            = your_actual_token_here
PUBLIC_URL           = https://usluba-bot.render.com
WEBHOOK_SECRET       = abc123random456token789secret
PORT                 = 10000
```

**Getting values:**
- `BOT_TOKEN`: From BotFather on Telegram
- `PUBLIC_URL`: Will show in Render dashboard (replace `usluba-bot` with your service name)
- `WEBHOOK_SECRET`: Generate at [uuidgenerator.net](https://www.uuidgenerator.net/)

Save environment variables → Auto-deploys!

### Step 5: Wait & Test (Happens automatically!)

1. Render builds your app (1-2 minutes)
2. You see **"Live"** status ✅
3. Open Telegram, find your bot
4. Send `/start` → Bot responds! 🎉

---

## ✅ That's It!

Your bot now runs **24/7** on Render. No computer needed!

---

## 🧪 Quick Verification

### Is it working?
```bash
curl https://usluba-bot.render.com/
# Should return: OK
```

### Is webhook set?
```bash
curl https://api.telegram.org/bot<YOUR_TOKEN>/getWebhookInfo
# Should show your PUBLIC_URL
```

### Test in Telegram
- `/start` → Welcome message ✅
- Click trick → Shows trick ✅
- Click formation → Shows formation ✅
- Send text → Responds ✅

---

## 📊 What Changed?

| File | What Changed |
|------|--------------|
| `webhook_app.py` | ✨ NEW - Webhook server for Render |
| `requirements.txt` | Added `aiohttp==3.9.0` |
| `UslubaBot_improved.py` | Already refactored (has `create_app()`) |
| `.env.example` | Updated with webhook variables |

---

## 🆘 Troubleshooting

### Bot not responding?
1. Check Render **Logs** tab for errors
2. Verify `BOT_TOKEN` is set correctly
3. Click "Restart" on service

### "BOT_TOKEN belgilanmagan"?
- Go to Render → Environment
- Add missing variable
- Restart

### Webhook error in logs?
- Verify `PUBLIC_URL` matches your service name
- Verify `WEBHOOK_SECRET` is set
- Restart

---

## 📚 Need More Details?

Full guides created:
- [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) - Detailed step-by-step
- [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) - Verification steps
- [WEBHOOK_REFACTORING_SUMMARY.md](WEBHOOK_REFACTORING_SUMMARY.md) - What changed

---

## 🎉 Enjoy!

Your bot is now:
- ✅ Running 24/7
- ✅ Responding instantly
- ✅ Scalable on Render
- ✅ Production-ready

**Need help? Check the full documentation files above!**
