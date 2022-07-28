import pyttsx3
import speech_recognition as sr

tts = pyttsx3.init()
voices = tts.getProperty('voices')

# set 'human'
tts.setProperty('voice', voices[1].id) # Irina
# tts.setProperty('voice', voices[1].id) # Microsoft Zira
# tts.setProperty('voice', voices[2].id) # Alexander

tts.setProperty('rate', 220)

# duration = 5
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
while True:
    try:
        with mic as source:
            print('Скажите что-нибудь..')
            tts.say('Скажите что-нибудь..')
            tts.runAndWait()
            # r.adjust_for_ambient_noise(source)
            # audio = r.record(mic, duration)
            audio = r.listen(source)
        q = r.recognize_google(audio, language='ru')
        print(q + '\n')
        tts.say(q)
        tts.runAndWait()
    except:
        print('Я жду...')
        tts.say('Я жду...')
        tts.runAndWait()
        continue
