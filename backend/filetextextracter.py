from abc import ABC, abstractmethod
from typing import IO
from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text as fallback_text_extraction
import docx

class TextExtractor(ABC):  # Interface Segregation Principle (ISP)
    @abstractmethod
    def get_text(self, file: IO) -> str:
        pass


class PDFTextExtractor(TextExtractor):  # Single Responsibility Principle (SRP)
    def get_text(self, file: IO) -> str:
        text = ""
        try:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        except Exception as e:
            print(str(e))
            text = fallback_text_extraction(file)
            return None
        return text 


class DOCXTextExtractor(TextExtractor):  # SRP
    def get_text(self, file: IO) -> str:
        final_text = []
        doc = docx.Document(file)
        for line in doc.paragraphs:
            final_text.append(line.text)
        return "\n".join(final_text)


class PlainTextExtractor(TextExtractor):  # SRP
    def get_text(self, file: IO) -> str:
        return file.read()


class TextExtractorFactory:  # SRP, Dependency Inversion Principle (DIP)
    def create_extractor(self, file_extension: str) -> TextExtractor:
        if file_extension == "pdf":
            return PDFTextExtractor()
        elif file_extension == "docx":
            return DOCXTextExtractor()
        else:
            return PlainTextExtractor()


def extract_text_from_file(file: IO, file_extension: str) -> str:  # DIP
    """
    Extracts text from a file based on its extension.
    """
    factory = TextExtractorFactory()
    extractor = factory.create_extractor(file_extension)  # DIP: Injecting the dependency
    return extractor.get_text(file)