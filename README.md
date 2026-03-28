# Emotion Sentiment Analysis

A simple emotion classification project with two inference options:
- A local ML model (SVM) served by a Flask API.
- An OpenAI-powered model for AI-based emotion prediction.

The Streamlit UI lets you try both models side-by-side.

## Project Structure

- api.py
  - Flask API with two endpoints:
    - /predict uses the local SVM model (svc_model.joblib).
    - /ai-predict uses the OpenAI API for emotion classification.
- streamlit_page.py
  - Streamlit UI that calls the Flask API endpoints.
- train_model.ipynb
  - Notebook used to train the vectorizer and SVM model.
- vector.joblib
  - Saved text vectorizer used by the SVM model.
- svc_model.joblib
  - Saved SVM classifier.
- test.csv
  - Example dataset file (used for testing or experiments).
- requirements.txt
  - Python dependencies for this project.
- .env.example
  - Example environment variable file for OpenAI API key. Do `cp .env.example .env` and fill in your key.
## Emotions and Labels

The ML model predicts an integer label mapped as:
- 0: sadness
- 1: joy
- 2: love
- 3: anger
- 4: fear
- 5: surprise

The AI model returns the label name directly.

## Local Setup

### 1) Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies

```powershell
pip install -r requirements.txt
```

### 3) Run the Notebook (train_model.ipynb)

This run will train the vectorizer and SVM model, then save them as .joblib files for the API to use.

### 4) Configure environment variables (optional for AI endpoint)

Create a .env file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```

If you do not set this, the /ai-predict endpoint will not work.

## Running the Project

### 1) Start the Flask API

```powershell
python api.py
```

The API will run on http://localhost:5000

### 2) Start the Streamlit UI

Open a second terminal:

```powershell
streamlit run streamlit_page.py
```

The UI will open in your browser and let you test both prediction methods.

## API Usage

### Local ML prediction

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"message":"I feel excited and happy"}'
```

Response:
```json
{"Model Prediction":1}
```

### OpenAI prediction

```bash
curl -X POST http://localhost:5000/ai-predict \
  -H "Content-Type: application/json" \
  -d '{"message":"I feel excited and happy"}'
```

Response:
```json
{"AI Prediction":"joy"}
```

## Notes

- The ML model expects English text and uses basic NLTK preprocessing.
- The OpenAI endpoint uses a lightweight model and returns a single label.
- Make sure api.py is running before you open the Streamlit UI.