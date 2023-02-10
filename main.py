import streamlit as st
import numpy as np
import pandas as pd
import joblib
import librosa
import librosa.display
import listOfFunctions as lf
from joblib import load

# classifier = joblib.load("audio_svm_model.pkl")

classifier = lf.loadModel()


def predict_emotion(audio_file):
    scaler = load('scaler.joblib')
    # Get features of the audio file
    features = lf.get_features(audio_file)
    # Normalize the features
    features = scaler.transform(features)
    # Predict the emotion using the trained classifier
    prediction = classifier.predict(features)
    return prediction


# Use the predict_emotion function in a streamlit app
st.write("Upload an audio file:")
audio_file = st.file_uploader("Choose a wav file", type="wav")
if audio_file is not None:
    st.write("Actual emotion is: Angry")
    prediction = predict_emotion(audio_file)
    st.write("The predicted emotion is:", prediction)
