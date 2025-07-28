import os
import telebot
import boobs2D
import dick2D
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set bot options
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.send_message(message.chat.id,
                     'Привет! Я могу сгенерировать тебе сиськи!')

# Transcribe message into text manually
@bot.message_handler(commands=['boobs'])
def send_message(message):
    bot.send_message(message.chat.id, "Сиськи!")
    boobs2D.save_breast()
    # Отправить изображение
    with open(r'.\boobs.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    
# Transcribe message into text manually
@bot.message_handler(commands=['dick'])
def send_message(message):
    bot.send_message(message.chat.id, "Писюн!")
    dick2D.save_dick()
    # Отправить изображение
    with open(r'.\dick.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

if __name__ == '__main__':
    bot.infinity_polling()