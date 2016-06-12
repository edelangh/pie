import pyaudio
import wave
import sys
import thread
import time
import speech_recognition as sr
from subprocess import Popen, PIPE

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 4
output_file = "file-"
 
def main(output):
    audio = pyaudio.PyAudio()
     
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print "recording..."
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print "finished recording"
     
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
     
    print "saving..."
    waveFile = wave.open(output, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    print "reading..."
    # use "output" as the audio source
    r = sr.Recognizer()
    with sr.WavFile(output) as source:
        audio = r.record(source) # read the entire WAV file
    # recognize speech using Google Speech Recognition
    print "treating..."
    try:
        text = r.recognize_google(audio)
        print("You said " + text)
        Popen("curl localhost:8080/" + text.replace(" ", "_"))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results")

for i in range(100):
    thread.start_new_thread(main, (output_file + str(i) + ".wav", ) ) 
    time.sleep(2)

time.sleep(1)
