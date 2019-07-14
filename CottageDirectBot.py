import telebot

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Eligible commands: /start, /help and /info')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Eligible commands: start, help and info')


@bot.message_handler(commands=['info'])
def start_message(message):
    bot.send_message(message.chat.id, 'smth smth smth smth smth smth'
                                      'smth smth smth smth smth smth.')




bot.polling()
