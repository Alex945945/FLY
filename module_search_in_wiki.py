import wikipedia

def search_in_wikipedia(query):
    wikipedia.set_lang("ru")  # Устанавливаем язык поиска на русский
    try:
        page = wikipedia.page(query)
        summary = page.summary
        return summary
    except wikipedia.DisambiguationError as e:
        options = e.options[:5]  # Ограничиваем количество вариантов до 5
        return "Уточните ваш запрос, возможно вы имели в виду одну из следующих статей:\n" + "\n".join(options)
    except wikipedia.PageError:
        return "Информация по вашему запросу не найдена."