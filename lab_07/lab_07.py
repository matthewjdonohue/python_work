import string
from pathlib import Path

def list_current_files():
    p = Path(".")
    txt_files = p.glob("*.txt")
    
    print("Available files:")
    for txt_file in txt_files:
        print(txt_file.name)

def get_file():
    while True:
        file_name = input("Enter the name of the file you want to load: ")
        
        try:
            file = open(file_name, 'r', encoding = 'utf-8')
            return file, file_name
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Please try again.")

def search(file, target_word):
    count = 0
    for line in file:
        words = line.split()

        for word in words:
            cleaned_word = word.strip(string.punctuation)
            if cleaned_word.lower() == target_word.lower():
                count += 1
    return count


if __name__ == "__main__":
    while True:
        list_current_files()
        file_object, file_name = get_file()
        target_word = input("Enter the word you want to search for: ")
        word_count = search(file_object, target_word)
        file_object.close()
        
        message = f"The word '{target_word}' appeared {word_count} times in the file '{file_name}'."
        print(message)
        
        with open("output.txt", 'a') as output_file:  
            output_file.write(message + '\n')  
        repeat = input("Would you like to search again? Y/n: ")   
        if repeat.lower() != "y":
            break
        
