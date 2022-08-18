# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Importing Libraries;

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import cv2
import os
import time
import subprocess
import json
import requests
import webbrowser
import wolframalpha

# Welcome message for our AI:

print("Loading your AI Assistant: {name}")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voice[0].id')

# function =======

def speak(text):
    engine.say(text)
    engine.setProperty("rate", 175)
    engine.runAndWait()

# Wishing Function:

def wishMe():
    hour = datetime.datetime.now().hour
    
    if hour>=0 and hour<12:
        speak("Hello Akshit, Wish you a very Good Morning")
        print("Hello Akshit, Wish you a very Good Morning")
        
    elif hour >=12 and hour<18:
        speak("Hello Akshit, Good Afternoon")
        print("Hello Akshit, Good Afternoon")
    
    else:
        speak("Hello Akshit, Good Evening")
        print("Hello Akshit, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        
        try:
            statement = r.recognize_google(audio, language = 'en-in')
            print(f"user said: {statement}\n")
            
        except Exception as e:
            speak("Pardon me, Please say that again, Sir")
            return "none"
        
        return statement

speak("Loading your AI personal Assistant Akki")

wishMe()

if __name__ == '__main__':
    
    while True:
        speak ("Tell me, How can I help you ?")
        statement = takeCommand().lower()
        
        if statement == 0:
            continue
        
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("{name} is shutting down, Good Bye")
            print("{name} is shutting down, Good Bye")
            break
        
        
        if 'wikipedia' in statement:
            speak("Searching Wikipedia...")
            statement = statement.replace('wikipedia', '')
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube has been opened for you")
            time.sleep(5)
        
        elif 'open google' in statement:
            webbrowser.open_new_tab("http://www.google.com")
            speak("Google is now opened")
            time.sleep(5)
            
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("http://www.gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        
        elif "weather" in statement:
            api_key = '3700181d96dab29846781e0312aa8b79'
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("Tell me the place...")
            city_name = takeCommand()
            complete_url = base_url + 'apiid='+api_key+'&q='+city_name
            response = requests.get(complete_url)
            x = response.json()
            print(x)
            
            if x["cod"] != "404":
                y = x["main"]
                current_temp = y["temp"]
                current_hum = y["humidity"]
                z = x["weather"]
                
                weather_desc = z[0]["description"]
                speak("Temperature in Kelvin unit is "+
                      str(current_temp) +
                      "\n humidity in percentage is " +
                      str(current_hum) +
                      "\n description " + 
                      str(weather_desc))
                print("Temperature in Kelvin unit is "+
                      str(current_temp) +
                      "\n humidity in percentage is " +
                      str(current_hum) +
                      "\n description " + 
                      str(weather_desc))
            else:
                speak("Sorry, This place is not found")
        
        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Akki version 1 point O, your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
        
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Akshit Negi")
            print("I was built by Akshit Negi")
        
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is Stack Overflow")
        
        #elif "camera" in statement or "take a photo" in statement:
            #ec.capture(0,"robo camera","img.jpg")
        
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            
        elif 'ask' in statement:
            speak("I can answer to computational and geographical questions and what question do you want to ask now")
            ques = takeCommand()
            app_id = 'UUHKGT-6X882YWUXV'
            client = wolframalpha.Client(app_id)
            res = client.query(ques)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])


time.sleep(3)






















