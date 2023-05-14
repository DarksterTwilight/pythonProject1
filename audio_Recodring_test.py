import pyaudio
import wave
import os
import datetime

# Set up the PyAudio object
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

#
RECORD_SECONDS = 30

# Get the current date and time for use in the file name
now = datetime.datetime.now()
file_name = "recording.wav"

def record_audio():
    # Create a PyAudio object
    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recording as a WAV file
    wave_file = wave.open(file_name, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    print("Recording saved as {}".format(file_name))


