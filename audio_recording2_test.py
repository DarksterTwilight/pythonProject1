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

