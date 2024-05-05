import streamlit as st
import io
import os

# Import the Google Cloud client library
from google.cloud import speech_v1p1beta1 as speech

# Set up environment variable for Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_service_account_json_file.json"

def transcribe_audio(audio_file):
    # Create a SpeechClient object
    client = speech.SpeechClient()

    # Read the audio file
    content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    # Configure the speech recognition request
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",  # Change this to the appropriate language code
    )

    # Perform the speech recognition
    response = client.recognize(request={"config": config, "audio": audio})

    # Print the transcription
    for result in response.results:
        return result.alternatives[0].transcript

# Streamlit web interface
st.title("Speech to Text Transcription")

# Upload audio file
audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])

if audio_file:
    # Display uploaded audio file
    st.audio(audio_file, format='audio/wav')

    # Transcribe audio when the user clicks the button
    if st.button("Transcribe"):
        transcript = transcribe_audio(audio_file)
        st.write("Transcription:")
        st.write(transcript)
