import src.recommend as recommend
from src.gui_train import TrainGUI

import tkinter as tk
from tkinter import messagebox, ttk

MODEL_PATH = 'model.pkl'

class HomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("IMDB-Based Animation Movie Recommender")
        self.root.geometry("700x450")
        self.root.configure(bg='#fff3b0')

        self.data = None
        self.tfidf_matrix = None
        self.model_loaded = False

        self.create_widgets()

    def create_widgets(self):
        default_font = ('Comic Sans MS', 11)
        self.root.option_add("*Font", default_font)
        btn_style = {'padx': 15, 'pady': 6, 'font': ('Comic Sans MS', 11)}

        # Title
        tk.Label(self.root, text="IMDB-Based Animation Movie Recommender", bg='#fff3b0',
                font=('Comic Sans MS', 18, 'bold')).pack(pady=(40, 5))

        # Subtitle / Description
        tk.Label(self.root, text="Discover similar animation movies by typing a title below.",
                bg='#fff3b0', font=('Comic Sans MS', 10, 'italic')).pack(pady=(0, 15))

        # Movie search field
        self.movie_var = tk.StringVar()
        self.dropdown = ttk.Combobox(self.root, textvariable=self.movie_var, width=90, font=('Comic Sans MS', 12))
        self.dropdown.pack(padx=20, pady=(0, 10), fill='x')
        self.dropdown.config(state='disabled')

        # Button row
        btn_frame = tk.Frame(self.root, bg='#fff3b0')
        btn_frame.pack(pady=(5, 15))

        tk.Button(btn_frame, text="Train Model", command=self.open_training_window,
                bg='#fff3b0', relief='groove', **btn_style).pack(side='left', padx=10)

        tk.Button(btn_frame, text="Reload Model", command=self.reload_model,
                bg='#fff3b0', relief='groove', **btn_style).pack(side='left', padx=10)

        self.get_button = tk.Button(btn_frame, text="Get Recommendations", command=self.get_recommendations,
                                    bg='#f4a261', activebackground='#e76f51', fg='black',
                                    relief='groove', state='disabled', **btn_style)
        self.get_button.pack(side='left', padx=10)

        # Output area (smaller height, but scrollable)
        self.result_box = tk.Text(self.root, height=8, width=90, font=('Comic Sans MS', 11), wrap='word')
        self.result_box.pack(pady=(0, 15), padx=20, fill='both', expand=False)

        self.status_bar = tk.Label(self.root, text="Status: Waiting for input...", bd=1, relief='sunken',
                                anchor='w', bg='#ffeb99', font=('Comic Sans MS', 10))
        self.status_bar.pack(side='bottom', fill='x')

        self.reload_model()

    def reload_model(self):
        try:
            self.data, _, self.tfidf_matrix = recommend.load_model(MODEL_PATH)
            self.full_movie_list = sorted(self.data['primaryTitle'].unique().tolist())
            self.dropdown['values'] = self.full_movie_list
            self.dropdown.config(state='normal')
            self.dropdown.bind("<KeyRelease>", self.update_dropdown)
            self.dropdown.bind("<Button-1>", lambda e: self.dropdown.event_generate('<Down>'))
            self.get_button.config(state='normal')
            self.model_loaded = True
            self.update_status("Model loaded successfully.")
        except:
            self.model_loaded = False
            self.get_button.config(state='disabled')
            self.dropdown.config(state='readonly')
            self.dropdown['values'] = []
            self.full_movie_list = []
            self.data = None
            self.tfidf_matrix = None
            self.dropdown.delete(0, tk.END)
            self.dropdown.bind("<KeyRelease>", lambda e: None)
            self.dropdown.bind("<Button-1>", lambda e: None)
            self.dropdown.bind("<FocusIn>", lambda e: None)
            messagebox.showerror("Error", "Failed to load model.pkl")
            self.update_status("Model loading failed.")

    def update_dropdown(self, event):
        value = self.movie_var.get().lower()
        filtered = [title for title in self.full_movie_list if value in title.lower()]
        self.dropdown['values'] = filtered[:100]

    def open_training_window(self):
        train_win = tk.Toplevel(self.root)
        TrainGUI(train_win, self.reload_model)

    def get_recommendations(self):
        if not self.model_loaded:
            messagebox.showerror("Error", "Model not loaded.")
            return

        title = self.movie_var.get()
        results = recommend.get_recommendations(title, self.data, self.tfidf_matrix, top_n=10)

        self.result_box.delete(1.0, tk.END)
        if results.empty:
            self.result_box.insert(tk.END, "No recommendations found.")
        else:
            self.result_box.insert(tk.END, f"Recommendations for: {title}\n\n")
            for _, row in results.iterrows():
                self.result_box.insert(tk.END, f"{row['primaryTitle']} (Rating: {row['averageRating']})\n")
            self.update_status("Recommendations displayed.")

    def update_status(self, message):
        self.status_bar.config(text=f"Status: {message}")