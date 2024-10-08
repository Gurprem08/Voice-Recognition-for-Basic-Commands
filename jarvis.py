import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import math,random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f'Good Morning .  Its {hour} AM')
    elif hour>=12 and hour<18:
        speak(f'Good Afternoon . Its {hour}PM')
    else:
        speak('Good Evening')
    speak(' I am Jarvis Sir . Please tell me how may i help you')            

def takeCommand():
    '''
    this is taking command
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        r.energy_threshold =500
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in') 
        print(f"User said : {query}\n")                     
    except Exception as e:
        #print(e)
        print("Say that again please")
        return("NONE")     
    return(query) 



if __name__ == "__main__":
    wishMe()
    if 1:
       query = takeCommand().lower()

       if 'wikipedia' in query:
           speak("Searching wikipedia....")
           query =  query.replace('wikipedia' , "")
           results = wikipedia.summary(query, sentences = 3)
           speak("According to wikipedia")
           speak(results)
        
       elif "open youtube" in query:
            webbrowser.open("youtube.com")
       elif "play music" in query:
            music_dir = 'D:\\MUSIC'
            songs = os.listdir(music_dir)    
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
       elif "the time" in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(strTime)
           speak(f"Sir , the time is {strTime}")
       elif "google" in query:
           webbrowser.open("google.com")
 