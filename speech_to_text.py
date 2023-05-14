import speech_recognition as sr

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()  # instance created
    with sr.AudioFile(filename) as source:
        print(filename)
        audio = recognizer.record(source)  # record the audiofile provided
        print(audio)
    try:
        print('trying')
        return recognizer.recognize_google(audio)  # speech to text conversion using google recognizer
    except Exception as exception:
        print('I did not quite catch that')
        print(exception)
        return 'None'



