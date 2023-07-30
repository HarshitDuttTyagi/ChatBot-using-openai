import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import openai
import random
from config import apikey
chatStr = ""
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harshit {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside of a try catch block
    speaker.speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response For Prompt: {prompt} \n************************************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this inside of a try catch block
    # print(response["Choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 4
        audio = r.listen(source, 0, 7)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('Pycharm')
    speaker.speak("Hello, I am Jarvis A.I.")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
               speaker.speak(f"Opening {site[0]} sir....")
               webbrowser.open(site[1])
        if "open music" in query:
            speaker.speak("Playing th music Sir")
            musicPath = r"C:\Users\Acer\Downloads\downfall-21371.mp3"
            os.startfile(musicPath)

        elif "the time" in query:
            musicPath = r"C:\Users\Acer\Downloads\downfall-21371.mp3"
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.speak(f"Sir the time is {strfTime}")

        elif "open teams" in query:
            speaker.speak("Opening teams Sir")
            os.startfile(r"C:\Users\Acer\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams (work or school).lnk")

        elif "Using artificial intelligence".lower() in query:
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query:
            speaker.speak("Goodbye Sir")
            exit()

        elif "reset chat".lower() in query:
            chatStr = ""
            speaker.speak("Chat Reseted")

        else:
            print("Chatting...")
            chat(query)

