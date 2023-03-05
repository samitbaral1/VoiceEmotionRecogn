import streamlit as st
import streamlit_option_menu as som
from webAppPage import pages

st.set_page_config(
    page_title="Sound Emotion Recognition",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "## Final year project. \n"
                 "#**Team Members:**\n 1. Samit Baral\n 2. Menuka Sharma "
                 "\n 3. Samrat Kafle"
    }
)
selected = som.option_menu(
    menu_title=None,
    options=["Homepage", "Audio Classifier", "Contact"],
    icons=["house-fill", "soundwave", "telephone-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Homepage":
    pages.homepage()
elif selected == "Audio Classifier":
    pages.classifyAudio()
elif selected == "Contact":
    pages.getContactPage()
