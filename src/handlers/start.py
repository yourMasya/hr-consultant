from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Send a welcome message when the command /start is ran
    """
    welcome_text = """
👋 *Welcome to CV Advisor Bot!* 

I can analyze your CV and provide detailed feedback on:
• Formatting and structure 📄
• Content effectiveness 💼  
• ATS optimization tips 🤖
• Overall impact assessment ⚡

*How to get started:*
1. Click 'See My CV' below
2. Upload your PDF or DOCX file
3. Receive instant AI-powered feedback!
"""

    keyboard = [
        [KeyboardButton("📄 See my CV"), KeyboardButton("🙏 Help")]
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, 
        resize_keyboard=True,
        one_time_keyboard=True
    )
    
    await update.message.reply_markdown(
        welcome_text, 
        reply_markup=reply_markup
    )