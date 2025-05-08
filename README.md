# 🎨 Portfolio Web App

A Python-based web application to showcase your projects and certificates. This app allows you to display your work and credentials in a structured and visually appealing manner.

## 🚀 Features

- Display a list of your projects with descriptions and links.
- Showcase your certificates with relevant details.
- Send emails directly from the app using the integrated email functionality.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Max-creates/portfolio_web_app.git
   cd portfolio_web_app
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

1. **Run the application:**
   ```bash
   streamlit run Home.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5000/
   ```

3. **Explore your portfolio and certificates displayed on the web app.**

## 📁 Project Structure

```
portfolio_web_app/
├── certificates/          # Contains certificate images
├── images/                # Contains project images
├── pages/                 # HTML templates for different pages
├── Home.py                # Main application script
├── send_email.py          # Script to handle email functionality
├── certificates.csv       # CSV file containing certificate details
├── data.csv               # CSV file containing project details
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
