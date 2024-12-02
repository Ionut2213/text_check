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


# function to handle the user questions

def handle_question(question, context):
    if "search for words" in question.lower():
        return f"The file contains {count_words(content)} words."
    elif "how many punctuation signs" in question.lower():
        return f"The file contains {count_punctuation(content)} punctuation signs"
    elif "how many characters" in question.lower():
        return f"The file contains {count_characters(content)} characters"
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
        output_text.insert(tk.END, "No file was uploaded.\n")







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
root.title("Text checker using AI")


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

