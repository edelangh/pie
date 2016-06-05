# -*- coding:latin-1 -*-

#importer : sudo apt-get install python-pyaudio
# importer : sudo apt-get install python-pocketsphinx
# importer : sudo apt-get install python-pocketsphinx-hmm-wsj1pocketsphinx-lm-wsj


import pyaudio


def dotask(string):
    print ("hello"+ string)



CHUNK = 1024
FORMAT = pyaudio.paInt16
#format audio
CHANNELS = 2
#nombre de canaux pr enregistrer
RATE = 44100
RECORD_SECS = 5

p=pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
#definition du flux a enregistrer

frames=[]
for i in range(0,int(RATE/CHUNK*RECORD_SECS)):
    data=stream.read(CHUNK)
    frames.append(data)
#on enregistre dans un buffer temp

wf = open('filename.wav', 'rwb+');
wf.writeframes(frames);



stream.stop_stream()
stream.close()
p.terminate()

import wave
#wf=wave.open("filename.wav","rb")
#on ouvre et renomme le wave

p=pyaudio.PyAudio()

stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getchannels(),rate=wf.getframerate(),output=True)
#on ouvre le flux avec les params du wave

data=wf.readframes(CHUNK)
while data != '':
    stream.write(data)
    data=wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()





import pocketsphinx as ps
import sphinxbase

hmmd='/usr/share/pocketsphinx/model/hmm/wsj1'
lmd='/usr/share/pocketsphinx/lm/wsj/wlist5o.3e-7.vp.tg.lm.DMP'
dictd='/usr/share/pocketsphinx/lm/wsj/wlist5o.dic'
d=ps.Decoder(hmm=hmmd, lm=lmd, dict=dictd)
#on crée un décodeur

wavFile=file('my_file.wav','rb')
wavFile.seek(44)
#on vire l'entete

d.decode_raw(wavFile)
results=d.get_hyp()

decoded_speech=results[0]
print ("i want", decoded_speech[0])
dotask(str(decoded_speech[0]))



#pour temps réel : stream_callback, ou alors ca 

#import pyaudio

#q=pyaudio.PyAudio()
#in_stream=p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=1024)
#in_stream.start_stream()
#on ouvre un flux entrant pour décodage tps réel

#d.start_utt()
#while True:
#    buf=in_stream.read(1024)
#    d.process_raw(buf,False,False)
#    results=d.get_hyp()
#             
#    dotask(str(results))
#             #la on peut fouttre les instructions
#
#    break
#d.end_utt()
#
