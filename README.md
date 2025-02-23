# ML Memovault

ML Memovault is a Flask-based web application that provides sentiment analysis capabilities through a REST API. The application uses Hugging Face's transformers library to perform sentiment analysis on text input.

## Features

- Sentiment Analysis API endpoint
- Cross-Origin Resource Sharing (CORS) enabled
- Easy-to-use REST API interface

## Tech Stack

- Python
- Flask
- Transformers (Hugging Face)
- PyTorch

## API Endpoints

### 1. Home Endpoint
- **URL:** `/`
- **Method:** `GET`
- **Response:** Returns "Hello World"

### 2. Sentiment Analysis
- **URL:** `/sentiment`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "text": "Your text for sentiment analysis"
  }
  ```
- **Response:** Returns sentiment analysis results

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Swayam-code/ML-Memovault.git
cd ML-Memovault
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## Requirements

See `requirements.txt` for a complete list of dependencies.

## Development

The application runs in debug mode by default when running locally. For production deployment, make sure to disable debug mode and use a production-grade WSGI server like gunicorn.
