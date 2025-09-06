from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Создание инлайн-клавиатуры для отчета
report_sheet = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Ссылка на таблицу',  # Текст кнопки
            url='https://docs.google.com/spreadsheets/d/1JKzWgEa9ddd-rhJyrgfoWO2HY9rjbmf0FCOr7QHE--Y/edit?usp=sharing'
            # URL на Google Sheets
        ),
    ],
], resize_keyboard=True)  # Параметр resize_keyboard не применяется к инлайн-клавиатурам, можно удалить
