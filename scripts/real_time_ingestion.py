from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

def handle_message(update: Update, context: CallbackContext):
    message = update.message
    # Process text, images, etc.
    print(f"Received message: {message.text}")

def main():
    # Set up the Updater with your bot token
    updater = Updater("YOUR_API_TOKEN", use_context=True)
    dp = updater.dispatcher
    
    # Handler for text messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()