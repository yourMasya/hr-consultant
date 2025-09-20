from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


async def cancel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Cancel the conversation.
    """
    await update.message.reply_text("❌ CV analysis cancelled.")
    return ConversationHandler.END
