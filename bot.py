import telebot
from telebot import types
import yt_dlp
import os
import time
import datetime
import threading
import requests
import json
import random
from keep_alive import keep_alive

# ==========================================
# 💎 SYSTEM CONFIGURATION (ULTRA PREMIUM)
# ==========================================
API_TOKEN = '8349405998:AAEmx5B9_-QyiKNhESBIkTBr6ybsEmvdlAs'  # ⚠️ টোকেন
ADMIN_ID = 6243881362
CHANNEL_ID = -1002879589597
CHANNEL_LINK = 'https://t.me/RedX_Developer' # ⚠️ চ্যানেলের লিংক
NAGAD_NUMBER = "01812774257"
DEV_NAME = "Ayman Hasan Shaan"
BRAND = "Swygen IT"

# 🔐 JSONBIN DATABASE
JSONBIN_BIN_ID = "695bf73043b1c97be91b1114"
JSONBIN_API_KEY = "$2a$10$YAI7gdCaN8UY68wdmhrfT.NaQTMlsANujgmlhlchRUQJsHVgb6gka"
BIN_URL = f"https://api.jsonbin.io/v3/b/{JSONBIN_BIN_ID}"
HEADERS = {"Content-Type": "application/json", "X-Master-Key": JSONBIN_API_KEY}

bot = telebot.TeleBot(API_TOKEN)

# 📦 PREMIUM PLANS
PLANS = {
    "free": {"name": "Starter", "limit": 10, "price": 0, "days": 9999},
    "plan1": {"name": "Basic Daily  40 (7 Days)", "limit": 40, "price": 100, "days": 7},
    "plan2": {"name": "Standard Daily 60 (15 Days)", "limit": 60, "price": 250, "days": 15},
    "plan3": {"name": "Premium Daily Unlimited (30 Days)", "limit": 999999, "price": 700, "days": 30}
}

# 🌐 ULTRA ADVANCED LANGUAGE DICTIONARY (4 Languages)
LANG = {
    "bn": {
        "menu_dl": "⬇️ ভিডিও ডাউনলোড", "menu_sub": "💎 প্রিমিয়াম প্ল্যান", 
        "menu_prof": "👤 আমার প্রোফাইল", "menu_sup": "👨‍💻 হেল্পলাইন",
        "menu_ref": "👥 ইনভাইট ফ্রেন্ড", "menu_lang": "🌐 ভাষা / Language", "menu_pol": "📜 ব্যবহারের নিয়ম",
        "welcome": "স্বাগতম", "select_opt": "👇 নিচের মেনু থেকে আপনার কাঙ্ক্ষিত সেবাটি বেছে নিন:",
        "prof_head": "👤 **ব্যবহারকারী প্রোফাইল**", "name": "নাম", "id": "আইডি",
        "plan": "প্যাকেজ", "exp": "মেয়াদ", "usage": "ব্যবহার", "joined": "জয়েনিং ডেট",
        "ref_head": "👥 **রেফারাল ড্যাশবোর্ড**", "ref_inv": "মোট ইনভাইট", "ref_link": "🔗 আপনার ইনভাইট লিংক:",
        "ref_note": "এই লিংক শেয়ার করুন এবং বিশেষ রিওয়ার্ড জিতুন!",
        "sub_head": "💎 **প্রিমিয়াম জোন**", "sub_desc": " আনলিমিটেড ডাউনলোডের জন্য প্যাকেজ কিনুন:",
        "sub_p1": "🥉 বেসিক - ১০০৳ দৈনিক ৪০ (৭ দিন)", "sub_p2": "🥈 স্ট্যান্ডার্ড - ২৫০৳ দৈনিক  ৬০ (১৫ দিন)", "sub_p3": "🥇 প্রিমিয়াম - ৭০০৳ দৈনিক আনলিমিটেড (৩০ দিন)",
        "pay_ins": "🛒 **পেমেন্ট ইনভয়েস**\n💰 পরিমাণ: {price}৳\n💳 নগদ (পার্সোনাল): `{number}`\n\n⚠️ **নিয়ম:** এই নাম্বারে সেন্ড মানি করুন এবং নিচে TrxID দিন।",
        "pay_succ": "✅ তথ্য জমা হয়েছে! এডমিন শীঘ্রই অ্যাপ্রুভ করবেন।",
        "dl_head": "📥 **স্মার্ট ডাউনলোড প্যানেল**\nভিডিওর ধরণ বা প্লাটফর্ম নির্বাচন করুন:",
        "ask_fmt": "👋 **প্রিয় {name}**, আপনি এটি কোন ফরম্যাটে ডাউনলোড করতে চাচ্ছেন?",
        "vid_btn": "🎬 ভিডিও (HD)", "aud_btn": "🎵 অডিও (MP3)",
        "link_ask": "🔗 আপনার **{plat}** ভিডিও লিংকটি নিচে দিন:",
        "anim_1": "🔄 **Processing... 20%**\n□□□□□□□□□□",
        "anim_2": "🔄 **Processing... 45%**\n■■■■□□□□□□",
        "anim_3": "⬇️ **Downloading... 80%**\n■■■■■■■■□□",
        "anim_4": "🚀 **Uploading... 100%**\n■■■■■■■■■■",
        "complete": "✅ **ডাউনলোড সফল হয়েছে!**",
        "limit_over": "⚠️ **আজকের ফ্রি লিমিট শেষ!**\nআনলিমিটেড অ্যাক্সেস পেতে সাবস্ক্রিপশন নিন।",
        "policy_text": "👋 **স্বাগতম!**\nআমি **আয়মান হাসান শান** —\nআমি আপনাদের জন্য সম্পূর্ণ ফ্রি **TikTok Video Downloader Telegram Bot** তৈরি করেছি।\n\n🎯 **এই বটের মাধ্যমে আপনি যা করতে পারবেন:**\n✅ TikTok ভিডিও ওয়াটারমার্ক ছাড়া ডাউনলোড\n✅ HD কোয়ালিটিতে ভিডিও সেভ\n✅ কোনো লগইন বা পেমেন্ট ছাড়াই ১০০% ফ্রি\n✅ খুব সহজ ও দ্রুত ব্যবহারযোগ্য\n\n📌 **ব্যবহার করার নিয়ম:**\n1️⃣ TikTok ভিডিওর লিংক কপি করুন\n2️⃣ বটে পাঠান\n3️⃣ কয়েক সেকেন্ড অপেক্ষা করুন\n4️⃣ ভিডিও ডাউনলোড করুন 📥\n\n💡 **নোট:**\nএই বটটি শুধুমাত্র শিক্ষামূলক ও ব্যক্তিগত ব্যবহারের জন্য\nকোনো ভিডিওর কপিরাইট দায়ভার ব্যবহারকারীর নিজের\n\n❤️ যদি বটটি ভালো লাগে, বন্ধুদের সাথে শেয়ার করুন\n🐞 কোনো সমস্যা বা ফিডব্যাক থাকলে জানাতে ভুলবেন না\nধন্যবাদ সবাইকে 🙏\n\n— **Developer:** আয়মান হাসান শান",
        "sup_txt": "👨‍💻 **সাপোর্ট সেন্টার**\nযেকোনো টেকনিক্যাল সমস্যায় সরাসরি ডেভেলপারকে মেসেজ দিন।",
        "sup_btn": "📩 মেসেজ পাঠান"
    },
    "en": {
        "menu_dl": "⬇️ Download Video", "menu_sub": "💎 Premium Plan", 
        "menu_prof": "👤 My Profile", "menu_sup": "👨‍💻 Helpline",
        "menu_ref": "👥 Invite Friends", "menu_lang": "🌐 Language", "menu_pol": "📜 Policy",
        "welcome": "Welcome", "select_opt": "👇 Select your desired service below:",
        "prof_head": "👤 **USER PROFILE**", "name": "Name", "id": "ID",
        "plan": "Plan", "exp": "Expiry", "usage": "Usage", "joined": "Joined",
        "ref_head": "👥 **REFERRAL DASHBOARD**", "ref_inv": "Total Invites", "ref_link": "🔗 Your Invite Link:",
        "ref_note": "Share this link to earn special rewards!",
        "sub_head": "💎 **PREMIUM ZONE**", "sub_desc": "Unlock unlimited downloads:",
        "sub_p1": "🥉 Basic - 100৳ Daily 40 (7 Days)", "sub_p2": "🥈 Standard - 250৳ Daily 60 (15 Days)", "sub_p3": "🥇 Premium - 700৳ Daily Unlimited (30 Days)",
        "pay_ins": "🛒 **PAYMENT INVOICE**\n💰 Amount: {price}৳\n💳 Nagad (Personal): `{number}`\n\n⚠️ **Rule:** Send Money and reply with TrxID.",
        "pay_succ": "✅ Submitted! Admin will approve shortly.",
        "dl_head": "📥 **SMART DOWNLOAD PANEL**\nSelect platform type:",
        "ask_fmt": "👋 **Dear {name}**, which format do you want to download?",
        "vid_btn": "🎬 Video (HD)", "aud_btn": "🎵 Audio (MP3)",
        "link_ask": "🔗 Send your **{plat}** video link:",
        "anim_1": "🔄 **Processing... 20%**\n□□□□□□□□□□",
        "anim_2": "🔄 **Processing... 45%**\n■■■■□□□□□□",
        "anim_3": "⬇️ **Downloading... 80%**\n■■■■■■■■□□",
        "anim_4": "🚀 **Uploading... 100%**\n■■■■■■■■■■",
        "complete": "✅ **Download Successful!**",
        "limit_over": "⚠️ **Daily Limit Reached!**\nBuy subscription for unlimited access.",
        "policy_text": "👋 **Welcome!**\nI am **Ayman Hasan Shaan** —\nI created this **TikTok Video Downloader Telegram Bot** for you completely free.\n\n🎯 **Features:**\n✅ No Watermark\n✅ HD Quality\n✅ 100% Free\n✅ Fast & Easy\n\n📌 **How to Use:**\n1️⃣ Copy Link\n2️⃣ Send to Bot\n3️⃣ Wait a few seconds\n4️⃣ Get Video 📥\n\n💡 **Note:**\nFor educational/personal use only. Copyright belongs to owners.\n\n❤️ Share with friends!\n🐞 Report any bugs.\nThanks 🙏\n\n— **Developer:** Ayman Hasan Shaan",
        "sup_txt": "👨‍💻 **SUPPORT CENTER**\nContact developer directly for any technical issues.",
        "sup_btn": "📩 Send Message"
    },
    "ar": {
        "menu_dl": "⬇️ تحميل الفيديو", "menu_sub": "💎 خطة بريميوم", 
        "menu_prof": "👤 ملفي الشخصي", "menu_sup": "👨‍💻 المساعدة",
        "menu_ref": "👥 دعوة صديق", "menu_lang": "🌐 اللغة", "menu_pol": "📜 سياسة",
        "welcome": "أهلاً بك", "select_opt": "👇 اختر الخدمة المطلوبة:",
        "prof_head": "👤 **ملف المستخدم**", "name": "الاسم", "id": "المعرف",
        "plan": "الخطة", "exp": "الانتهاء", "usage": "الاستخدام", "joined": "انضم",
        "ref_head": "👥 **لوحة الإحالة**", "ref_inv": "الدعوات", "ref_link": "🔗 رابط الدعوة:",
        "ref_note": "شارك الرابط لتربح المكافآت!",
        "sub_head": "💎 **منطقة بريميوم**", "sub_desc": "اشترِ خطة لفتح الحدود:",
        "sub_p1": "🥉 أساسي - 100৳ 40 يوميًا (7 أيام)", "sub_p2": "🥈 قياسي - 250৳ 60 يوميًا  (15 يوم)", "sub_p3": "🥇 بريميوم - 700৳ يومي غير محدود (30 يوم)",
        "pay_ins": "🛒 **فاتورة الدفع**\n💰 المبلغ: {price}৳\n💳 Nagad: `{number}`\n\n⚠️ أرسل المال ثم رقم المعاملة.",
        "pay_succ": "✅ تم الإرسال! بانتظار الموافقة.",
        "dl_head": "📥 **لوحة التحميل الذكية**\nاختر المنصة:",
        "ask_fmt": "👋 **عزيزي {name}**، بأي تنسيق تريد التحميل؟",
        "vid_btn": "🎬 فيديو (HD)", "aud_btn": "🎵 صوت (MP3)",
        "link_ask": "🔗 أرسل رابط **{plat}**:",
        "anim_1": "🔄 **معالجة... 20%**\n□□□□□□□□□□",
        "anim_2": "🔄 **معالجة... 45%**\n■■■■□□□□□□",
        "anim_3": "⬇️ **تحميل... 80%**\n■■■■■■■■□□",
        "anim_4": "🚀 **رفع... 100%**\n■■■■■■■■■■",
        "complete": "✅ **تم التحميل بنجاح!**",
        "limit_over": "⚠️ **انتهى الحد اليومي!**\nاشترك للحصول على وصول غير محدود.",
        "policy_text": "👋 **مرحباً!**\nأنا **أيمن حسن شان** —\nلقد قمت بإنشاء هذا البوت لك مجاناً.\n\n🎯 **الميزات:**\n✅ بدون علامة مائية\n✅ جودة HD\n✅ مجاني 100%\n\n📌 **كيفية الاستخدام:**\n1️⃣ انسخ الرابط\n2️⃣ أرسله للبوت\n3️⃣ انتظر قليلاً\n4️⃣ حمل الفيديو 📥\n\n❤️ شارك مع الأصدقاء!\n\n— **المطور:** أيمن حسن شان",
        "sup_txt": "👨‍💻 **مركز الدعم**\nتواصل مع المطور مباشرة.",
        "sup_btn": "📩 إرسال رسالة"
    },
    "hi": {
        "menu_dl": "⬇️ वीडियो डाउनलोड", "menu_sub": "💎 प्रीमियम प्लान", 
        "menu_prof": "👤 मेरी प्रोफाइल", "menu_sup": "👨‍💻 हेल्पलाइन",
        "menu_ref": "👥 आमंत्रित करें", "menu_lang": "🌐 भाषा", "menu_pol": "📜 नीति",
        "welcome": "स्वागत है", "select_opt": "👇 नीचे से अपनी सेवा चुनें:",
        "prof_head": "👤 **उपयोगकर्ता प्रोफ़ाइल**", "name": "नाम", "id": "आईडी",
        "plan": "योजना", "exp": "समाप्ति", "usage": "उपयोग", "joined": "शामिल",
        "ref_head": "👥 **रेफरल डैशबोर्ड**", "ref_inv": "कुल आमंत्रण", "ref_link": "🔗 आपका लिंक:",
        "ref_note": "पुरस्कार पाने के लिए शेयर करें!",
        "sub_head": "💎 **प्रीमियम क्षेत्र**", "sub_desc": "सीमा हटाने के लिए प्लान खरीदें:",
        "sub_p1": "🥉 बेसिक - 100৳ दैनिक 40 (7 दिन)", "sub_p2": "🥈 स्टैंडर्ड - 250৳ प्रतिदिन 60 (15 दिन)", "sub_p3": "🥇 प्रीमियम - 700৳ दैनिक असीमित (30 दिन)",
        "pay_ins": "🛒 **भुगतान चालान**\n💰 राशि: {price}৳\n💳 नकद: `{number}`\n\n⚠️ पैसे भेजें और TrxID रिप्लाई करें।",
        "pay_succ": "✅ जमा हो गया! अनुमोदन की प्रतीक्षा करें।",
        "dl_head": "📥 **स्मार्ट डाउनलोड पैनल**\nप्लेटफ़ॉर्म चुनें:",
        "ask_fmt": "👋 **प्रिय {name}**, आप किस फॉर्मेट में डाउनलोड करना चाहते हैं?",
        "vid_btn": "🎬 वीडियो (HD)", "aud_btn": "🎵 ऑडियो (MP3)",
        "link_ask": "🔗 अपना **{plat}** लिंक भेजें:",
        "anim_1": "🔄 **प्रोसेसिंग... 20%**\n□□□□□□□□□□",
        "anim_2": "🔄 **प्रोसेसिंग... 45%**\n■■■■□□□□□□",
        "anim_3": "⬇️ **डाउनलोडिंग... 80%**\n■■■■■■■■□□",
        "anim_4": "🚀 **अपलोडिंग... 100%**\n■■■■■■■■■■",
        "complete": "✅ **डाउनलोड सफल!**",
        "limit_over": "⚠️ **दैनिक सीमा समाप्त!**\nअनलिमिटेड एक्सेस के लिए सब्सक्रिप्शन लें।",
        "policy_text": "👋 **स्वागत है!**\nमैं **अरायन हसन शान** हूँ —\nमैंने यह बॉट आपके लिए मुफ़्त बनाया है।\n\n🎯 **विशेषताएँ:**\n✅ बिना वॉटरमार्क डाउनलोड\n✅ HD क्वालिटी\n✅ 100% मुफ़्त\n\n📌 **कैसे उपयोग करें:**\n1️⃣ लिंक कॉपी करें\n2️⃣ बॉट को भेजें\n3️⃣ प्रतीक्षा करें\n4️⃣ वीडियो डाउनलोड करें 📥\n\n❤️ दोस्तों के साथ शेयर करें!\n\n— **डेवलपर:** अरायन हसन शान",
        "sup_txt": "👨‍💻 **सहायता केंद्र**\nमदद के लिए डेवलपर से संपर्क करें।",
        "sup_btn": "📩 संदेश भेजें"
    }
}

# ==========================================
# 💾 DATABASE ENGINE (Stable & Persistent)
# ==========================================
local_db_cache = {}

def load_db():
    global local_db_cache
    try:
        req = requests.get(BIN_URL, headers=HEADERS)
        if req.status_code == 200:
            data = req.json().get("record", {})
            local_db_cache = data.get("users", {})
            print("✅ Database Online & Loaded")
        else: local_db_cache = {}
    except: local_db_cache = {}

def save_db():
    def _save():
        try: requests.put(BIN_URL, headers=HEADERS, json={"users": local_db_cache})
        except: pass
    threading.Thread(target=_save).start()

load_db()

def get_user(user_id):
    sid = str(user_id)
    today = str(datetime.date.today())
    
    if sid not in local_db_cache:
        local_db_cache[sid] = {
            "plan": "free", "expiry": None, "downloads_today": 0,
            "last_date": today, "referrals": 0, "is_verified": False,
            "joined_date": today, "lang": "bn", "name": "Unknown"
        }
        save_db()
        return local_db_cache[sid]

    user = local_db_cache[sid]
    save_needed = False

    if user.get("last_date") != today:
        user["last_date"] = today; user["downloads_today"] = 0; save_needed = True

    if user["plan"] != "free" and user.get("expiry"):
        try:
            if datetime.date.today() > datetime.datetime.strptime(user["expiry"], "%Y-%m-%d").date():
                user["plan"] = "free"; user["expiry"] = None; save_needed = True
                try: bot.send_message(user_id, "⚠️ **Subscription Expired!** Switched to Free.")
                except: pass
        except: user["plan"] = "free"; save_needed = True

    if save_needed: save_db()
    return user

def update_user(uid, key, val):
    if str(uid) in local_db_cache:
        local_db_cache[str(uid)][key] = val
        save_db()

# ==========================================
# 🚀 CORE LOGIC (Aura Level: 100M+)
# ==========================================
@bot.message_handler(commands=['start'])
def start(message):
    uid = message.chat.id
    name = message.from_user.first_name
    update_user(uid, "name", name)
    user = get_user(uid)
    L = LANG[user.get('lang', 'bn')]
    
    # Referral System
    args = message.text.split()
    if len(args) > 1 and args[1] != str(uid):
        ref_id = args[1]
        if user['joined_date'] == str(datetime.date.today()) and user['downloads_today'] == 0:
             if str(ref_id) in local_db_cache:
                 local_db_cache[str(ref_id)]["referrals"] += 1
                 save_db()
                 try: bot.send_message(ref_id, f"🎉 **New Referral:** {name} joined via your link!")
                 except: pass

    if not check_force_sub(uid): return show_force_sub(uid)
    if user.get("is_verified"): show_menu(uid)
    else: show_policy_agreement(uid, name, L)

def check_force_sub(uid):
    try: return bot.get_chat_member(CHANNEL_ID, uid).status in ['creator', 'administrator', 'member']
    except: return True

def show_force_sub(uid):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📢 Join Official Channel", url=CHANNEL_LINK))
    markup.add(types.InlineKeyboardButton("✅ Joined", callback_data="check_sub"))
    bot.send_message(uid, "⚠️ **Access Denied!**\nPlease join our channel to use this premium bot.", reply_markup=markup)

def show_policy_agreement(uid, name, L):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✅ I Agree / আমি সম্মত", callback_data="agree"))
    bot.send_message(uid, L['policy_text'], reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda c: c.data == "agree")
def agree_cb(c):
    update_user(c.message.chat.id, "is_verified", True)
    bot.delete_message(c.message.chat.id, c.message.message_id)
    show_menu(c.message.chat.id)

@bot.callback_query_handler(func=lambda c: c.data == "check_sub")
def sub_check_cb(c):
    if check_force_sub(c.message.chat.id):
        bot.delete_message(c.message.chat.id, c.message.message_id)
        if get_user(c.message.chat.id)["is_verified"]: show_menu(c.message.chat.id)
        else: 
            u = get_user(c.message.chat.id)
            show_policy_agreement(c.message.chat.id, c.from_user.first_name, LANG[u.get('lang','bn')])
    else: bot.answer_callback_query(c.id, "❌ You haven't joined yet!")

def show_menu(uid):
    user = get_user(uid)
    L = LANG[user.get('lang', 'bn')]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(L['menu_dl'], L['menu_sub'])
    markup.add(L['menu_prof'], L['menu_ref'])
    markup.add(L['menu_sup'], L['menu_lang'])
    markup.add(L['menu_pol'])
    
    info = (
        f"👋 **{L['welcome']} {local_db_cache[str(uid)]['name']}**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"💎 Plan: **{PLANS[user['plan']]['name']}**\n"
        f"📊 Daily Limit: **{user['downloads_today']}/{PLANS[user['plan']]['limit']}**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"{L['select_opt']}"
    )
    bot.send_message(uid, info, reply_markup=markup, parse_mode="Markdown")

# ==========================================
# 🌟 DYNAMIC FEATURES
# ==========================================

# 1. 📜 POLICY
@bot.message_handler(func=lambda m: m.text in ["📜 নীতিমালা", "📜 Policy", "📜 سياسة", "📜 नीति", "📜 ব্যবহারের নিয়ম"])
def show_policy_text(m):
    L = LANG[get_user(m.chat.id).get('lang', 'bn')]
    bot.send_message(m.chat.id, L['policy_text'], parse_mode="Markdown")

# 2. 🌐 LANGUAGE (FIXED)
@bot.message_handler(func=lambda m: m.text in ["🌐 ভাষা / Language", "🌐 Language", "🌐 اللغة", "🌐 भाषा", "🌐 ভাষা/Lang"])
def change_lang(m):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🇧🇩 বাংলা", callback_data="lang_bn"),
        types.InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"),
        types.InlineKeyboardButton("🇸🇦 Arabic", callback_data="lang_ar"),
        types.InlineKeyboardButton("🇮🇳 Hindi", callback_data="lang_hi")
    )
    bot.send_message(m.chat.id, "🌐 **Select System Language:**", reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data.startswith("lang_"))
def set_lang_cb(c):
    lang = c.data.split("_")[1]
    update_user(c.message.chat.id, "lang", lang)
    bot.delete_message(c.message.chat.id, c.message.message_id)
    show_menu(c.message.chat.id)

# 3. 👥 REFERRAL
@bot.message_handler(func=lambda m: m.text in ["👥 রেফারাল", "👥 Referral", "👥 إحالة", "👥 रेफरल", "👥 ইনভাইট ফ্রেন্ড", "👥 Invite Friends", "👥 دعوة صديق", "👥 आमंत्रित करें"])
def referral_system(m):
    uid = m.chat.id
    user = get_user(uid)
    L = LANG[user.get('lang', 'bn')]
    link = f"https://t.me/{bot.get_me().username}?start={uid}"
    
    text = (
        f"{L['ref_head']}\n"
        "━━━━━━━━━━━━━━━━\n"
        f"👤 {L['name']}: **{local_db_cache[str(uid)]['name']}**\n"
        f"🎁 {L['ref_inv']}: **{user['referrals']}**\n\n"
        f"{L['ref_link']}\n`{link}`\n\n"
        f"💡 {L['ref_note']}"
    )
    bot.send_message(uid, text, parse_mode="Markdown")

# 4. 👤 PROFILE
@bot.message_handler(func=lambda m: m.text in ["👤 প্রোফাইল", "👤 Profile", "👤 الملف الشخصي", "👤 प्रोफ़ाइल", "👤 আমার প্রোফাইল", "👤 My Profile", "👤 ملفي الشخصي", "👤 मेरी प्रोफाइल"])
def show_profile(m):
    uid = m.chat.id
    user = get_user(uid)
    L = LANG[user.get('lang', 'bn')]
    limit = PLANS[user['plan']]['limit']
    exp = user['expiry'] if user['expiry'] else "Lifetime"
    
    text = (
        f"{L['prof_head']}\n"
        "━━━━━━━━━━━━━━━━\n"
        f"🆔 {L['id']}: `{uid}`\n"
        f"📛 {L['name']}: **{local_db_cache[str(uid)]['name']}**\n"
        f"📅 {L['joined']}: {user['joined_date']}\n"
        "━━━━━━━━━━━━━━━━\n"
        f"📦 {L['plan']}: **{PLANS[user['plan']]['name']}**\n"
        f"⏳ {L['exp']}: {exp}\n"
        f"📊 {L['usage']}: {user['downloads_today']}/{limit}"
    )
    bot.send_message(uid, text, parse_mode="Markdown")

# 5. 👨‍💻 SUPPORT
@bot.message_handler(func=lambda m: m.text in ["👨‍💻 সাপোর্ট", "👨‍💻 Support", "👨‍💻 الدعم", "👨‍💻 सहायता", "👨‍💻 হেল্পলাইন", "👨‍💻 Helpline", "👨‍💻 المساعدة", "👨‍💻 हेल्पलाइन"])
def support_handler(m):
    L = LANG[get_user(m.chat.id).get('lang', 'bn')]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📩 Admin", url=f"tg://user?id={ADMIN_ID}"))
    bot.send_message(m.chat.id, L['sup_txt'], reply_markup=markup, parse_mode="Markdown")

# 6. 💎 SUBSCRIPTION
@bot.message_handler(func=lambda m: m.text in ["💎 সাবস্ক্রিপশন", "💎 Subscription", "💎 اشتراك", "💎 सदस्यता", "💎 প্রিমিয়াম প্ল্যান", "💎 Premium Plan", "💎 خطة بريميوم", "💎 प्रीमियम प्लान"])
def sub_menu(m):
    L = LANG[get_user(m.chat.id).get('lang', 'bn')]
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(L['sub_p1'], callback_data="buy_plan1"),
        types.InlineKeyboardButton(L['sub_p2'], callback_data="buy_plan2"),
        types.InlineKeyboardButton(L['sub_p3'], callback_data="buy_plan3")
    )
    bot.send_message(m.chat.id, f"{L['sub_head']}\n{L['sub_desc']}", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda c: c.data.startswith("buy_"))
def buy_cb(c):
    p = c.data.split("_")[1]
    uid = c.message.chat.id
    L = LANG[get_user(uid).get('lang', 'bn')]
    
    text = L['pay_ins'].format(price=PLANS[p]['price'], number=NAGAD_NUMBER)
    msg = bot.send_message(uid, text, parse_mode="Markdown")
    bot.register_next_step_handler(msg, verify_payment, p)

def verify_payment(m, plan):
    trx = m.text
    L = LANG[get_user(m.chat.id).get('lang', 'bn')]
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("✅ Approve", callback_data=f"ok_{m.chat.id}_{plan}"),
        types.InlineKeyboardButton("❌ Reject", callback_data=f"no_{m.chat.id}")
    )
    
    bot.send_message(ADMIN_ID, f"🔔 **PAYMENT RECEIVED!**\nUser: `{m.chat.id}`\nName: {m.from_user.first_name}\nPlan: {PLANS[plan]['name']}\nTrxID: `{trx}`", reply_markup=markup, parse_mode="Markdown")
    bot.send_message(m.chat.id, L['pay_succ'])

@bot.callback_query_handler(func=lambda c: c.data.startswith(("ok_", "no_")))
def admin_action(c):
    if c.message.chat.id != ADMIN_ID: return
    action, uid, *rest = c.data.split("_")
    
    if action == "no":
        bot.edit_message_text("❌ Rejected", ADMIN_ID, c.message.message_id)
        try: bot.send_message(uid, "❌ **Payment Rejected.** Contact Support.")
        except: pass
    else:
        plan = rest[0]
        days = PLANS[plan]['days']
        exp = str(datetime.date.today() + datetime.timedelta(days=days))
        
        if str(uid) in local_db_cache:
            local_db_cache[str(uid)]["plan"] = plan
            local_db_cache[str(uid)]["expiry"] = exp
            save_db()
            
        bot.edit_message_text(f"✅ Approved for {uid}", ADMIN_ID, c.message.message_id)
        try: bot.send_message(uid, f"🎉 **Premium Activated!**\nPlan: {PLANS[plan]['name']}\nExpiry: {exp}")
        except: pass

# 7. ⬇️ DOWNLOAD LOGIC (YouTube Blocked)
@bot.message_handler(func=lambda m: m.text in ["⬇️ ডাউনলোড", "⬇️ Download", "⬇️ تحميل", "⬇️ डाउनलोड", "⬇️ ভিডিও ডাউনলোড", "⬇️ Download Video", "⬇️ تحميل الفيديو", "⬇️ वीडियो डाउनलोड"])
def dl_menu(m):
    L = LANG[get_user(m.chat.id).get('lang', 'bn')]
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🎵 TikTok", callback_data="plt_tiktok"),
        types.InlineKeyboardButton("📘 Facebook", callback_data="plt_facebook"),
        types.InlineKeyboardButton("📸 Instagram", callback_data="plt_instagram"),
        types.InlineKeyboardButton("📺 YouTube", callback_data="plt_youtube")
    )
    bot.send_message(m.chat.id, L['dl_head'], reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda c: c.data.startswith("plt_"))
def plt_cb(c):
    plat = c.data.split("_")[1].capitalize()
    uid = c.message.chat.id
    name = local_db_cache[str(uid)]['name']

    # ⚠️ BLOCK YOUTUBE
    if plat == "Youtube":
        msg = (
            f"প্রিয় {name},\n"
            "আমরা আন্তরিকভাবে দুঃখিত যে এই মুহূর্তে YouTube কন্টেন্ট ডাউনলোড সার্ভিসটি আপনাকে প্রদান করতে পারছি না।\n"
            "কারিগরি (Technical) সমস্যার কারণে সাময়িকভাবে সার্ভিসটি বন্ধ রাখা হয়েছে।\n"
            "সমস্যার সমাধান শেষ হয়ে সার্ভিসটি পুনরায় চালু হওয়া মাত্রই আপনাকে দ্রুত আপডেট জানানো হবে।\n"
            "আপনার ধৈর্য ও সহযোগিতার জন্য আমরা কৃতজ্ঞ।\n\n"
            "ধন্যবাদান্তে,\n"
            "Team Swygen ❤️"
        )
        bot.send_message(uid, msg)
        return

    L = LANG[get_user(c.message.chat.id).get('lang', 'bn')]
    msg = bot.send_message(c.message.chat.id, L['link_ask'].format(plat=plat), parse_mode="Markdown")
    bot.register_next_step_handler(msg, process_link)

@bot.message_handler(func=lambda m: any(x in m.text.lower() for x in ["tiktok", "facebook", "instagram", "youtube", "reel", "youtu"]))
def auto_link(m): process_link(m)

temp_links = {}

def process_link(m):
    uid = m.chat.id
    user = get_user(uid)
    L = LANG[user.get('lang', 'bn')]
    name = m.from_user.first_name
    
    # ⚠️ BLOCK YOUTUBE DIRECT LINKS
    if "youtube.com" in m.text.lower() or "youtu.be" in m.text.lower():
        msg = (
            f"প্রিয় {name},\n"
            "আমরা আন্তরিকভাবে দুঃখিত যে এই মুহূর্তে YouTube কন্টেন্ট ডাউনলোড সার্ভিসটি আপনাকে প্রদান করতে পারছি না।\n"
            "কারিগরি (Technical) সমস্যার কারণে সাময়িকভাবে সার্ভিসটি বন্ধ রাখা হয়েছে।\n"
            "সমস্যার সমাধান শেষ হয়ে সার্ভিসটি পুনরায় চালু হওয়া মাত্রই আপনাকে দ্রুত আপডেট জানানো হবে।\n"
            "আপনার ধৈর্য ও সহযোগিতার জন্য আমরা কৃতজ্ঞ।\n\n"
            "ধন্যবাদান্তে,\n"
            "Team Swygen ❤️"
        )
        bot.send_message(uid, msg)
        return

    if user['downloads_today'] >= PLANS[user['plan']]['limit']:
        bot.send_message(uid, L['limit_over'])
        return
        
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(L['vid_btn'], callback_data=f"d_vid_{m.message_id}"),
        types.InlineKeyboardButton(L['aud_btn'], callback_data=f"d_aud_{m.message_id}")
    )
    temp_links[str(uid)] = m.text
    bot.send_message(uid, L['ask_fmt'].format(name=name), reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda c: c.data.startswith("d_"))
def final_dl(c):
    uid = c.message.chat.id
    url = temp_links.get(str(uid))
    if not url: return bot.send_message(uid, "⚠️ Session Expired.")
    
    user = get_user(uid)
    L = LANG[user.get('lang', 'bn')]
    mode = c.data.split("_")[1]
    
    # 🔥 REAL-TIME ANIMATION (Progress Bar)
    msg = bot.edit_message_text(L['anim_1'], uid, c.message.message_id, parse_mode="Markdown")
    time.sleep(0.5)
    
    bot.edit_message_text(L['anim_2'], uid, msg.message_id, parse_mode="Markdown")
    time.sleep(0.8)
    
    bot.edit_message_text(L['anim_3'], uid, msg.message_id, parse_mode="Markdown")
    time.sleep(0.5)
    
    fn = f"swygen_{uid}_{int(time.time())}"
    try:
        # Configuration for other platforms
        opts = {
            'quiet': True, 
            'outtmpl': fn+'.mp4', 
            'format': 'bestvideo+bestaudio/best',
            'noplaylist': True
        }
        if mode == 'aud': opts['outtmpl'] = fn+'.mp3'; opts['format'] = 'bestaudio/best'
        
        with yt_dlp.YoutubeDL(opts) as ydl: ydl.download([url])
        
        bot.edit_message_text(L['anim_4'], uid, msg.message_id, parse_mode="Markdown")
        bot.send_chat_action(uid, 'upload_document')
        
        ext = '.mp3' if mode == 'aud' else '.mp4'
        with open(fn+ext, 'rb') as f:
            cap = f"{L['complete']}\n━━━━━━━━━━━━\n👤 **User:** {local_db_cache[str(uid)]['name']}\n🤖 **Bot:** @{bot.get_me().username}\n👨‍💻 **Dev:** {DEV_NAME}"
            if mode == 'aud': bot.send_audio(uid, f, caption=cap, parse_mode="Markdown")
            else: bot.send_video(uid, f, caption=cap, parse_mode="Markdown")
            
        local_db_cache[str(uid)]['downloads_today'] += 1
        save_db()
        
        # Feedback
        fb = types.InlineKeyboardMarkup()
        fb.add(types.InlineKeyboardButton("🌟 Review / ফিডব্যাক", url="https://swygen.xyz"))
        bot.send_message(uid, "❤️ Thanks for using Swygen IT!", reply_markup=fb)
        
        bot.delete_message(uid, msg.message_id)
        if os.path.exists(fn+ext): os.remove(fn+ext)
        
    except Exception as e:
        bot.edit_message_text(f"❌ Error: {str(e)}", uid, msg.message_id)

# ADMIN COMMANDS
@bot.message_handler(commands=['admin'])
def adm(m):
    if m.chat.id == ADMIN_ID:
        u = len(local_db_cache)
        p = sum(1 for x in local_db_cache.values() if x['plan'] != 'free')
        bot.reply_to(m, f"📊 **Stats:**\nUsers: {u}\nPremium: {p}")

@bot.message_handler(commands=['broadcast'])
def bdc(m):
    if m.chat.id == ADMIN_ID:
        msg = m.text.replace('/broadcast', '')
        for u in local_db_cache:
            try: bot.send_message(u, msg)
            except: pass

# ==========================================
# 🔄 24/7 RUNNER (Robust Polling)
# ==========================================
keep_alive()

print("🤖 Bot is Running 24/7...")
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as e:
        print(f"❌ Network Error: {e}")
        time.sleep(5) # Wait 5 sec before reconnecting
