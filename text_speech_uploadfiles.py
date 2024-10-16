import streamlit as st
from gtts import gTTS
from io import BytesIO
import os

# Streamlit app title
st.title("Text2Talk Converting Application")

# Text input
text = st.text_area("Enter your text to convert text  to speech")
# Button to trigger TTS
if st.button("Convert to Speech"):
    if text:
        # Convert text to speech
        tts = gTTS(text)        
        audio_stream = BytesIO()
        tts.write_to_fp(audio_stream)
        st.audio(audio_stream)     
    else:
        st.warning("The text not found")
        
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Read and decode the file
    file_text = uploaded_file.read().decode(encoding="utf-8")
    st.subheader( "Uploaded file text_speech_conversion",divider="gray")
    st.text(file_text)
    st.text_area("File Contents", file_text, height=300)
    
if st.button("Convert uploaded file to Speech"):
    if file_text :
        # Convert text to speech
        tts = gTTS(file_text )        
        audio_stream2 = BytesIO()
        tts.write_to_fp(audio_stream2)
        st.audio(audio_stream2)         
    else:
        st.warning("The text not found")


st.markdown(
    """
    <style>
    /* Background color for the app */
    .stApp {
        background-color:#D8DFE4;
    }
    /* Change the color of titles */
    h1 {
        color:#FFFFFF;
        font-family: '{Monospace}';
    }

    </style>
    """,
    unsafe_allow_html=True)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .custom-container {
        background-color: #D5ABD6;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True)





#run - streamlit run text_speech_uploadfiles.py
