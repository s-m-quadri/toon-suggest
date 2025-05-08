![image](https://github.com/user-attachments/assets/186b26eb-a1e5-4c65-9a18-d19ef3419bdb)

<div align="center">
  <h1><b><code>ToonSuggest</code> Animation Movie Recommender System</b></h1>
  <p><strong>ToonSuggest</strong> is a simple, lightweight, and interactive movie recommender system designed for animation and cartoon titles using IMDb datasets. Built using Python and Tkinter, it allows you to train a recommendation model and get suggestions for similar titles based on textual similarity and user ratings.</p>

  <p>
    <a href="https://s-m-quadri.me/projects/toon-suggest">Homepage</a> ·
    <a href="https://github.com/s-m-quadri/toon-suggest">Repository</a> ·
    <a href="https://github.com/s-m-quadri/toon-suggest/releases">Download Executable</a> ·
    <a href="mailto:dev.smq@gmail.com">Contact</a>
  </p>

  <a href="https://github.com/s-m-quadri/toon-suggest/releases">
         <img src="https://custom-icon-badges.demolab.com/github/v/tag/s-m-quadri/toon-suggest?label=Version&labelColor=302d41&color=f2cdcd&logoColor=d9e0ee&logo=tag&style=for-the-badge" alt="Release Version"/>
  </a>
  <a href="https://www.codefactor.io/repository/github/s-m-quadri/toon-suggest"><img src="https://img.shields.io/codefactor/grade/github/s-m-quadri/toon-suggest?label=CodeFactor&labelColor=302d41&color=8bd5ca&logoColor=d9e0ee&logo=codefactor&style=for-the-badge" alt="GitHub Readme Profile Code Quality"/></a>
  <a href="https://github.com/s-m-quadri/toon-suggest/issues">
    <img src="https://custom-icon-badges.demolab.com/github/issues/s-m-quadri/toon-suggest?label=Issues&labelColor=302d41&color=f5a97f&logoColor=d9e0ee&logo=issue&style=for-the-badge" alt="Issues"/>
  </a>
  <a href="https://github.com/s-m-quadri/toon-suggest/pulls">
    <img src="https://custom-icon-badges.demolab.com/github/issues-pr/s-m-quadri/toon-suggest?label=PRs&labelColor=302d41&color=ddb6f2&logoColor=d9e0ee&logo=git-pull-request&style=for-the-badge" alt="Pull Requests"/>
  </a>
  <a href="https://github.com/s-m-quadri/toon-suggest/graphs/contributors">
    <img src="https://custom-icon-badges.demolab.com/github/contributors/s-m-quadri/toon-suggest?label=Contributors&labelColor=302d41&color=c9cbff&logoColor=d9e0ee&logo=people&style=for-the-badge" alt="Contributors"/>
  </a>

  <p>
    <a href="https://github.com/s-m-quadri/toon-suggest/issues/new?assignees=&labels=bug&projects=&template=bug_report.yml">Report Bug</a> · 
    <a href="https://github.com/s-m-quadri/toon-suggest/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.yml">Request Feature</a> · 
    <a href="https://github.com/s-m-quadri/toon-suggest/discussions/new?category=q-a">Ask Question</a> · 
    <a href="https://github.com/Safouene1/support-palestine-banner/blob/master/Markdown-pages/Support.md">Support 🇵🇸 Palestine<a>
  </p>
</div>


## 📌 **Features**

- GUI-based interface with file selection, training, and recommendation
- Uses TF-IDF vectorization for content-based filtering
- Compatible with IMDb `.tsv.gz` data files
- One-click `.exe` build available (see Releases)
- No external API or internet access required

## 📌 **Getting Started**

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

## 📌 **How It Works**

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

## 📌 **Project Structure**

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

## 📌 **Executable Build**

To create a standalone `.exe`:

```bash
pyinstaller --onefile --noconsole setup.spec
```

Or use the ready-built binary available in [Releases](https://github.com/s-m-quadri/toon-suggest/releases).

## 📌 **IMDb Dataset Download**

ToonSuggest requires two official IMDb dataset files:

1. **title.basics.tsv.gz** – Contains title names, genres, and years  
2. **title.ratings.tsv.gz** – Contains user ratings and number of votes

Download both from the official IMDb dataset portal:

👉 https://datasets.imdbws.com/

### Steps:

- Visit the link above
- Download:
  - `title.basics.tsv.gz`
  - `title.ratings.tsv.gz`
- Keep both files easily accessible for selection during model training

> Note: IMDb datasets are periodically updated, so you may retrain your model when new data becomes available.


## 📌 **Walkthrough: How to Use the App**

### Home Window (`main.py` → `gui_home.py`)

This is the main user interface for movie recommendations.

- **Title Input Field**: Start typing an animated movie title to search
- **Train Model**: Opens the training window to build or rebuild the model
- **Refresh Model**: Reloads an already trained model from `model.pkl`
- **Get Recommendations**: Fetches similar movies to the selected title

> The Get Recommendations button is only enabled when a valid model is loaded.

### Training Window (`gui_train.py`)

Accessed via the "Train Model" button on the Home screen.

- **Choose IMDb Files**:
  - `Choose title.basics.tsv.gz`
  - `Choose title.ratings.tsv.gz`
- **Reset**: Clears selected files and allows re-selection
- **Start Training**:
  - Enabled only when both files are selected
  - Builds the model using TF-IDF vectorization and saves it as `model.pkl`
  - Automatically closes and updates the Home screen once training completes

> During training, all inputs are disabled to avoid interruptions.

## 📌 **License**

This project is licensed under the **GNU General Public License**.

## 📌 **Contact**

For bug reports or feature requests, please contact:
**[dev.smq@gmail.com](mailto:dev.smq@gmail.com)**
