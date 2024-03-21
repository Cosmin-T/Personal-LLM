# main.py

from logic.model import *
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes



async def  start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi, how can I help you?')

def handle_repsonse(text):
    return query(text)

async def handle_message(update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User: {update.message.chat.id} in {message_type}: {text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_repsonse(new_text)
        else:
            print('Bot was not mentioned in the group. No response sent.')
            return
    else:
        response = handle_repsonse(text)

    print(f'Bot: {response}')
    await update.message.reply_text(response)



async def error(update:Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting Bot')
    app = Application.builder().token(ACCESS_TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling')
    app.run_polling(poll_interval=3)