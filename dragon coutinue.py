import speech_recognition as sr
import pyttsx3
import tkinter as tk

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speech_to_text():
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize.listen(source)
            print("Listening...")
            speak(text) # Read the recognized text
        except sr.UnknownValueError:
            print(f"Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request result; {e}")
        except sr.RequestError as e:
            print(f"Could not request result; {e}")



# Create a simple GUI 
root = tk.Tk()
root.title("Speech Recognition App")

recognize_button = tk.Button(root, text="Speak Now", command=recognize_speech)
recognize_button.pack(pady=20)

root.mainloop()



import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

# Initialize text-to-speech 
engine = pyttsx3.init()

# Load common phrases
common_phrases = [
 "Hello, how are you?",
 "I need help.",
 "Can you repeat that?",
   "Thank you.",
   "Goodbye."
   "Yes"
   "No" 
    ]

# Load or create a frequent phrases 
def load_frequent_phrases():
    if os.path.exists("frequent_phrases.json"):
        with open("frequent_phrases.json", "r") as file:
            return json.load(file)
        return []

def save_frequent_phrases(frequent_phrases):
    with open("frequent_phrases.json", "w") as file:
        json.dump(frequent_phrases, file)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("Listening...")
            speak(text) # Read the recognized text
        except sr.UnknownValueError:
            print(f"Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request result; {e}")

def update_frequent_phrase(phrase):
    if phrase not in frequent_phrases:
        frequent_phrases.append(phrase)
        save_frequent_phrases(frequent_phrases)

def get_frequent_phrase():
    common_phrases_string = "\n".join(common_phrases)
    messagebox.showinfo("Common Phrases", common_phrases_string)

def predict_next_phrase():
    user_input = simpledialog.askstring("Predict Next Phrase", "What's the current phrase?")
    if user_input:
        predictions = [phrase for phrase in frequent_phrases if user_input.lower in phrase.lower()] 
        if predictions:
            predictions_string = "\n".join(predictions)
            messagebox.showinfo("Predicted Phrases", predictions_string)
            else:
            messagebox.showinfo("Predicted Phrases", "No predictions found.")

# Create a simple GUI
root = tk.Tk()
root.title("Speech Recognition App")

recognize_button = tk.Button(root, text="Speak Now", command=recognize_speech)
recognize_button.pack(pady=20)

common_phrases_button = tk.Button(root, text="Common Phrases", command=get_frequent_phrase)
common_phrases_button.pack(pady=20)

predict_button = tk.Button(root, text="Predict Next Phrase", command=predict_next_phrase)
predict_button.pack(pady=20)

root.mainloop()