from docx import Document as DocxDocument
import pdfplumber

from typing import Dict, Any
import logging


logger = logging.getLogger(__name__)


class DocParser:    
    async def _parse_pdf(self, file_path: str) -> None | str:
        """
        Parse PDF file
        """
        try:
            with pdfplumber.open(file_path) as pdf:
                return " ".join([page.extract_text() for page in pdf.pages])
            
        except Exception as e:
            logger.error(f"PDF parsing error: {e}")
            return None
    
    async def _parse_docx(self, file_path: str) -> None | str:
        """
        Parse DOCX file
        """
        try:
            doc = DocxDocument(file_path)
            return "\n".join([para.text.strip() for para in doc.paragraphs])
            
        except Exception as e:
            logger.error(f"DOCX parsing error: {e}")
            return None

    async def parse_doc(self, file_path: str) -> Dict[str, Any]:
        """
        Extract text and formatting information from CV file.
        """
        try:
            if file_path.endswith('.pdf'):
                return await self._parse_pdf(file_path)
            elif file_path.endswith(('.docx', '.doc')):
                return await self._parse_docx(file_path)

        except Exception as e:
            logger.error(f"Error parsing file {file_path}: {e}")
            return None
