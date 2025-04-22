import speech_recognition as sr
import pyttsx3
import datetime
import requests
import pyaudio
import wikipedia
import webbrowser
from openai import OpenAI


recognizer = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
news_api_key ="f1dcbb5a7eaa493590ffddbf5621b069"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def ai(command):
   clint = OpenAI(
       api_key = "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"

   )
   comletion = clint.chat.completions.create(
         model = "gpt-3.5-turbo",
         messages = [
              {
                "role": "user",
                "content": command
              }
         ]
    )
   mas = comletion.choices[0].message.content
   return mas


def processCommand(c):
    if 'open youtube' in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'open instagram' in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif 'open facebook' in c:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif c.lower().startswith('play'):
        song = c.replace('play', '')
        speak(f"Playing {song}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    elif 'time' in c:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif 'date' in c:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif 'news' in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}")
        if r.status_code == 200:
            data = r.json()
            articales = data.get('articles',[])
            for article in articales:
                speak(article['title'])
    else:
        output = ai(c)
        speak(output)
    

if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print('say something')
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if (word.lower() == 'hello'):
                speak("Yes Sir")
                with sr.Microphone() as source:
                    print('Jarvis is now activet')
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    processCommand(command)
        except Exception as e:
            print("Enter;(0)" , format(e))
