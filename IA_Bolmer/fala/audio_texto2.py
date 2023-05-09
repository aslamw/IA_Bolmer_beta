
import os
import json
import vosk
import pyaudio
#r"C:\Users\wgngu\Desktop\Bolmer\IA_Bolmer\fala\pt"

vosk.SetLogLevel(-1)

if not os.path.exists(r"./pt"):
        print ("Modelo em portugues nao encontrado.")
        exit (1)

def test_speack(): 
    
    model = vosk.Model(r"./pt2")
    sample_rate = 16000
    buffer_size = 4000
    
    recognition_config = vosk.KaldiRecognizer(model, sample_rate)
    p = pyaudio.PyAudio()
    
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=buffer_size)
    stream.start_stream()
    
    print('listener...')
    
    while True:
        
        data = stream.read(buffer_size)
        
        if len(data) == 0:
            break
        
        if recognition_config.AcceptWaveform(data):
            
            resultado = json.loads(recognition_config.Result())
            return resultado['text']   
if __name__ == "__main__":
    
    print(test_speack())