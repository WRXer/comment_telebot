import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from dotenv import load_dotenv


load_dotenv()


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = os.getenv('token')

# Замените target_user_id на идентификатор целевого пользователя
target_user_id = 527186007  # Замените на фактический идентификатор пользователя

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет 🤍\nЯ телебот для сбора обратной связи. Анонимно передам админу ваши буквы 🫡\n\nНапишите, если:\n• вы нашли скидку и желаете поделиться находкой\n• хотите оставить отзыв на банку\n• есть идея по улучшению канала')


@dp.message(F.photo)
async def send_photo_echo(message: Message):
    username = message.from_user.first_name
    reply_text = f"Ты супер, {username} 😼 Спасибо за ОС:)"
    await bot.send_photo(target_user_id, photo=message.photo[-1].file_id)
    await bot.send_message(message.chat.id, reply_text)  # Отправка ответа анониму


@dp.message()
async def send_echo(message: Message):
    # Отправляем анонимное сообщение вам с содержанием оригинального сообщения
    username = message.from_user.first_name
    reply_text = f"Ты супер, {username} 😼 Спасибо за ОС:)"
    await bot.send_message(target_user_id, text=f'{message.text}')
    await bot.send_message(message.chat.id, reply_text)  # Отправка ответа анониму

@dp.message(F.sticker)
async def echo_sticker(message: Message):
    username = message.from_user.first_name
    reply_text = f"Ты супер, {username} 😼 Спасибо за ОС:)"
    await bot.send_sticker(target_user_id, message.sticker.file_id)
    await bot.send_message(message.chat.id, reply_text)  # Отправка ответа анониму


@dp.message(F.animation)
async def echo_animation(message: Message):
    # Отправляем анонимное сообщение вам с указанием отправленного GIF-файла
    username = message.from_user.first_name
    reply_text = f"Ты супер, {username} 😼 Спасибо за ОС:)"
    await bot.send_animation(target_user_id, message.animation.file_id)
    await bot.send_message(message.chat.id, reply_text)  # Отправка ответа анониму


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)
