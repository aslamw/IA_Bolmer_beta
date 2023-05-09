import sounddevice, wavio
#from scipy.io.wavfile import write 
freq = 44100
duration = 2
recording = sounddevice.rec(int(duration * freq),  
                   samplerate=freq, channels=2) 
sounddevice.wait() 
#write("recording0.wav", freq, recording) 
print(recording)

for item in recording:
    with open('testevoz1.txt','a') as o:
        o.write(f'{item}')
#wavio.write("recording1.wav", recording, freq, sampwidth=2)