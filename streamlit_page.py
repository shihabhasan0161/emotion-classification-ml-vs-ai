import streamlit as st
import requests

label_map = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}

st.title("Emotion Analysis App")

st.write("""
This app classifies emotion into:
sadness=0, joy=1, love=2, anger=3, fear=4, surprise=5
""")

message = st.text_input("Enter your message here")

col1, col2 = st.columns(2)
with col1:
    ml_send_btn = st.button("Predict with ML Model")
with col2:
    ai_send_btn = st.button("Predict with AI Model")

if ml_send_btn and message:
    try:
        response = requests.post(
            "http://localhost:5000/predict",
            json={"message": message}
        )
        pred = response.json()["Model Prediction"]
        emotion = label_map.get(pred, str(pred))

        st.write(f"**ML Prediction:** {emotion}")
    except Exception as e:
        st.error(f"Error connecting to ML API: {e}")
    
if ai_send_btn and message:
    try:
        response = requests.post(
            "http://localhost:5000/ai-predict",
            json={"message": message}
        )
        pred = response.json()["AI Prediction"]

        st.write(f"**AI Prediction:** {pred}")
    except Exception as e:
        st.error(f"Error connecting to AI API: {e}")