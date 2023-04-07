import requests
import re
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Halo! Saya adalah bot telegram untuk melakukan bypass URL. Ketik /bypass [URL] untuk membypass URL.")

def bypass(update, context):
    url = context.args[0]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"URL sudah tidak terbypass: {url}")
        elif r.status_code == 302:
            new_url = r.headers["Location"]
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"URL berhasil dibypass: {new_url}")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Gagal melakukan bypass URL.")
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Terjadi kesalahan: {e}")

def main():
    updater = Updater(token='TOKEN_BOT_ANDA', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    bypass_handler = CommandHandler('bypass', bypass)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(bypass_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
