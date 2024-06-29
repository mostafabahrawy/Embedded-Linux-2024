import os
import speech_recognition
import playsound
import webbrowser
import psutil
import random
from time import ctime
from gtts import gTTS

class voice_assistant:
    recognizer = speech_recognition.Recognizer()

    def record_audio(self):
        with speech_recognition.Microphone() as source:
            print('Listening...')
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio
    
    def reconize_speech(self, audio):
        try:
            text = self.recognizer.recognize_google(audio, language="ar-EG")
            print(f'You said: {text}')
            return text
        except speech_recognition.UnknownValueError:
            print("Sorry, I couldn't understand that, Say it again")
        except speech_recognition.RequestError:
            print("Sorry, There is an error processing your request")
        return ""
    
    def speak(self, audios):
        tts = gTTS(text=audios, lang="ar", slow=False)
        audio = 'audio.mp3'
        tts.save(audio)
        playsound.playsound(audio)
        print(audios)
        os.remove(audio)

def search_words_in_string(word_list, text):
    found_words = [word for word in word_list if word in text]
    return len(found_words)!= 0

def respond(voice_data):
    global alexa
    if search_words_in_string(['اسم', 'الاسم', 'اسمي', 'ازيك'], voice_data):
        alexa.speak('اسمك المعلم بحر طبعا')
    if search_words_in_string(['يوم', 'اليوم', 'النهاردة', 'تاريخ'], voice_data):
        alexa.speak('الوقت الان '+ ctime())
    if search_words_in_string(['الساعه', 'ساعه', 'الساعة', 'ساعة', 'وقت', 'الوقت'], voice_data):
        alexa.speak('الوقت الان '+ ctime().split(" ")[-2])
    if search_words_in_string(['battery', 'البطارية', 'بطارية', 'البطاريه', 'بطاريه'], voice_data):
        alexa.speak('نسبة البطارية ' + str(round(psutil.sensors_battery().percent)) + 'في المائة')

    if search_words_in_string(['google', 'جوجل'], voice_data):
        webbrowser.open('https://www.google.com')
    if search_words_in_string(['youtube', 'يوتيوب'], voice_data):
        webbrowser.open('https://www.youtube.com')
    if search_words_in_string(['facebook', 'فيسبوك'], voice_data):
        webbrowser.open('https://www.facebook.com')
    if search_words_in_string(['Japanese', 'ياباني', 'قاموس'], voice_data):
        webbrowser.open('https://jisho.org/')
    if search_words_in_string(['code', 'كود', 'الكود'], voice_data):
        os.system('code')
    if search_words_in_string(['discord', 'ديسكورد', 'الديسكورد'], voice_data):
        os.system('discord')

    if search_words_in_string(['نكته', 'نكتة', 'joke'], voice_data):
        with open('jokes.txt', 'r') as jokes:
            lines = jokes.readlines()
            random_joke = random.choice(lines).strip()
            alexa.speak(str(random_joke))
    


alexa = voice_assistant()
alexa.speak('Hey Bahr')
while True:
    audio = alexa.record_audio()
    data = alexa.reconize_speech(audio)
    print(data)
    respond(str(data))
