# ✅ USLUBA BOT - Render Webhook Deployment Checklist

## 📋 Pre-Deployment Verification

### Code & Files
- [ ] `UslubaBot_improved.py` exists and has `create_app()` function
- [ ] `webhook_app.py` exists with aiohttp server
- [ ] `requirements.txt` includes: `python-telegram-bot==20.7`, `python-dotenv==1.0.0`, `aiohttp==3.9.0`
- [ ] `.env.example` has all variables documented
- [ ] `.gitignore` includes `.env` (don't commit secrets!)
- [ ] All files pushed to GitHub

### Local Testing
- [ ] `pip install -r requirements.txt` succeeds
- [ ] `python UslubaBot_improved.py` runs with `BOT_TOKEN` set (polling mode works)
- [ ] Bot responds to `/start`, `/help` commands
- [ ] Trick selection responds with emoji + trick name
- [ ] Formation selection responds with emoji + formation
- [ ] Regular messages are handled correctly
- [ ] No Python syntax errors in webhook_app.py

---

## 🌐 Render Deployment Setup

### Create Render Web Service
- [ ] Log in to [Render Dashboard](https://dashboard.render.com)
- [ ] Click **"New +"** → **"Web Service"**
- [ ] Connect GitHub repository
- [ ] Configure service:
  - [ ] **Name**: `usluba-bot` (or preferred name)
  - [ ] **Environment**: Select **Python 3.11**
  - [ ] **Build Command**: `pip install -r requirements.txt`
  - [ ] **Start Command**: `python webhook_app.py`
  - [ ] **Instance Type**: Free tier selected

### Set Environment Variables
In Render Dashboard → Your Service → **Environment** section:

- [ ] `BOT_TOKEN` = Your actual bot token from BotFather
- [ ] `PUBLIC_URL` = Exactly like: `https://usluba-bot.render.com` (replace `usluba-bot` with your service name)
- [ ] `WEBHOOK_SECRET` = Random secret token (use [uuidgenerator.net](https://www.uuidgenerator.net/))
- [ ] `PORT` = `10000` (or any 10000-10100 range)

### Deploy
- [ ] Click **"Create Web Service"** or **"Deploy"**
- [ ] Watch build logs (should complete in 2-3 minutes)
- [ ] Deployment status shows **"Live"** ✅

---

## 🧪 Post-Deployment Verification

### Health Check
- [ ] Health endpoint returns 200:
  ```bash
  curl https://your-service.render.com/
  # Expected: OK
  ```

### Webhook Configuration Check
- [ ] Verify webhook was set by Telegram:
  ```bash
  curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getWebhookInfo
  ```
  - [ ] Response includes your `PUBLIC_URL`
  - [ ] URL ends with `/telegram`
  - [ ] `has_custom_certificate: false`
  - [ ] `ip_address` is populated

### Bot Functionality Test
- [ ] Open Telegram, find your bot
- [ ] Send `/start`
  - [ ] Bot responds with welcome message + emoji keyboard ✅
- [ ] Click trick emoji button
  - [ ] Bot displays selected trick ✅
- [ ] Click formation emoji button
  - [ ] Bot displays selected formation ✅
- [ ] Send regular text message
  - [ ] Bot responds with random message ✅
- [ ] Invalid command → Bot responds with help ✅

### Logs & Monitoring
- [ ] Check Render logs for errors
  - [ ] Go to Service → **Logs** tab
  - [ ] Should see: `✅ Webhook set to: https://your-service.render.com/telegram`
  - [ ] Should see: `📡 Webhook server running on port 10000`
  - [ ] No errors related to TOKEN or PUBLIC_URL

---

## 🔐 Security Checklist

- [ ] `.env` file is in `.gitignore` (not committed to repo)
- [ ] Real bot token is NOT in source code, only in Render environment
- [ ] `WEBHOOK_SECRET` is strong (random, 32+ characters)
- [ ] Webhook_app.py validates `X-Telegram-Bot-Api-Secret-Token` header
- [ ] No debug logs expose sensitive information
- [ ] Render service is not public on unnecessary ports

---

## 📊 Performance Baseline

After deployment, verify these metrics:

- [ ] **Response Time**: Bot responds to messages within 1-2 seconds
- [ ] **Memory Usage**: Monitor in Render dashboard (should be ~100-120 MB)
- [ ] **Log Volume**: Check that logs are reasonable (not flooding)
- [ ] **Uptime**: Service stays online 24/7 (monitor for 24 hours)
- [ ] **No Memory Leaks**: Logs don't show increasing memory over time

---

## 🚨 Troubleshooting Checklist

If bot doesn't work, check in order:

1. **Bot not responding at all?**
   - [ ] Check Render logs for startup errors
   - [ ] Verify `BOT_TOKEN` in Render environment variables
   - [ ] Restart service (Render dashboard → "Restart")
   - [ ] Check health: `curl https://your-service.render.com/`

2. **"BOT_TOKEN belgilanmagan" error?**
   - [ ] Go to Render Dashboard → Environment
   - [ ] Add missing `BOT_TOKEN` variable
   - [ ] Restart service

3. **"PUBLIC_URL belgilanmagan" error?**
   - [ ] Go to Render Dashboard → Environment
   - [ ] Add `PUBLIC_URL` matching your service name
   - [ ] Format: `https://your-service-name.render.com` (NO trailing slash)
   - [ ] Restart service

4. **403 Forbidden on webhook?**
   - [ ] Verify `WEBHOOK_SECRET` matches exactly in Render
   - [ ] Check that header is `X-Telegram-Bot-Api-Secret-Token` (exact spelling)
   - [ ] Restart service

5. **Webhook URL wrong in Telegram?**
   ```bash
   curl https://api.telegram.org/bot<TOKEN>/getWebhookInfo
   ```
   - [ ] If URL is wrong, check `PUBLIC_URL` in Render
   - [ ] Restart service to re-register webhook

6. **Free tier limitation (15-minute sleep)?**
   - [ ] Render free tier services auto-sleep after 15 min inactivity
   - [ ] First message will be slower (2-3 sec wake-up time)
   - [ ] Upgrade to Paid tier if faster response needed

---

## 🔄 Updating Code

After deployment, to push updates:

```bash
# 1. Make changes to code locally
# 2. Test with: python UslubaBot_improved.py
# 3. Commit and push to GitHub
# 4. Render auto-deploys (watch in Dashboard → Deployments)
# 5. Verify in logs after deployment completes
```

- [ ] Code changes tested locally first
- [ ] Git changes pushed to main branch
- [ ] Render auto-build triggered
- [ ] Deployment successful (Logs show no errors)
- [ ] Bot still responds after update

---

## 📞 Useful Commands

### Check webhook status:
```bash
TOKEN=your_token_here
curl https://api.telegram.org/bot$TOKEN/getWebhookInfo
```

### Delete webhook (if needed):
```bash
TOKEN=your_token_here
curl -X POST https://api.telegram.org/bot$TOKEN/deleteWebhook
```

### Set webhook manually (rarely needed):
```bash
TOKEN=your_token_here
URL=https://your-service.render.com/telegram
SECRET=your_secret_token
curl -X POST https://api.telegram.org/bot$TOKEN/setWebhook \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$URL\", \"secret_token\": \"$SECRET\"}"
```

---

## ✨ Success Criteria

Your deployment is **SUCCESSFUL** when:

- ✅ Render service shows **"Live"** status
- ✅ Health endpoint returns **OK**
- ✅ Webhook URL is correct in `getWebhookInfo`
- ✅ Bot responds to `/start` in Telegram
- ✅ All tricks and formations work
- ✅ Regular messages are handled
- ✅ Logs show no errors
- ✅ Bot runs 24/7 without stopping

---

## 📞 Support & Resources

- **Render Docs**: https://render.com/docs
- **python-telegram-bot Docs**: https://docs.python-telegram-bot.org/
- **Telegram Bot API**: https://core.telegram.org/bots/api
- **aiohttp Docs**: https://docs.aiohttp.org/

---

## 🎉 Congratulations!

Your bot is now deployed on Render and will:
- ✅ Run 24/7 without your computer
- ✅ Respond instantly via webhook (no polling delays)
- ✅ Handle multiple users simultaneously
- ✅ Auto-restart if any errors occur
- ✅ Scale horizontally if needed

**Your USLUBA BOT is LIVE! 🚀**
