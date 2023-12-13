import telebot
from telebot import types

token="6755112066:AAFrLEdlmoiGC1ZmeMjKAQwzQATJ0qtkB5k"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Как тебя зовут?", "/help", "/lobby")
    bot.send_message(message.chat.id,'Здравтсвуйте! Я ваш персональный помощник в МТУСИ! Чем могу быть полезен?', reply_markup=keyboard)

@bot.message_handler(commands=['lobby'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/start", "/help", "ВУЗ", "Как тебя зовут?", "Пока")
    bot.send_message(message.chat.id,'Выбирите нужную Вам функцию', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,'Давайте дружить! Могу Вам указать нужный путь, нажмите на кнопку "Lobby" и я Вас перенаправлю к строке команд')

@bot.message_handler(content_types={'text'})
def manipulator(message):
    if message.text == 'Как тебя зовут?':
        bot.send_message(message.chat.id, 'Можете звать меня Григорий')
    elif message.text == 'ВУЗ':
        bot.send_message(message.chat.id, 'Перенаправляю Вас на сайт МТУСИ https://mtuci.ru/')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'До свидания!')
    elif message.text == 'Григорий':
        bot.send_message(message.chat.id, 'Да-да, я')
    elif message.text == 'Ты кто?':
        bot.send_message(message.chat.id, 'Я Ваш персональный помощник')

bot.infinity_polling()
