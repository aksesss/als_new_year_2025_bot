import telebot
from telebot import types
from src.config.config import TOKEN
import logging
from src.Joke import Joke

# Создаем объект бота с вашим токеном
bot = telebot.TeleBot(TOKEN)
logger = logging.getLogger(__name__)

# Список шуток
jokes = Joke()
# Хранение имени пользователя
user_name = {}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Как тебя зовут?")
    bot.register_next_step_handler(message, process_name)


def process_name(message):
    user_name[message.chat.id] = message.text  # Запоминаем имя пользователя
    bot.send_message(message.chat.id, f"Приятно познакомиться, {message.text}! Нажми на кнопку, чтобы получить шутку.")

    # Создаем клавиатуру с кнопкой "Получить шутку"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    joke_button = types.KeyboardButton("Получить шутку")
    markup.add(joke_button)

    bot.send_message(message.chat.id, "Выбери опцию:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Получить шутку")
def send_joke(message):
    logger.info(f'{message.chat.id} requested joke')
    print(f'{message.chat.id} requested joke')

    new_joke = jokes.get_joke()
    bot.send_message(message.chat.id, new_joke)

    # 669381946 - я
    # 1542156183 - саша


# Запускаем бота
bot.polling()
