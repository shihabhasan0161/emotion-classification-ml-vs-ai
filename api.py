from flask import Flask, request, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
import joblib
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# openai client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# load vectorizer and model
vectorizer = joblib.load("vector.joblib")
model = joblib.load("svc_model.joblib")


def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    filtered_tokens = [
        token for token in tokens if token not in stopwords.words("english")
    ]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [str(lemmatizer.lemmatize(token)) for token in filtered_tokens]
    return " ".join(lemmatized_tokens)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    message = data["message"]
    clean = preprocess_text(message)
    vec = vectorizer.transform([clean])
    pred = model.predict(vec)
    return jsonify({"Model Prediction": int(pred[0])})


@app.route("/ai-predict", methods=["POST"])
def ai_predict():
    data = request.json
    message = data["message"]
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
        Classify the emotion of this text into one of:
        sadness, joy, love, anger, fear, surprise.

        Text: {message}

        Return ONLY the emotion label.
        """,
    )
    return jsonify({"AI Prediction": response.output_text.strip()})


if __name__ == "__main__":
    app.run()
