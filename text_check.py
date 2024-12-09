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
def words_with_1_letters(text):
    word = re.findall(r"\b[a-zA-Z]{1}\b", text)
    if not word:
        return "Words with one character doesn t exists"
    else:
        print("Print words with 1 letter:", word)
        return len(word)

#2
def words_with_2_letters(text):
    word = re.findall(r"\b[a-zA-Z]{2}\b", text)
    if not word:
        return "Words with two characters doesn t exists"
    else:
        print("Print words with 2 letters:", word)
        return len(word)

#3
def words_with_3_letters(text):
    word = re.findall(r"\b[a-zA-Z]{3}\b", text)
    if not word:
        return "Words with three characters doesn t exists"
    else:
        print("Print words with 3 letters:", word)
    return len(word)

#4
def words_with_4_letters(text):
    word = re.findall(r"\b[a-zA-Z]{4}\b", text)
    if not word:
        return "Words with four characters doesn t exists"
    else:
        print("Print words with 4 letters:", word)
        return len(word)

#5
def words_with_5_letters(text):
    word = re.findall(r"\b[a-zA-Z]{5}\b", text)
    if not word:
        return "Words with five characters doesn t exists"
    else:
        print("Print words with 5 letters:", word)
        return len(word)

#6
def words_with_6_letters(text):
    word = re.findall(r"\b[a-zA-Z]{6}\b", text)
    if not word:
        return "Words with six characters doesn t exists"
    else:
        print("Print words with 6 letters:", word)
        return len(word)

#7
def words_with_7_letters(text):
    word = re.findall(r"\b[a-zA-Z]{7}\b", text)
    if not word:
        return "Words with seven characters doesn t exists"
    else:
        print("Print words with 7 letters:", word)
        return len(word)

#8
def words_with_8_letters(text):
    word = re.findall(r"\b[a-zA-Z]{8}\b", text)
    if not word:
        return "Words with eight characters doesn t exists"
    else:
        print("Print words with 8 letters:", word)
        return len(word)

#9
def words_with_9_letters(text):
    word = re.findall(r"\b[a-zA-Z]{9}\b", text)
    if not word:
        return "Words with nine characters doesn t exists"
    else:
        print("Print words with 9 letters:", word)
        return len(word)

#10
def words_with_10_letters(text):
    word = re.findall(r"\b[a-zA-Z]{10}\b", text)
    if not word:
        return "Words with ten characters doesn t exists"
    else:
        print("Print words with 10 letters:", word)
        return len(word)

#11
def words_with_11_letters(text):
    word = re.findall(r"\b[a-zA-Z]{11}\b", text)
    if not word:
        return "Words with eleven characters doesn t exists"
    else:
        print("Print words with 11 letters:", word)
        return len(word)

#12
def words_with_12_letters(text):
    word = re.findall(r"\b[a-zA-Z]{12}\b", text)
    if not word:
        return "Words with twelve characters doesn t exists"
    else:
        print("Print words with 12 letters:", word)
        return len(word)

#13
def words_with_13_letters(text):
    word = re.findall(r"\b[a-zA-Z]{13}\b", text)
    if not word:
        return "Words with thirteen characters doesn t exists"
    else:
        print("Print words with 13 letters:", word)
        return len(word)



#14
def words_with_14_letters(text):
    word = re.findall(r"\b[a-zA-Z]{14}\b", text)
    if not word:
        return "Words with fourteen characters doesn t exists"
    else:
        print("Print words with 14 letters:", word)
        return len(word)



#15
def words_with_15_letters(text):
    word = re.findall(r"\b[a-zA-Z]{15}\b", text)
    if not word:
        return "Words with fifteen characters doesn t exists"
    else:
        print("Print words with 15 letters:", word)
        return len(word)

#16
def words_with_16_letters(text):
    word = re.findall(r"\b[a-zA-Z]{16}\b", text)
    if not word:
        return "Words with sixteen characters doesn t exists"
    else:
        print("Words with 16 letters:", word)
        return len(word)

#17
def words_with_17_letters(text):
    word = re.findall(r"\b[a-zA-Z]{17}\b", text)
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
    
    
    # Verificam intrebarile pentru cuvinte cu 1 - 17 litere

    for i in range(1, 18):
        if f"words with {i}" in question:
            return f"The file contains {globals()[f'words_with_{i}_letters'](content)} words with {i} letters"

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

