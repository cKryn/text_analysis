"""Phrase analysis, according to assignment.txt"""


from pathlib import Path
from docx import Document #Option one!
import docx2txt


WORKING_DIR = Path(__file__).parent.parent
INPUT_DIR = WORKING_DIR / "input_data"


def functionality_library_docx(file):
    """Solve problem with docx library"""
    doc = Document(file)
    result = [parag.text for parag in doc.paragraphs]
    return " ".join(result)


def functionality_library_docx2txt(file):
    """Solve problem with docx2txt library"""
    result = docx2txt.process(file)
    return result.replace("\n", " ")


def character_numbers(reformed_data):
    """Count all the characters in data"""
    reformed_text_1 = reformed_data.replace(" ", "")
    reformed_text_2 = reformed_text_1.replace("\n", "")
    count_1 = len(reformed_text_2)
    print(f"The total number of characters in your 'input_data' is: {count_1}")


def words_numbers(data):
    """Count only words in data"""
    chars_to_remove = ["1","2","3","4","5","6","7","8","9","0","?","!",",",".","-","'"]
    pre_result = ""
    for char in data:
        if char not in chars_to_remove:
            pre_result += char
    pre_result = pre_result.split(" ")
    result = [word for word in pre_result if word != '']
    count = len(result)
    print(f"The total number of words in your 'input_data' is: {count}")


def phrase_numbers(data):
    """Count total number of phrases"""
    phrases = data.replace("!", ".").replace("?", ".").split(".")
    count = len(phrases)
    print(f"The total number of phrases in your 'input_data' is: {count}")
