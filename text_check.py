# what you need to make this app functional
# Import part
import os
import tkinter as tk
from tkinter import filedialog, scrolledtext
import re # we gonna use regex to create some patterns 
from transformers import pipeline
# Install required 
# pip install transformers (i comment this because i already installed this package)


# functions for our app

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_punctuation(text):
    punctuation = re.findall(r'[.,!?;:]', text)
    return len(punctuation)

def count_characters(text):
    return len(text)

# couting words by letters


#1
def words_with_one_letter(text):
    word = re.findall(r"\b\w{1}\b", text)
    if not word:
        return "Words with one character doesn t exists"
    else:
        print("Print words with 1 letter:", word)
        return len(word)

#2
def words_with_two_letters(text):
    word = re.findall(r"\b\w{2}\b", text)
    if not word:
        return "Words with two characters doesn t exists"
    else:
        print("Print words with 2 letters:", word)
        return len(word)

#3
def words_with_three_letters(text):
    word = re.findall(r"\b\w{3}\b", text)
    if not word:
        return "Words with three characters doesn t exists"
    else:
        print("Print words with 3 letters:", word)
    return len(word)

#4
def words_with_four_letters(text):
    word = re.findall(r"\b\w{4}\b", text)
    if not word:
        return "Words with four characters doesn t exists"
    else:
        print("Print words with 4 letters:", word)
        return len(word)

#5
def words_with_five_letters(text):
    word = re.findall(r"\b\w{5}\b", text)
    if not word:
        return "Words with five characters doesn t exists"
    else:
        print("Print words with 5 letters:", word)
        return len(word)

#6
def words_with_six_letters(text):
    word = re.findall(r"\b\w{6}\b", text)
    if not word:
        return "Words with six characters doesn t exists"
    else:
        print("Print words with 6 letters:", word)
        return len(word)

#7
def words_with_seven_letters(text):
    word = re.findall(r"\b\w{7}\b", text)
    if not word:
        return "Words with seven characters doesn t exists"
    else:
        print("Print words with 7 letters:", word)
        return len(word)

#8
def words_with_eight_letters(text):
    word = re.findall(r"\b\w{8}\b", text)
    if not word:
        return "Words with eight characters doesn t exists"
    else:
        print("Print words with 8 letters:", word)
        return len(word)

#9
def words_with_nine_letters(text):
    word = re.findall(r"\b\w{9}\b", text)
    if not word:
        return "Words with nine characters doesn t exists"
    else:
        print("Print words with 9 letters:", word)
        return len(word)

#10
def words_with_ten_letters(text):
    word = re.findall(r"\b\w{10}\b", text)
    if not word:
        return "Words with ten characters doesn t exists"
    else:
        print("Print words with 10 letters:", word)
        return len(word)

#11
def words_with_eleven_letters(text):
    word = re.findall(r"\b\w{11}\b", text)
    if not word:
        return "Words with eleven characters doesn t exists"
    else:
        print("Print words with 11 letters:", word)
        return len(word)

#12
def words_with_twelve_letters(text):
    word = re.findall(r"\b\w{12}\b", text)
    if not word:
        return "Words with twelve characters doesn t exists"
    else:
        print("Print words with 12 letters:", word)
        return len(word)

#13
def words_with_thirteen_letters(text):
    word = re.findall(r"\b\w{13}\b", text)
    if not word:
        return "Words with thirteen characters doesn t exists"
    else:
        print("Print words with 13 letters:", word)
        return len(word)



#14
def words_with_fourteen_letters(text):
    word = re.findall(r"\b\w{14}\b", text)
    if not word:
        return "Words with fourteen characters doesn t exists"
    else:
        print("Print words with 14 letters:", word)
        return len(word)



#15
def words_with_fifteen_letters(text):
    word = re.findall(r"\b\w{15}\b", text)
    if not word:
        return "Words with fifteen characters doesn t exists"
    else:
        print("Print words with 15 letters:", word)
        return len(word)

#16
def words_with_sixteen_letters(text):
    word = re.findall(r"\b\w{16}\b", text)
    if not word:
        return "Words with sixteen characters doesn t exists"
    else:
        print("Words with 16 letters:", word)
        return len(word)

#17
def words_with_seventeen_letters(text):
    word = re.findall(r"\b\w{17}\b", text)
    if not word:
        return "Words with seventeen characters doesn t exists"
    else:
        print("Print words with 16 letters:", word)
        return len(word)


# function to handle the user questions

def handle_question(question, context):
    if "search for words" in question.lower():
        return f"The file contains {count_words(content)} words."
    elif "how many punctuation signs" in question.lower():
        return f"The file contains {count_punctuation(content)} punctuation signs"
    elif "how many characters" in question.lower():
        return f"The file contains {count_characters(content)} characters"
    #1
    elif "words with 1" in question.lower():
        return f"The file contains {words_with_one_letter(content)} words with one letter"
    #2
    elif "words with 2" in question.lower():
        return f"The file contains {words_with_two_letters(content)} words with two letters"
    #3
    elif "words with 3" in question.lower():
        return f"The file contains {words_with_three_letters(content)} words with three letters"
    #4
    elif "words with 4" in question.lower():
        return f"The file contains {words_with_four_letters(content)} words with four letters"
    #5
    elif "words with 5" in question.lower():
        return f"The file contains {words_with_five_letters(content)} words with five letters"

    #6
    elif "words with 6" in question.lower():
        return f"The file contains {words_with_six_letters(content)} words with six letters"

    #7
    elif "words with 7" in question.lower():
        return f"The file contains {words_with_seven_letters(content)} words with seven letters"

    #8
    elif "words with 8" in question.lower():
        return f"The file contains {words_with_eight_letters(content)} words with eight letters"

    #9
    elif "words with 9" in question.lower():
        return f"The file contains {words_with_nine_letters(content)} words with nine letters"

    #10
    elif "words with 10" in question.lower():
        return f"The file contains {words_with_ten_letters(content)} words with ten letters"

    #11
    elif "words with 11" in question.lower():
        return f"The file contains {words_with_eleven_letters(content)} words with eleven letters"

    #12
    elif "words with 12" in question.lower():
        return f"The file contains {words_with_twelve_letters(content)} words with twelve letters"

    #13
    elif "words with 13" in question.lower():
        return f"The file contains {words_with_thirteen_letters(content)} words with thirteen letters"

    #14
    elif "words with 14" in question.lower():
        return f"The file contains {words_with_fourteen_letters(content)} words with fourteen letters"

    #15
    elif "words with 15" in question.lower():
        return f"The file contains {words_with_fifteen_letters(content)} words with fifteen letters"

    #16
    elif "words with 16" in question.lower():
        return f"The file contains {words_with_sixteen_letters(content)} words with sixteen letters"

    #17
    elif "words with 17" in question.lower():
        return f"The file contains {words_with_seventeen_letters(content)} words with seventeen letters"

    else:
        qa_pipeline = pipeline("question-answering", model='distilbert-base-uncased-distilbert-squad')
        response = qa_pipeline(question=question, context=context)
        return response['answer']
    

# function that handle the user question

def ask_question():
    global content
    question = question_entry.get()
    if content:
        answer = handle_question(question, content)
        output_text.insert(tk.END, f"Question: {question}\nAnswer: {answer}\n\n")
    else:
        output_text.insert(tk.END, "No file was uploaded!!!!.\n")







# Loading files in our app
def load_selected_file():
    global content
    selected_file = file_dropdown.get()
    if selected_file and selected_file != "Upload the file":
        try:
            file_path = os.path.join(os.getcwd(), selected_file)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            output_text.insert(tk.END, f"File succesfully uploaded: {selected_file}\nContain {len(content)} characters.\n")
        except Exception as e:
            output_text.insert(tk.END, f"Error when the file was uploaded: {str(e)}\n")
    else:
        output_text.insert(tk.END, "No file selected/ Invalid selection.\n")






# User interface
root = tk.Tk()
root.title("Text checking using AI")


# Dropdown menu for selecting files
def list_text_files():
    current_directory = os.getcwd()
    return [file for file in os.listdir(current_directory) if file.endswith(".txt")]

files = list_text_files()
file_dropdown = tk.StringVar(root)
file_dropdown.set("Select a file")


dropdown_menu = tk.OptionMenu(root, file_dropdown, *files)
dropdown_menu.pack(pady=10)


load_button = tk.Button(root, text="Upload the file", command=load_selected_file)
load_button.pack(pady=10)


# Question area
question_label = tk.Label(root, text = "Write a question about your text file:")
question_label.pack(pady=5)


question_entry = tk.Entry(root, width=50)
question_entry.pack(pady=5)


ask_button = tk.Button(root, text ="Ask the question", command=ask_question)
ask_button.pack(pady=10)


# Area where the answers are displayed
output_text = scrolledtext.ScrolledText(root, width=70, height=20)
output_text.pack(pady=10)

root.mainloop()

