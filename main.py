from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_TOKEN = '7718597010:AAHuSYci8ZYB95YZVSzjY_hmwi9ESUxjbsY'

async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [ InlineKeyboardButton("Новости", url="https://ria.ru/")],
        [InlineKeyboardButton("Музыка", url="https://music.yandex.ru/")],
        [InlineKeyboardButton("Видео", url="https://ru.freepik.com/videos")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите пожалуйста ссылку:", reply_markup=reply_markup)

if __name__ == '__main__':
    app = ApplicationBuilder().token(API_TOKEN).build()

    app.add_handler(CommandHandler("links", links))

    print("Бот запущен...")
    app.run_polling()

