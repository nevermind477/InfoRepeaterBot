import json
import os


def load_words(file_path):
    """Загружает слова из JSON файла."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_words_by_class_and_letter(class_number, letter=None, file_path='subjects/russian/data_russian.json'):
    """Возвращает слова для указанного класса и, при необходимости, фильтрует по первой букве."""
    words_data = load_words(file_path)

    # Проверяем, существует ли класс
    if class_number in words_data:
        words = words_data[class_number]

        # Если указана буква, фильтруем слова
        if letter:
            words = [word for word in words if word.lower().startswith(letter.lower())]

        return words
    else:
        raise ValueError(f"Класс {class_number} не найден.")


# Пример использования
async def vocabulary_words(class_number, letter):
    try:
        words = get_words_by_class_and_letter(class_number, letter)
        return f"Слова для {class_number} класса с буквы '{letter}': {', '.join(words)}"
    except (FileNotFoundError, ValueError) as e:
        return str(e)
