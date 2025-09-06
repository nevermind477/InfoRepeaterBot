from mendeleev import element
from aiogram.types import Message


async def display_element_info(symbol: str, message: Message):
    try:
        elem = element(symbol)
        await message.answer(f"Элемент: {elem.name}")
        await message.answer(f"Символ: {elem.symbol}")
        await message.answer(f"Атомный номер: {elem.atomic_number}")
        await message.answer(f"Масса: {elem.atomic_weight}")
        await message.answer(f"Состояние при нормальных условиях: {elem.state}")
        await message.answer(f"Классификация: {elem.category}")
    except Exception as e:
        print()
