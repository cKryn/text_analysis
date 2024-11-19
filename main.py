"""Main root of the program - file analysis"""


from src.file_analysis import *


print("Choose an option:")
print("1. Use library docx")
print("2. Use library docx2txt")


file = INPUT_DIR / "text.docx"


try:
    while True:
        user_choice = input("Please choose a library to solve the problem: ")
        if user_choice == "1":
            print("Using docx library...")
            data = functionality_library_docx(file)
            break
        elif user_choice == "2":
            print("Using docx2txt library...")
            data = functionality_library_docx2txt(file)
            break
        else:
            print("Invalid option. Choose 1 or 2")
    character_numbers(data)  # Inside function -> Print all character_numbers
    words_numbers(data)  # Inside function -> Print all words_numbers
    phrase_numbers(data)  # Inside function -> Print all phrase_numbers
except FileNotFoundError:
    print("From your 'input_data' directory, the actually docx file is missing!")
