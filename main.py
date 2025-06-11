# main.py

import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import pygame
from gtts import gTTS
import requests
import musicLibrary
from dotenv import load_dotenv
import google.generativeai as genai

engine = pyttsx3.init(driverName='espeak')

load_dotenv()
NEWS_API = os.getenv("NEWS_API")
GEMINI_API = os.getenv("GEMINI_API")

if GEMINI_API:
    genai.configure(api_key=GEMINI_API)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    print("Gemini API key is missing.")
    model = None


def speak_old(audio):
    engine.say(audio)
    engine.runAndWait()

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("audio.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("audio.mp3")


def aiprocess(command):
    if not model:
        speak("AI is not available because the API key is missing.")
        return

    try:
        prompt = {
            "You are a smart AI assistant named Jarvis. Always reply in a short and simple manner, "
            "within 1-2 sentences.\n"
            f"User: {command}\nAI:"
        }

        response = model.generate_content(prompt)
        reply = response.text.strip()
        short_reply = ". ".join(reply.split(". ")[:2])
        print("Response:", short_reply)
        speak(short_reply)
    except Exception as e:
        print("Error with Gemini API:", e)
        speak("Sorry, I couldn't process that with AI.")


def processCommand(command):
    command = command.lower()
    print("command:", command)

    if "google" in command:
        webbrowser.open("https://www.google.com")
        speak("opening google")

    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("opening youtube")

    elif "instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("opening instagram")

    elif "facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("opening facebook")

    elif "github" in command:
        webbrowser.open("https://www.github.com")
        speak("opening github")

    elif "linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        speak("opening linkedin")

    elif "search" in command:
        query = command.split("search ")[1]
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"searching for {query}")

    elif command.startswith("play"):
        song = command.split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak("Song not found in library")

    elif "news" in command:
        if not NEWS_API:
            speak("News API key is missing")
            print("ERROR: NEWS_API is not set.")
            return

        try:
            url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API}"
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                for article in articles[:5]:
                    title = article.get("title")
                    if title:
                        speak(title)
                        print(title)
            else:
                speak("Failed to fetch news")
                print(f"Error: Status Code {r.status_code} - {r.text}")
        except Exception as e:
            speak("Error occurred while fetching news")
            print("Exception in news request:", e)

    else:
        aiprocess(command)


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone(device_index=12) as source:
                print("listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=5)

            print("Recognizing...")
            key = r.recognize_google(audio)
            print("you said:", key)

            if key.lower() == "jarvis":
                with sr.Microphone(device_index=12) as source:
                    speak("Ya...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=15)
                    command = r.recognize_google(audio)
                    print("you said:", command)
                    processCommand(command)
        except sr.UnknownValueError:
            print("could not understand audio")
        except Exception as e:
            print("could not request results from google; {0}".format(e))
