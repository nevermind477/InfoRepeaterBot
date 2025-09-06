from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главная клавиатура с основными опциями
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Выбрать предмет 📚')  # Кнопка для выбора предмета
        ],
        [
            KeyboardButton(text='Сообщить об ошибке/Предложить идею 💬'),  # Кнопка для обратной связи
            KeyboardButton(text='О боте ⁉️')  # Кнопка для получения информации о боте
        ]
    ],
    resize_keyboard=True  # Автоматическая подгонка размера клавиатуры
)

# Клавиатура для выбора предметов
subject_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Химия 🧪'),  # Кнопка для химии
            KeyboardButton(text='Информатика 👨‍💻')  # Кнопка для информатики
        ],
        [
            KeyboardButton(text='Русский язык 📝'),  # Кнопка для русского языка
            KeyboardButton(text='История 📆')  # Кнопка для истории
        ],
        [
            KeyboardButton(text='В главное меню'),  # Кнопка для возврата в главное меню
        ],
    ],
    resize_keyboard=True,  # Автоматическая подгонка размера клавиатуры
    input_field_placeholder='Выберите пункт меню'  # Подсказка для ввода
)
