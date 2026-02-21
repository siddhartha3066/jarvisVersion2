import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import requests

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except Exception as e:
        print("Error:", e)
        speak("Say that again please")
        return ""

def get_news():
    api_key = "your API"

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    try:
        response = requests.get(url)
        news_data = response.json()

        articles = news_data["articles"][:3]

        speak("Here are today's top headlines")

        for article in articles:
            speak(article["title"])

    except Exception as e:
        print("News Error:", e)
        speak("Sorry, I could not fetch news")

def process_command(command):

    if "hello" in command:
        speak("Hello Siddhartha")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open chrome" in command:
        speak("Opening Chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif "news" in command:
        get_news()

    elif "open whatsapp" in command:
        speak("Opening WhatsApp")

        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open("https://web.whatsapp.com")

    elif "exit" in command:
        speak("Goodbye Siddhartha")
        return False

    else:
        speak("I don't know that command yet")

    return True


speak("Jarvis activated")

running = True
while running:
    command = listen()
    if command:
        running = process_command(command)
