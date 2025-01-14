import streamlit as st
from gtts import gTTS
import os

# Function to convert text to speech
def save_and_play_audio(text, language='en'):
    try:
        # Convert text to speech
        tts = gTTS(text=text, lang=language, slow=False)
        
        # Save the audio to a BytesIO object (in memory)
        audio = "audio.mp3"
        tts.save(audio)
        # Return the audio file in memory to play in Streamlit
        return audio
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit UI
st.title("Text to Speech Converter")

# Input text from the user
user_text = st.text_area("Enter text to convert to audio:")

# Language selection (optional)
selected_language = st.selectbox("Select Language", ['en', 'es', 'fr', 'de', 'it'])

def main():
    # Button to trigger conversion
    if st.button("Convert to Audio"):
        if user_text.strip() == "":
            st.warning("Please enter some text to convert.")
        else:
            # Convert text to audio (without saving to file)
            audio_file = save_and_play_audio(user_text, selected_language)
            if audio_file:
                st.success("Audio generated successfully!")
                
                # Play the audio in the Streamlit app
                st.audio(audio_file, format="audio/mp3")
                
                # Option to download the audio file
                st.download_button(
                    label="Download Audio",
                    data=audio_file,
                    file_name="output_audio.mp3",
                    mime="audio/mp3"
                )
            
            # delete the audio file
            os.remove("audio.mp3")

# Run the app
if __name__ == "__main__":
   main()
