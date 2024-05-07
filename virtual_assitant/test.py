import tkinter as tk
import speech_recognition as sr
import datetime

class Assistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        print(text)  # For testing, replace with actual text-to-speech code
        # Add your text-to-speech code here

    def tell_time(self):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M")
        self.speak("The time is:")
        self.speak(formatted_time)

    def open_application(self, application_name):
        if application_name == "whatsapp":
            # Replace the print statement with appropriate code to open WhatsApp
            print("Opening WhatsApp...")

        elif application_name == "Edge":
            # Replace the print statement with appropriate code to open Edge
            print("Opening Microsoft Edge...")
        elif application_name == "chrome":
            # Replace the print statement with appropriate code to open Chrome
            print("Opening Google Chrome...")
        else:
            self.speak("Sorry, I don't know how to open that application.")

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
            if "time" in request:
                self.assistant.tell_time()
            elif "open" in request:
                words = request.split()
                app_name_index = words.index("open") + 1
                if app_name_index < len(words):
                    application_name = words[app_name_index]
                    self.assistant.open_application(application_name)
                else:
                    self.assistant.speak("Please specify an application to open.")
            else:
                self.assistant.speak("Sorry, I could not understand your request.")
        except sr.UnknownValueError:
            self.assistant.speak("Sorry, I could not understand what you said.")

if __name__ == "__main__":
    assistant = Assistant()
    gui = GUIAssistant(assistant)
    gui.run()
