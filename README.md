# 🎬 IMDB Movie Data Scraper

IMDB Movie Data Scraper is a Python script that extracts upcoming movie information from **IMDB**, including **movie name, categories, and cast**. The extracted data is then saved in **CSV** and **JSON** formats.

## 📑 Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Required Libraries](#required-libraries)
- [Files](#files)

## 📂 Project Structure

imdb-movie-scraper 
    
    │── data/ # Folder for storing extracted data │ 
        ├── movies.csv # Extracted movie data in CSV format │ 
        ├── movies.json # Extracted movie data in JSON format │ 
    │── get_data.py # Main script for extracting movie data 
    │── requirements.txt # List of required Python libraries 
    │── README.md # Project documentation │



## ⚙️ Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/image-compressor.git
   cd image-compressor
2. **(Optional) Create a virtual environment:**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. **Install dependencies:**
   ```bash
    pip install -r requirements.txt
4. **Run the application:**
   ```bash
    streamlit run app.py

## 🚀 Usage
1. Upload an image (JPG, JPEG, PNG).
2. The app will automatically compress the image to be under 1MB while maintaining quality.
3. Download the compressed image.
## 📦 Required Libraries
Ensure you have the following Python libraries installed:

- `streamlit`
- `PIL` (Pillow)
- `io`

## 📄 Files
- `app.py`: Main Streamlit application script that:
    - Accepts image uploads
    - Compresses images to be under 1MB
    - Allows users to download the compressed image
- `requirements.txt`: List of required Python libraries.
- `README.md`: Project documentation.