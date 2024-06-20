import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests

# Initialize the recognizer
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        speak("Good morning!")
    elif current_hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I assist you today?")

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()

def tell_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    speak(f"The time is {time}")

def tell_date():
    date = datetime.datetime.now().strftime('%B %d, %Y')
    speak(f"Today's date is {date}")

def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    greet()
    while True:
        query = take_command()
        if "hello" in query:
            speak("Hello! How can I help you?")
        elif "time" in query:
            tell_time()
        elif "date" in query:
            tell_date()
        elif "search" in query:
            speak("What do you want to search for?")
            search_query = take_command()
            search_web(search_query)
        elif "exit" in query:
            speak("Goodbye!")
            break

if __name__ == "_main_":
    main()