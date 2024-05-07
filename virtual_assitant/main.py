import tkinter as tk
import subprocess

import datetime
import speech_recognition as sr
import pyttsx3
import os
from AppOpener import open, close
class Assistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def tell_time(self):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M")
        self.speak("The time is:")
        self.speak(formatted_time)

    import subprocess

    def open_application(self, application_name):
        if application_name == "lightworks":
            app_path = r"C:\Users\Public\Desktop\lightworks 2023.2.lnk"

        if application_name == "edge":
            app_path = r"C:\Users\dell\Desktop\edge 2023.2.lnk"
            try:
                subprocess.run(app_path, shell=True)
            except Exception as e:
                print("Error opening application:", e)
        else:
            print("Application not supported or not found.")
