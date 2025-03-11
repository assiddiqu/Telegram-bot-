import os
import openai
from telegram import Update
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load API keys from environment variables
OPENAI_API_KEY = "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"
TELEGRAM_BOT_TOKEN = "7850771542:AAH4zkNOaUPUshvWi0huSviwOjleMekXsg4"

openai.api_key = OPENAI_API_KEY

# Function to interact with ChatGPT
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Handle messages
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    chat_response = chat_with_gpt(user_message)
    update.message.reply_text(chat_response)

# Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm an AI bot. Ask me anything.")

# Main function
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
