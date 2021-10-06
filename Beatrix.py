import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning,Sir!")
        speak("Good Morning,Sir!")
    elif hour>=12 and hour<18:
        print("Good Afternoon,Sir!")
        speak("Good Afternoon,Sir!")
    else:
        print("Good Evening,Sir!")
        speak("Good Evening,Sir!")
    print("I am Beatrix. How can I help you?")
    speak("I am Beatrix. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("PLEASE Say that again..")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for exec tasks based on query
        if 'on wikipedia search' in query or 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia,")
            print("According to wikipedia,")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play the big bang theory' in query:
            series_dir = "M:\\Series\\Big Bang Theory\\BBT-S01"
            bbt = os.listdir(series_dir)
            print(bbt)
            os.startfile(os.path.join(series_dir,bbt[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir,the time is {strTime}")
            speak(f"Sir,the time is {strTime}")

        elif 'open teams' in query:
            teamsPath = "C:\\Users\\kxhx.m\\AppData\\Local\\Microsoft\\Teams\\current\\Teams"
            os.startfile(teamsPath)

        elif 'how are you' in query:
            print("I am all good sir,Thank you!")
            speak("I am all good sir,Thank you!")

        elif 'open vlc' in query:
            os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")

        elif 'quit' in query or 'bye' in query:
            print("Quitting sir, Bye. Thank you for your time.!")
            speak("Quitting sir, Bye. Thank you for your time.!")
            exit()