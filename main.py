import re

import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button_cat_video = types.InlineKeyboardButton("Видео с котиками", callback_data='cat_video')
    markup.add(button_cat_video)
    button_cat_photo = types.InlineKeyboardButton("Фото котиков", callback_data='cat_photo')
    markup.add(button_cat_photo)
    button_cat_voice = types.InlineKeyboardButton("Мурлыканье", callback_data='cat_voice')
    markup.add(button_cat_voice)
    button_miu = types.InlineKeyboardButton("Миу", callback_data='cat_miu')
    markup.add(button_miu)
    button_help = types.InlineKeyboardButton("Help", callback_data='cat_help')
    markup.add(button_help)
    button_my_tg = types.InlineKeyboardButton("Тот кто создал бота", url="https://t.me/dornall", callback_data="my_tg")
    markup.add(button_my_tg)

    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! \nМеню)", reply_markup=markup)

    print(message.text)


@bot.callback_query_handler(func=lambda call: True)
def start_button_ck(call):
    if call.data == 'cat_miu':
        bot.send_message(chat_id=call.message.chat.id, text="Миу")
        print("Button_Miu")
    elif call.data == 'cat_photo':
        print(call.message.text)
        step_Set_Price(message=call.message)

        print("Button_photo")
    elif call.data == 'cat_voice':
        start_audio(call.message)
        print("Button_voice")
    elif call.data == 'cat_video':
        start_video(call.message)
        print("Button_video")
    elif call.data == 'my_tg':
        print("Butthon_my_tg")
    elif call.data == 'cat_help':
        bot.send_message(chat_id=call.message.chat.id, text="Все команды бота: \n1) /video \n2) /audio\n3) /photo")
        print("Butthon_cat_help")


@bot.message_handler(commands=['video'])
def start_video(message):
    video = open('source/cotic.mp4', 'rb')
    bot.send_video(chat_id=message.chat.id, video=video)
    print(message.text)


@bot.message_handler(commands=['audio'])
def start_audio(message):
    audio = open('source/mur.mp3', 'rb')
    bot.send_voice(chat_id=message.chat.id, voice=audio)
    print(message.text)


@bot.message_handler(content_types=['text', 'sticker'])
def sticket(message):
    chat_id = message.chat.id
    match message.text:
        case '🐈':
            bot.send_message(chat_id, 'Эта котя лижит ножку')
            print(message.text)
        case "🐱":
            bot.send_message(chat_id, 'Эта котя лижит ляпку')
            print(message.text)
        case "💥":
            bot.send_message(chat_id, 'Это бум')
            print(message.text)
        case "🍜":
            bot.send_message(chat_id, 'Это еда кись')
            print(message.text)
        case "❤️":
            bot.send_message(chat_id, 'I love you')
            print(message.text)
        case "\U0001F408":
            bot.send_message(chat_id, 'I love you')
            print(message.text)
        case _:
            if message.text == "/photo":
                cat_photo(message)
                return
            bot.send_message(chat_id, "Нет такой функции")
            print("Херню просят")


@bot.message_handler(commands=['photo'])
def cat_photo(message):
    chat_id = message.chat.id
    bot.register_next_step_handler(bot.send_message(chat_id, 'Введи сколько(числом не более 4): '), step_Set_Price)
    print(message.text)


def step_Set_Price(message):
    cid = message.chat.id
    user_text = message.text
    if not ("Меню" in user_text):
        for i in range(int(user_text)):
            phot = open(f"source/Cat{i + 1}.jpg", "rb")
            bot.send_photo(chat_id=cid, photo=phot)
            print("Кинул фото")
    else:
        for i in range(4):
            phot = open(f"source/Cat{i + 1}.jpg", "rb")
            bot.send_photo(chat_id=cid, photo=phot)
            print("Кинул фото")


bot.polling(none_stop=True)
