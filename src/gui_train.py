import src.train as train


import threading
import tkinter as tk
from tkinter import filedialog
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class TrainGUI:
    def __init__(self, master, on_complete):
        self.master = master
        self.on_complete = on_complete
        self.master.title("Train Recommender Model")
        self.master.iconbitmap(resource_path("icon.ico"))
        self.master.geometry("500x300")
        self.master.configure(bg='#fff3b0')

        self.basics_path = None
        self.ratings_path = None

        self.create_widgets()

    def create_widgets(self):
        default_font = ('Comic Sans MS', 10)
        self.master.option_add("*Font", default_font)

        tk.Label(self.master, text="Train Recommender Model", bg='#fff3b0',
                font=('Comic Sans MS', 14, 'bold')).pack(pady=(25, 10))

        # Vertical buttons for file selection
        file_frame = tk.Frame(self.master, bg='#fff3b0')
        file_frame.pack(pady=5, fill='x')

        self.btn_basics = tk.Button(file_frame, text="Choose IMDb title.basics.tsv.gz",
                                    command=self.select_basics, bg='#fff3b0', relief='groove',
                                    padx=15, pady=6)
        self.btn_basics.pack(pady=5)

        self.btn_ratings = tk.Button(file_frame, text="Choose IMDb title.ratings.tsv.gz",
                                    command=self.select_ratings, bg='#fff3b0', relief='groove',
                                    padx=15, pady=6)
        self.btn_ratings.pack(pady=5)

        # Horizontal row of Reset + Train
        bottom_frame = tk.Frame(self.master, bg='#fff3b0')
        bottom_frame.pack(pady=(10, 20))

        self.btn_reset = tk.Button(bottom_frame, text="Reset", command=self.reset,
                                bg='#fff3b0', relief='groove',
                                padx=15, pady=6, state='disabled')
        self.btn_reset.pack(side='left', padx=10)

        self.btn_train = tk.Button(bottom_frame, text="Start Training", command=self.train_model,
                                bg='#f4a261', activebackground='#e76f51', fg='black',
                                font=('Comic Sans MS', 10), relief='groove',
                                padx=15, pady=6, state='disabled')
        self.btn_train.pack(side='left', padx=10)

        self.status_bar = tk.Label(self.master, text="Status: Waiting for IMDb data files...",
                                bd=1, relief='sunken', anchor='w', bg='#ffeb99',
                                font=('Comic Sans MS', 10))
        self.status_bar.pack(side='bottom', fill='x')

    def select_basics(self):
        path = filedialog.askopenfilename(filetypes=[("TSV GZ files", "*.tsv.gz")])
        if path:
            self.basics_path = path
            self.btn_basics.config(state='disabled')
            self.update_status("Selected: title.basics.tsv.gz")
            self.update_button_states()

    def select_ratings(self):
        path = filedialog.askopenfilename(filetypes=[("TSV GZ files", "*.tsv.gz")])
        if path:
            self.ratings_path = path
            self.btn_ratings.config(state='disabled')
            self.update_status("Selected: title.ratings.tsv.gz")
            self.update_button_states()

    def reset(self):
        self.basics_path = None
        self.ratings_path = None
        self.btn_basics.config(state='normal')
        self.btn_ratings.config(state='normal')
        self.update_button_states()
        self.update_status("Selections have been cleared.")

    def check_ready(self):
        if self.basics_path and self.ratings_path:
            self.btn_train.config(state='normal')

    def train_model(self):
        # Disable everything
        self.btn_train.config(state='disabled')
        self.btn_basics.config(state='disabled')
        self.btn_ratings.config(state='disabled')
        self.btn_reset.config(state='disabled')
        self.update_status("Training the recommender model... Please wait.")
        
        def run_training():
            data = train.load_and_prepare_data(self.basics_path, self.ratings_path)
            tfidf, tfidf_matrix = train.train_model(data)
            train.save_model(data, tfidf, tfidf_matrix)
            self.update_status("Training complete! This window will close shortly.")
            self.master.after(2000, lambda: [self.on_complete(), self.master.destroy()])

        threading.Thread(target=run_training).start()

        threading.Thread(target=run_training).start()

    def update_status(self, message):
        self.status_bar.config(text=f"Status: {message}")

    def update_button_states(self):
        has_basics = self.basics_path is not None
        has_ratings = self.ratings_path is not None

        self.btn_reset.config(state='normal' if has_basics or has_ratings else 'disabled')
        self.btn_train.config(state='normal' if has_basics and has_ratings else 'disabled')