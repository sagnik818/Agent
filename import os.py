import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

speak("I am your personal assistant David how can I help you")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 1
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language = 'en-in').lower()
        print(f"You said: {command}")

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return "None"
    return command

if __name__ == "__main__":
    greet()
    while True:
        command = listen().lower()
        if "youtube" in command:
            webbrowser.open("https://www.youtube.com")

        elif "google" in command:
            webbrowser.open("https://www.google.com")

        elif "music" in command:
            misc_dir = "D:\\SWB Backup\\VOL4\\Roy (2015)"
            songs = os.listdir(misc_dir)
            print(songs)
            os.startfile(os.path.join(misc_dir, songs[9]))
            break

