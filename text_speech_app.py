import streamlit as st
from gtts import gTTS
from io import BytesIO
import os

# Streamlit app title
st.title("Text_to_Speech Converting Application")

# Text input
text = st.text_area("Enter your text to convert text  to speech")

# Button to trigger TTS
if st.button("Convert to Speech"):
    if text:
        # Convert text to speech
        tts = gTTS(text)
       # tts.save("text_speech.mp3")
        
        audio_stream = BytesIO()
        tts.write_to_fp(audio_stream)
        st.audio(audio_stream)
        
    else:
        st.warning("The text not found")