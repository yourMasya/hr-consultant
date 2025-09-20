from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the 'Help' button press and show help information
    """
    help_text = (
        "🤖 **HR Bot Help**\n\n"
        "**Authors:** @your_masya & @sashullel\n"
        "**Contact:** our_emails@example.com\n"
        "**Support:** support@example.com\n\n"
        "This bot helps with CV submission and processing."
    )
    
    keyboard = [[KeyboardButton("Back to Menu")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(help_text, reply_markup=reply_markup, parse_mode='Markdown')