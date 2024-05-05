import os
import streamlit as st
from gtts import gTTS

st.title("Text to Speech Converter")

# Input text box for user input
text_input = st.text_area("Enter text here:")

# Function to generate audio and save to file
def generate_audio(text, filename='output.mp3'):
    tts = gTTS(text, lang='en')
    tts.save(filename)

# Button to generate audio and play it
if st.button("Generate Audio"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        generate_audio(text_input)
        st.success("Audio generated successfully!")
        st.audio('output.mp3', format='audio/mp3')

