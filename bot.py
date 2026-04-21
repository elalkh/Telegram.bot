from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# الأزرار
keyboard = [
    ["📦 طلب خدمة"],
    ["💰 الأسعار", "📞 تواصل معنا"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# لما المستخدم يكتب /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا فيك 👋 اختر من القائمة:", reply_markup=reply_markup)

# التعامل مع الأزرار
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📦 طلب خدمة":
        await update.message.reply_text("شو الخدمة اللي بدك ياها؟")

    elif text == "💰 الأسعار":
        await update.message.reply_text("الأسعار رح نحطها هون 💵")

    elif text == "📞 تواصل معنا":
        await update.message.reply_text("راسلنا هون: @your_username")

    else:
        await update.message.reply_text("اختار من الأزرار لو سمحت 👇")

# تشغيل البوت
app = ApplicationBuilder().token("8752910871:AAEBa3xQDJW7F-fKJKIX0DzF_uqsSdNaYW8").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()