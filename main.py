import telebot
import sound
import os
from dotenv import load_dotenv

load_dotenv()


token = os.getenv('API_TOKEN')


bot = telebot.TeleBot(token)


@bot.message_handler(commands='start')
def start_message(message):
    bot.send_message(message.chat.id, 'Привет✌️, напиши мне любой текст, а я его озвучу!')


@bot.message_handler(content_types='text')
def sound_message(message):
    sound.sound(message.text)
    audio = open(f'{message.text}.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()
    os.remove(f'./{message.text}.mp3')



bot.infinity_polling()