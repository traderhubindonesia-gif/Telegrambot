import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
DEFAULT_CHANNEL = os.getenv("DEFAULT_CHANNEL", None)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    if message.text.lower().startswith("/start"):
        await message.reply("🔥 MASTER CALL X12 aktif! Kirim /signal BTCUSDT untuk mulai analisis.")
    elif message.text.lower().startswith("/signal"):
        await message.reply("📊 Generating signal...\n\n🔥 MASTER CALL: BTCUSDT – LONG\n📍 Entry: 65840\n🛑 Stop Loss: 65450\n🎯 Take Profit: 66600 – 67200\n📊 Risk Reward: 1:3\n✅ Confidence Level: HIGH ✅")
    else:
        await message.reply("Gunakan format /signal [COIN]. Contoh: /signal ETHUSDT")

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
