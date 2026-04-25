from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

ADMIN_ID =1033158867
QR_IMAGE = "shamcash_qr.jpg"   # اسم صورة QR بنفس المجلد

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

# قائمة الشراء
buy_keyboard = [
    ["🛒 شراء"],
    ["🔙 رجوع"]
]
buy_markup = ReplyKeyboardMarkup(buy_keyboard, resize_keyboard=True)

# تخزين آخر طلب لكل مستخدم
user_orders = {}

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا فيك 👋 اختر:", reply_markup=main_markup)

# التعامل مع الرسائل النصية
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    if text == "📦 الاشتراكات":
        await update.message.reply_text("اختر الاشتراك:", reply_markup=subs_markup)

    elif text == "📞 تواصل معنا":
        await update.message.reply_text("تواصل معنا هنا 👇\nhttps://t.me/GeorgeBazah")

    elif text == "⏱ ساعة":
        user_orders[user_id] = "اشتراك ساعة - 1$"
        await update.message.reply_text("اشتراك ساعة\nالسعر: 1$", reply_markup=buy_markup)

    elif text == "⏱ ساعتين":
        user_orders[user_id] = "اشتراك ساعتين - 2$"
        await update.message.reply_text("اشتراك ساعتين\nالسعر: 2$", reply_markup=buy_markup)

    elif text == "📅 أسبوع":
        user_orders[user_id] = "اشتراك أسبوع - 5$"
        await update.message.reply_text("اشتراك أسبوع\nالسعر: 5$", reply_markup=buy_markup)

    elif text == "📅 شهر":
        user_orders[user_id] = "اشتراك شهر - 15$"
        await update.message.reply_text("اشتراك شهر\nالسعر: 15$", reply_markup=buy_markup)

    elif text == "🛒 شراء":
        order = user_orders.get(user_id, "غير محدد")
        with open(QR_IMAGE, "rb") as qr:
            await update.message.reply_photo(
                photo=qr,
                caption=f"طلبك: {order}\n\nحوّل المبلغ عبر شام كاش باستخدام الباركود 👆\nوبعد الدفع ابعت صورة إشعار التحويل."
            )

    elif text == "🔙 رجوع":
        await update.message.reply_text("رجعنا للقائمة الرئيسية", reply_markup=main_markup)

    else:
        await update.message.reply_text("اختار من الأزرار 👇")

# استقبال صورة الدفع
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    order = user_orders.get(user.id, "غير محدد")

    photo = update.message.photo[-1].file_id
    caption = (
        f"طلب جديد 💰\n"
        f"الاسم: {user.full_name}\n"
        f"اليوزر: @{user.username if user.username else 'مافي'}\n"
        f"ID: {user.id}\n"
        f"الطلب: {order}"
    )

    await context.bot.send_photo(chat_id=ADMIN_ID, photo=photo, caption=caption)
    await update.message.reply_text("تم استلام إشعار الدفع ✅\nسيتم التحقق وتفعيل اشتراكك قريبًا.")

# تشغيل
app = ApplicationBuilder().token("8752910871:AAEBa3xQDJW7F-fKJKIX0DzF_uqsSdNaYW8").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()