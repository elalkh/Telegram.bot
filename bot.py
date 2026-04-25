from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# القائمة الرئيسية
main_keyboard = [
    ["📦 الاشتراكات"],
    ["📞 تواصل معنا"]
]

main_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)

# قائمة الاشتراكات
subs_keyboard = [
    ["⏱ ساعة", "⏱ ساعتين"],
    ["📅 أسبوع", "📅 شهر"],
    ["🔙 رجوع"]
]

subs_markup = ReplyKeyboardMarkup(subs_keyboard, resize_keyboard=True)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا فيك 👋 اختر:", reply_markup=main_markup)

# التعامل مع الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # القائمة الرئيسية
    if text == "📦 الاشتراكات":
        await update.message.reply_text("اختر الاشتراك:", reply_markup=subs_markup)

    elif text == "📞 تواصل معنا":
        await update.message.reply_text("تواصل معنا هنا 👇\nhttps://t.me/GeorgeBazah")

    # الاشتراكات
    elif text == "⏱ ساعة":
        await update.message.reply_text("اشتراك ساعة\nالسعر: 1$\n\nإذا بدك تكمل اكتب: شراء ساعة")

    elif text == "⏱ ساعتين":
        await update.message.reply_text("اشتراك ساعتين\nالسعر: 2$\n\nإذا بدك تكمل اكتب: شراء ساعتين")

    elif text == "📅 أسبوع":
        await update.message.reply_text("اشتراك أسبوع\nالسعر: 5$\n\nإذا بدك تكمل اكتب: شراء أسبوع")

    elif text == "📅 شهر":
        await update.message.reply_text("اشتراك شهر\nالسعر: 15$\n\nإذا بدك تكمل اكتب: شراء شهر")

    elif text == "🔙 رجوع":
        await update.message.reply_text("رجعنا للقائمة الرئيسية", reply_markup=main_markup)

    else:
        await update.message.reply_text("اختار من الأزرار 👇")

# تشغيل
app = ApplicationBuilder().token("8752910871:AAEBa3xQDJW7F-fKJKIX0DzF_uqsSdNaYW8").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()