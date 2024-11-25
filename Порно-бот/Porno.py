import telebot

bot = telebot.TeleBot('7745181783:AAEcZpw254NbgdtE7FF6luGs2iwMqjPj6UY')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Давай начнем познавать порно мир наших животных')
    bot.send_message(message.chat.id, 'Выбери команду!')
    

@bot.message_handler(commands=['pigeon'])
def pigeon(message):
    video = 'спаривание голубей.mp4'
    file = open('./'+ video, 'rb')
    bot.send_video(message.chat.id, file)


@bot.message_handler(commands=['rabbit'])
def rabbit(message):
    video = 'Спаривание кроликов.mp4'
    file = open('./'+ video, 'rb')
    bot.send_video(message.chat.id, file)

@bot.message_handler(commands=['dog'])
def dog(message):
    video = 'Полторы минуты из жизни бездомных собак.mp4'
    file = open('./'+ video, 'rb')
    bot.send_video(message.chat.id, file)


print('Телеграм бот запущен')
bot.polling(none_stop=True)