import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Diga algo!")
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {text}")
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
        except sr.RequestError as e:
            print(f"Erro ao acessar o serviço de reconhecimento de fala: {e}")