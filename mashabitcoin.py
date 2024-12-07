import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Вставте свій токен
TOKEN = "7147524855:AAF0twVgo6abbD7OZeKqYFNzDt7bcNmlbn4"
bot = telebot.TeleBot(TOKEN)

# Словник для збереження кліків користувачів
user_clicks = {}

# Команда старт
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    user_clicks[user_id] = 0  # Ініціалізація лічильника для користувача
    
    # Створення кнопок
    markup = InlineKeyboardMarkup()
    button_click = InlineKeyboardButton("Грабити у Маши!", callback_data="click")
    button_balance = InlineKeyboardButton("Награблене :", callback_data="balance")
    button_withdraw = InlineKeyboardButton("Вивести біток :", callback_data="withdraw")
    
    # Додаємо кнопки до інтерфейсу
    markup.add(button_click)
    markup.add(button_balance)
    markup.add(button_withdraw)
    
    bot.send_message(user_id, "Чо делаєм броу :", reply_markup=markup)

# Обробка натискання кнопки "Клік!"
@bot.callback_query_handler(func=lambda call: call.data == "click")
def handle_click(call):
    user_id = call.message.chat.id
    user_clicks[user_id] += 1  # Додаємо кліки
    
    # Відповідь у спливаючому вікні
    bot.answer_callback_query(call.id, f"Кількість біткоінів : {user_clicks[user_id]}")

# Обробка натискання кнопки "Баланс"
@bot.callback_query_handler(func=lambda call: call.data == "balance")
def handle_balance(call):
    user_id = call.message.chat.id
    balance = user_clicks.get(user_id, 0)
    
    bot.answer_callback_query(call.id)
    bot.send_message(user_id, f"Ви вкрали: {balance} біткоінів")

# Обробка натискання кнопки "Вивести біток"
@bot.callback_query_handler(func=lambda call: call.data == "withdraw")
def handle_withdraw(call):
    user_id = call.message.chat.id
    
    bot.answer_callback_query(call.id)
    bot.send_message(user_id, "Щоб вивести біткойн, скиньте дані від картки !")

# Запуск бота
bot.infinity_polling()
