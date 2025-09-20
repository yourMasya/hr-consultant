from telegram import Update
from telegram.ext import ContextTypes
import logging
import os
from pathlib import Path

from .process_doc import DocParser
# from ..ai_service import AIService

logger = logging.getLogger(__name__)

async def cv_processing_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle CV document uploads and process them
    """
    config = context.bot_data.get('config')
    logger.info(f'config content: {config}')

    user = update.effective_user
    document = update.message.document
    
    if not document.file_name.endswith(('.pdf', '.docx', '.doc')):
        await update.message.reply_text(
            "❌ Please upload a PDF or Word document (.pdf, .docx, .doc)"
        )
        return
    
    if document.file_size > config.MAX_FILE_SIZE_MB * 1024**2:
        await update.message.reply_text(
            f"❌ File too large. Please upload a file under {config.MAX_FILE_SIZE_MB}MB."
            )
        return
    
    await update.message.reply_text("📥 Downloading your CV...")
    
    try:
        # Create temp directory if it doesn't exist
        temp_dir = Path("temp")
        temp_dir.mkdir(exist_ok=True)
        
        file = await document.get_file()
        file_path = temp_dir / f"{document.file_id}_{document.file_name}"
        await file.download_to_drive(file_path)
        
        await update.message.reply_text("🔍 Extracting content and analyzing structure...")
        
        cv_data = await DocParser().parse_doc(str(file_path))
        logger.info(f'cv content: {cv_data}')
        
        if not cv_data:
            await update.message.reply_text("❌ Could not extract content from your CV. Please try a different file.")
            if file_path.exists():
                os.remove(file_path)
            return
        
        await update.message.reply_text("🤖 Analyzing with AI... This may take a moment...")
        
        # ai_service = AIService()
        # analysis = await ai_service.analyze_cv(cv_data)
        
        # response = f"📊 *CV Analysis Complete!*\n\n{analysis}"
        # await update.message.reply_markdown_v2(response)
        
        response = "📊 *CV Analysis Complete!*\n\nThis feature is currently under development."
        await update.message.reply_markdown(response)
        
        if file_path.exists():
            os.remove(file_path)
        
    except Exception as e:
        logger.error(f"Error processing CV: {e}", exc_info=True)
        await update.message.reply_text(
            "❌ Sorry, I encountered an error processing your CV. Please try again with a different file."
        )
        # Clean up file if it was partially downloaded
        try:
            if 'file_path' in locals() and file_path.exists():
                os.remove(file_path)
        except:
            pass
