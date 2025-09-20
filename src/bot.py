import logging
from telegram.ext import Application, ContextTypes, MessageHandler, filters, CommandHandler
from handlers.start import start_handler
from handlers.process_cv import cv_processing_handler
from handlers.help import help_handler
from handlers.cancel import cancel_handler
from settings.config import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """
    Run the HR Telegram bot
    """
    app = Application.builder().token(config.TG_BOT_TOKEN) \
    .context_types(ContextTypes()).build()
    
    app.bot_data['config'] = config

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(MessageHandler(filters.Text(["See my CV"]), cv_processing_handler))
    app.add_handler(MessageHandler(filters.Text(["🙏 Help"]), help_handler))
    app.add_handler(MessageHandler(filters.Text(["Back to Menu"]), start_handler))

    app.add_handler(CommandHandler("cancel", cancel_handler))
    app.add_handler(MessageHandler(filters.Document.ALL, cv_processing_handler))

    logger.info("Bot is starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
    