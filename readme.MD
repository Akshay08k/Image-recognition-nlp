
# Image Recognition Chatbot with NLP

This project is an image recognition chatbot built using Flask, Natural Language Processing (NLP), and machine learning models. The chatbot can analyze uploaded images, recognize objects within them, and return predictions with associated confidence percentages.

## Features

- **Image Upload**: Users can upload images directly through the web interface.
- **Object Recognition**: The chatbot processes the uploaded image and identifies objects within it.
- **Prediction Confidence**: Displays prediction results with confidence percentages next to each recognized object.
- **NLP Capabilities**: Supports natural language queries related to image recognition results.

## Project Structure

```
├── app.py
├── requirements.txt
├── runtime.txt (optional)
├── vercel.json
├── templates
│   └── index.html
└── static
    └── style.css
```

- **app.py**: The main Flask application file.
- **requirements.txt**: Contains the list of Python dependencies required to run the application.
- **runtime.txt**: Specifies the Python version to be used (optional).
- **vercel.json**: Configuration file for deploying the app on Vercel.
- **templates/index.html**: The HTML template for the web interface.
- **static/style.css**: The CSS file for styling the web interface.

## Prerequisites

- Python 3.8 or later
- Flask
- A Vercel account (for deployment)

## Setup

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/image-recognition-chatbot.git
cd image-recognition-chatbot
```

### 2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the application locally:

```bash
flask run
```

Access the app locally at `http://127.0.0.1:5000`.
