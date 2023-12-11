import logging
import telebot
import os, logging
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('token')
bot = telebot.TeleBot(token)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@bot.message_handler(commands=['start'])
def start(message):
    """
    Обработчик команды /start
    :param message:
    :return:
    """
    bot.reply_to(message, f"Привет! Я бот для приема сообщений администратору канала 'глаголю на скидочном'.🤖\nГотов передать сообщение анонимно! 😊")

@bot.message_handler(func=lambda message: True)
def echo(message):
    """
    Обработчик входящих сообщений
    :param message:
    :return:
    """
    user_id = 527186007  #437513483  # Замените на ID пользователя, которому нужно переслать сообщение
    #user_id = 437513483
    username = message.from_user.first_name  # Имя пользователя, которому отправляем благодарность
    if message.text:

        # Если есть текстовое сообщение, отправляем его текст
        bot.send_message(user_id, message.text)
        reply_text = f"Спасибо, {username}! Я очень вам благодарен! 😊"
        bot.reply_to(message, reply_text)
        logging.info(f"Текстовое сообщение от {username}: {message.text}")


def main():
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

