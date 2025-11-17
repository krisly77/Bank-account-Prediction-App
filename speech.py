import streamlit as st
import speech_recognition as sr

def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info('speak now...')
        #listen for speech and store in audio text variable
        audio_text = r.listen(source)
        st.info('transcribing...')

        try:
            #using Google speech recognitionn
            text = r.recognize_google(audio_text)
            return text
        
        except:
            return "Sorry, I did not get that."
        
def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")
    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech()
        st.write("Transcription: ", text)
if __name__ == "__main__":
    main()