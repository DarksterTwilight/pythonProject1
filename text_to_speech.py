import pyttsx3
from gtts import gTTS
from playsound import playsound
import tempfile
import os




def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def text_to_speech2(text):
    # Create a temporary directory to store the audio file
    temp_dir = tempfile.mkdtemp()
    audio_path = os.path.join(temp_dir, "output.mp3")

    # Perform text-to-speech conversion
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(audio_path)

    # Play the audio
    playsound(audio_path)

    # Remove the temporary directory and audio file
    os.remove(audio_path)
    os.rmdir(temp_dir)


