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



def count_punctuation(text):
    punctuation = re.findall(r'[.,!?;:]', text)
    return len(punctuation) if punctuation else 0

# couting words by letters


#1
def words_with_1_letters(text):
    word = re.findall(r"\b[a-zA-Z]{1}\b", text)
    return len(word) if word else 0
#2
def words_with_2_letters(text):
    word = re.findall(r"\b[a-zA-Z]{2}\b", text)
    return len(word) if word else 0
    

#3
def words_with_3_letters(text):
    word = re.findall(r"\b[a-zA-Z]{3}\b", text)
    return len(word) if word else 0

#4
def words_with_4_letters(text):
    word = re.findall(r"\b[a-zA-Z]{4}\b", text)
    return len(word) if word else 0

#5
def words_with_5_letters(text):
    word = re.findall(r"\b[a-zA-Z]{5}\b", text)
    return len(word) if word else 0

#6
def words_with_6_letters(text):
    word = re.findall(r"\b[a-zA-Z]{6}\b", text)
    return len(word) if word else 0

#7
def words_with_7_letters(text):
    word = re.findall(r"\b[a-zA-Z]{7}\b", text)
    return len(word) if word else 0

#8
def words_with_8_letters(text):
    word = re.findall(r"\b[a-zA-Z]{8}\b", text)
    return len(word) if word else 0

#9
def words_with_9_letters(text):
    word = re.findall(r"\b[a-zA-Z]{9}\b", text)
    return len(word) if word else 0

#10
def words_with_10_letters(text):
    word = re.findall(r"\b[a-zA-Z]{10}\b", text)
    return len(word) if word else 0

#11
def words_with_11_letters(text):
    word = re.findall(r"\b[a-zA-Z]{11}\b", text)
    return len(word) if word else 0

#12
def words_with_12_letters(text):
    word = re.findall(r"\b[a-zA-Z]{12}\b", text)
    return len(word) if word else 0

#13
def words_with_13_letters(text):
    word = re.findall(r"\b[a-zA-Z]{13}\b", text)
    return len(word) if word else 0



#14
def words_with_14_letters(text):
    word = re.findall(r"\b[a-zA-Z]{14}\b", text)
    return len(word) if word else 0



#15
def words_with_15_letters(text):
    word = re.findall(r"\b[a-zA-Z]{15}\b", text)
    return len(word) if word else 0

#16
def words_with_16_letters(text):
    word = re.findall(r"\b[a-zA-Z]{16}\b", text)
    return len(word) if word else 0

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
    
    if "how many punctuation signs" in question.lower():
        return f"The file contains {count_punctuation(content)} punctuation signs"
    
    
    # check the questions from 1 to 17
    for i in range(1, 18):
        if re.search(rf"\bwords with {i}\b", question.lower()):
            function_name = f"words_with_{i}_letters"
            if function_name in globals():
                count = globals()[function_name](content)
                return f"The file contains {count} words with {i} letters"
            else:
                return f"No function defined for {i} letters"
        

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
root.title("Text checking using user input questions")


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

