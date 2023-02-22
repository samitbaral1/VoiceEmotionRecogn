import streamlit as st
import numpy as np
import pandas as pd
import joblib
import librosa
import librosa.display
import listOfFunctions as lf
from joblib import load
import os
import numpy as np
import streamlit as st
from io import BytesIO
from st_custom_components import st_audiorec
import io
import tempfile

# classifier = joblib.load("audio_svm_model.pkl")

classifier = lf.loadModel()

wav_audio_data = st_audiorec()
if wav_audio_data is not None:
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.wav', delete=False) as temp_file:
        temp_file.write(wav_audio_data)
    temp_file_name = temp_file.name
    pred = lf.predict_emotion(temp_file_name, classifier)
    st.write("The predicted emotion is: ", pred)

# Use the predict_emotion function in a streamlit app
st.write("Upload an audio file:")
audio_file = st.file_uploader("Choose a wav file", type="wav")
if audio_file is not None:
    prediction = lf.predict_emotion(audio_file, classifier)
    st.write("The predicted emotion is:", prediction)
