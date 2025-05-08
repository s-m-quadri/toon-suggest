# ToonSuggest

ToonSuggest is a simple, lightweight, and interactive movie recommender system designed for animation and cartoon titles using IMDb datasets. Built using Python and Tkinter, it allows you to train a recommendation model and get suggestions for similar titles based on textual similarity and user ratings.

📌 **Features**

- GUI-based interface with file selection, training, and recommendation
- Uses TF-IDF vectorization for content-based filtering
- Compatible with IMDb `.tsv.gz` data files
- One-click `.exe` build available (see Releases)
- No external API or internet access required

📌 **Getting Started**

### 1. Clone the Repository

```bash
git clone https://github.com/s-m-quadri/toon-suggest.git
cd toon-suggest
````

### 2. Install Dependencies

Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python main.py
```

Or download the pre-built `.exe` from the [Releases](https://github.com/s-m-quadri/toon-suggest/releases) section to run without Python.

📌 **How It Works**

1. **Train the Model**

   * Launch the training window and select:

     * `title.basics.tsv.gz`
     * `title.ratings.tsv.gz`
   * Click "Start Training" to preprocess and vectorize the data.
   * A trained `model.pkl` file is generated and saved.

2. **Get Recommendations**

   * Launch the main window.
   * Load the trained model.
   * Enter the name of a movie and click "Get Recommendations".

📌 **Project Structure**

```
ToonSuggest/
├── main.py                  # Entry point for the GUI application
├── model.pkl                # Sample trained model (for demo/testing)
├── setup.spec               # PyInstaller config for .exe build
├── requirements.txt         # Python dependencies
└── src/
    ├── gui_home.py          # Main recommendation GUI
    ├── gui_train.py         # Model training GUI
    ├── recommend.py         # TF-IDF recommendation logic
    └── train.py             # Data loading, training, and saving logic
```

📌 **Executable Build**

To create a standalone `.exe`:

```bash
pyinstaller --onefile --noconsole setup.spec
```

Or use the ready-built binary available in [Releases](https://github.com/s-m-quadri/toon-suggest/releases).

📌 **License**

This project is licensed under the **GNU General Public License**.

📌 **Contact**

For bug reports or feature requests, please contact:
**[dev.smq@gmail.com](mailto:dev.smq@gmail.com)**