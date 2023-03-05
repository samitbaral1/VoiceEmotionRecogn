import streamlit as st
from webAppPage import pages
import streamlit_option_menu as som


# Define the page functions
# @st.cache_data()
def getHomePage():
    st.write("This is the home page.")


# @st.cache_resource()
def getClassifyPage():
    recordAudio.classifyAudio()


# @st.cache_resource()
def contact():
    ph = st.empty()
    ph.title("This is contant")


# Define the page dictionary
pages = {
    "Home": getHomePage,
    "About": getClassifyPage,
    "Contact": contact,
}

# Get the current page from the cache
current_page = st.sidebar.selectbox("Select a page", list(pages.keys()))

# Display the current page
pages[current_page]()

import streamlit as st

# from streamlit import experimental

st.write("Welcome to Page 1")

# Create a link to another page
if st.button("Go to Page 2"):
    contact()
