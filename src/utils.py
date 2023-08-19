import os

import telebot


token = os.getenv('token')
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
    username = message.from_user.first_name  # Имя пользователя, которому отправляем благодарность
    if 'http' in message.text:
        bot.send_message(user_id, message.text)
        reply_text = f"Спасибо, {username}! Я очень вам благодарен! 😊"  # Отправка благодарности пользователю в ответ на его сообщение
        bot.reply_to(message, reply_text)
    else:
        reply_text = f"Извините, {username}, но здесь нет ссылки! 🥲"  # Отправка благодарности пользователю в ответ на его сообщение
        bot.reply_to(message, reply_text)

def main():
    bot.polling()