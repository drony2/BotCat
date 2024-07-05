import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(chat_id=message.chat.id, text="Привет, я твой бот! \nХочешь покажу котика?\nДа/Нет")
    print(message.text)


@bot.message_handler(commands=['video'])
def start(message):
    video = open('source/cotic.mp4', 'rb')
    bot.send_video(chat_id=message.chat.id, video=video)
    bot.send_message(message.chat.id, 'А теперь голос котиков?\nЕсли да нажми на /audio')
    print(message.text)


@bot.message_handler(commands=['audio'])
def start(message):
    audio = open('source/mur.mp3', 'rb')
    bot.send_voice(chat_id=message.chat.id, voice=audio)
    print(message.text)


@bot.message_handler(content_types=['text'])
def cat_text(message):
    chat_id = message.chat.id
    if message.text == "Да" or message.text == "да" or message.text == "lf":
        bot.register_next_step_handler(bot.send_message(chat_id, 'Введи сколько(числом не более 4): '), step_Set_Price)
        print(message.text)

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
        case _:
            bot.send_message(chat_id, "Нет такой функции")
            print("Херню просят")


def step_Set_Price(message):
    cid = message.chat.id
    user_text = message.text

    for i in range(int(user_text)):
        phot = open(f"source/Cat{i + 1}.jpg", "rb")
        bot.send_photo(chat_id=cid, photo=phot)
        print("Кинул фото")

    bot.send_message(chat_id=cid, text="А хочешь видео?\nТогда нажми на /video")


bot.polling(none_stop=True)
