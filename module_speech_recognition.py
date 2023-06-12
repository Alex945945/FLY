import speech_recognition as sr
import sys
from module_text_to_speech import speak

# Основная функция
def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        audio = r.listen(source, timeout=2)

    try:
        print("Распознавание речи...")
        text = r.recognize_google(audio, language="ru-RU")
        print("Вы сказали: " + text.lower())

        if "пока" in text.lower():
            speak("Пока!")
            sys.exit()  # Завершение программы
    
        if "как дела" in text.lower():  # Добавляем проверку наличия фразы "как дела" в тексте
            speak("Ахуяяяяна Браааааатан")
            return
        
        else:
            return text

    except sr.UnknownValueError:
        print("Речь не распознана")
        return None

    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи: {0}".format(e))
        return None
