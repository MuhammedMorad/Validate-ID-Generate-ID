
# National ID Validator & Generator 🇪🇬

This project is an Egyptian National ID Validator and Generator built using Streamlit. It allows users to:

- **Validate** a 14-digit Egyptian National ID by analyzing personal information such as birth date, gender, and governorate.
- **Generate** a valid National ID based on user-provided birth date, gender, and governorate.

## Features

- **National ID Validation:** Ensures the provided National ID follows the correct format and extracts personal details.
- **National ID Generation:** Generates a valid National ID from a given birth date, gender, and governorate.
- **Multi-language Support:** The application supports both English and Arabic, offering a user-friendly interface.

## Installation

To run this project locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/national-id-validator-generator.git
cd national-id-validator-generator
```

### 2. Install dependencies

Make sure you have Python 3.x installed. Then, install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Run the app

After the dependencies are installed, run the application with:

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser to access the application.

## Project Structure

```
national-id-validator-generator/
│
├── app.py                  # Main Streamlit app
├── img/                    # Image folder for icons (LinkedIn, Facebook, WhatsApp)
│   ├── linkedin.png
│   ├── facebook.png
│   └── whatsapp.png
├── requirements.txt        # List of Python dependencies
└── README.md               # This file
```
