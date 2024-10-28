# Sentiment Analysis API

This repository provides an API for performing sentiment analysis on text inputs, built using Flask and a sentiment model from Hugging Face. The API allows you to analyze the sentiment of a given text—positive, negative, or neutral—through a prompt-based model.

## Features
- **Text Sentiment Analysis**: Easily analyze the sentiment of any text input.
- **API Integration**: Simple RESTful API for easy integration with other applications.
- **Hugging Face Model Integration**: Uses a model from Hugging Face for reliable sentiment predictions.

## Requirements
- **Python Version**: 3.11
- **Hugging Face API Token**: Required to access the model.

## Installation

1. **Clone the Repository**
```bash
 git clone https://github.com/dsinghdev/sentiment-analysis-api.git
 cd sentiment-analysis-api
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Set Up Hugging Face API Token**
    Create a .env file in the root directory.
    Paste your Hugging Face token into this file:
```bash
HUGGING_FACE_TOKEN=your_hugging_face_token_here
```

## Usage

After setting up, start the API server:
```bash
python main.py
```
You can then send POST requests to the API to analyze the sentiment of text inputs.

## Example Request
POST /predict
Content-Type: application/json
```json
{
  "text": "This is a wonderful day!"
}
```
## Example Response
```json
{
  "sentiment": "positive",
  "confidence": 0.95
}
```