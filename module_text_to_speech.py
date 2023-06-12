import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    current_rate = engine.getProperty('rate')
    engine.setProperty('rate', current_rate * 1.08)
    engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

