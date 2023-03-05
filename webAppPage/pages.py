import listOfFunctions as lf
import streamlit as st
from st_custom_components import st_audiorec
import tempfile
import pandas as pd
from webAppPage import utility

allFeaturesCombinedPath = "E:/EM/featuresFrommAllIndividualCombinedDatasets.xlsx"
allFeaturesCombined = pd.read_excel(allFeaturesCombinedPath)


def homepage():
    st.markdown("""# <div style="text-align:center">Speech Emotion Recognition using Support Vector Machine(SVM)""",
                unsafe_allow_html=True)
    st.write(
        """#### <div style = "text-align:center">Number of features after augmentation for each classes""" +
        """ from:</div><br>""",
        unsafe_allow_html=True)
    utility.getEmotionsFromEachDS_Dict()
    st.write(
        """#### <div style = "text-align:center">Number of features for each label after combining all datasets""" +
        """</div><br>""",
        unsafe_allow_html=True)
    col = st.columns(5)
    with col[2]:
        st.write(utility.getEmotionsCount(allFeaturesCombined))


def classifyAudio():
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
        st.write("<div style='text-align: center;'>The predicted emotion is:", prediction[0].capitalize(), "</div",
                 unsafe_allow_html=True)


def getContactPage():
    recipient_email = 'samitbaral12@gmail.com'
    gmail_url = f'mailto:{recipient_email}'
    st.write(
        f'<div style="text-align: center;">To contact us, click <a href="{gmail_url}">here</a> to send us an '
        f'email.</div>',
        unsafe_allow_html=True
    )
