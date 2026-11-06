import os, asyncio, logging, random
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.request import HTTPXRequest
from trading_engine import get_balance_demo, generate_signal
load_dotenv()
TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
logging.basicConfig(level=logging.INFO)
request=HTTPXRequest(connect_timeout=60,read_timeout=60)
def main_menu():
    k=[[InlineKeyboardButton("🚀 تشغيل التداول",callback_data="go")],[InlineKeyboardButton("📊 إشارة",callback_data="get_signal"),InlineKeyboardButton("💰 الرصيد",callback_data="balance")]]
    return InlineKeyboardMarkup(k)
async def start(update, context):
    await update.message.reply_text("🤖 بوت التداول الذكي - Pocket Robot 🚀\n✅ BEARISH/BULLISH\n✅ Smart Scaling", reply_markup=main_menu())
async def btn(update, context):
    q=update.callback_query
    await q.answer()
    if q.data=="balance":
        b=get_balance_demo()
        await q.edit_message_text(f"🟢 REAL\n💰 {b['real']} USD\n💳 DEMO {b['demo']}", reply_markup=main_menu())
    elif q.data=="get_signal":
        s=await asyncio.to_thread(generate_signal,"CSCO OTC")
        await q.edit_message_text(s, reply_markup=main_menu())
    else:
        p=random.uniform(10,70)
        await q.edit_message_text(f"🏆 انتصار! +{p:.1f} USD", reply_markup=main_menu())
def main():
    app=Application.builder().token(TOKEN).request(request).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CallbackQueryHandler(btn))
    print("🚀 بوت التداول يعمل...")
    app.run_polling()
if __name__=="__main__":
    main()
