from aiogram.types import Message
from subjects.history.data_history import ru_historical_events


async def get_historical_event(year: int):
    # Получаем событие по году
    event = ru_historical_events.get(year)

    if event:
        return f"Историческое событие в {year} году: {event}"
    else:
        return f"Нет исторических событий в {year} году."


# Пример использования функции
async def handle_year_request(message: Message):
    user_input = message.text
    try:
        year = int(user_input)
        response = await get_historical_event(year)
        await message.answer(response)
    except ValueError:
        await message.answer("Неверный формат года. Пожалуйста, введите год в формате YYYY.")
