from module_speech_recognition import recognize_speech
from module_text_to_speech import speak
from module_search_in_wiki import search_in_wikipedia

# Рассказ о себе
intro_text = "Привет! Я виртуальный ассистент 2077 ФЛАЙ. Я готов прослушать твои команды."
speak(intro_text)

# Поиск вики
def process_command(text):
    if "найти в википедии" in text.lower():
        query = text.lower().replace("найти в википедии", "").strip()
        search_result = search_in_wikipedia(query)
        return search_result
    else:
        return text

# Основной цикл программы
while True:
    # Слушаем речь пользователя
    text = recognize_speech()

    if text:
        # Обработка команды пользователя и генерация ответа
        response = process_command(text)

        # Ответ бота в голосовом формате
        speak(response)