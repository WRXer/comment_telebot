from auth_token import token

import telebot
import emoji

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    """
    Обработчик команды /start
    :param message:
    :return:
    """
    bot.reply_to(message, f"Привет! Я бот для приема сообщений администратору канала 'глаголю на скидочном'.🤖\nВ следующем сообщении можете просто вставить ссылку! 😊")

@bot.message_handler(func=lambda message: True)
def echo(message):
    """
    Обработчик входящих сообщений
    :param message:
    :return:
    """
    user_id = 527186007  #437513483  # Замените на ID пользователя, которому нужно переслать сообщение
    #user_id = 437513483
    bot.send_message(user_id, message.text)


def main():
    bot.polling()