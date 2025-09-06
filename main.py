import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router as main_router  # Основной маршрутизатор
from subjects.informatics.handler_informatic import router as informatics_router
from subjects.history.handler_history import router as history_router
from subjects.chemistry.handler_chemistry import router as chemistry_router
from subjects.russian.handler_russian import router as russian_router
from subjects.physics.handler_physics import router as physic_router
from report.report_handler import router as report_router

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    # Добавляем оба маршрутизатора в диспетчер
    dp.include_router(main_router)
    dp.include_router(informatics_router)
    dp.include_router(report_router)
    dp.include_router(history_router)
    dp.include_router(chemistry_router)
    dp.include_router(russian_router)
    dp.include_router(physic_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
