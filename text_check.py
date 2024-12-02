# what you need to make this app functional
# Import part
import os
import tkinter as tk
from tkinter import filedialog, scrolledtext
import re # we gonna use regex to create some patterns 
from transformers import pipeline
# Install required 
# pip install transformers (i comment this because i already installed this package)








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


load_button = tk.Button(root, text="Upload the file", command=None)
load_button.pack(pady=10)


# Question area

question_label = tk.Label(root, text = "Write a question about your text file:")
question_label.pack(pady=5)

question_entry = tk.Entry(root, width=50)
question_entry.pack(pady=5)

ask_button = tk.Button(root, text ="Ask the question", command=None)
ask_button.pack(pady=10)


# Are where the answers are displayed

output_text = scrolledtext.ScrolledText(root, width=70, height=20)
output_text.pack(pady=10)

root.mainloop()

