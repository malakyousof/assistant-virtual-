import tkinter as tk
from  main import Assistant
import speech_recognition as sr

class GUIAssistant:
    def __init__(self, assistant):
        self.assistant = assistant
        self.window = tk.Tk()
        self.window.title("Button Example")

        self.button = tk.Button(self.window, text="Click for Help", command=self.on_button_click)
        self.button.pack()

    def run(self):
        self.window.mainloop()

    def on_button_click(self):
        with sr.Microphone() as source:
            self.assistant.speak("How can I assist you?")
            audio = self.assistant.recognizer.listen(source)

        try:
            request = self.assistant.recognizer.recognize_google(audio)
            print("Request:", request)  # Debugging statement
            if "time" in request:
                self.assistant.tell_time()
            elif "open" in request:
                application_name = request.replace("open", "").strip()
                self.assistant.open_application(application_name)
            else:

                self.assistant.speak("Sorry, I could not understand your request.")
        except sr.UnknownValueError:
            print("UnknownValueError occurred.")  # Debugging statement
            self.assistant.speak("Sorry, I could not understand what you said.")

if __name__ == "__main__":
    assistant = Assistant()
    gui = GUIAssistant(assistant)
    gui.run()
