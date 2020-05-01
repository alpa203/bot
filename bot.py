token = "1010234664:AAFN8Ht2If1T_8gDkIQjN2rvyaDLVrEZiz0"
owner = "349075562"

import telebot
from time import sleep
import logging
import datetime

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot = telebot.AsyncTeleBot(token=token, threaded=False, skip_pending=False)


@bot.message_handler(commands=["ping"])  # Создаем команду
def start(message):
    try:  # Заворачиваем все в try
        bot.send_message(message.chat.id, "<b>PONG!</b>", parse_mode="HTML")
        bot.forward_message(owner, message.chat.id, message.message_id)
    except:
        bot.send_message(owner,
                         'Что-то пошло не так!')  # анная система (оборачивание в try и except позволит продолжить выполнение кода, даже если будут ошибки)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет, ' + str(message.from_user.first_name) + '!\n' 'Присылай мне мемы или видео для @g_prog.')
    bot.forward_message(owner, message.chat.id, message.message_id)



def process_mind(message):
    if int(message.chat.id) == owner:
        try:
            text = 'Сообщение было отправлено пользователю ' + str(message.reply_to_message.forward_from.first_name)
            bot.forward_message(message.reply_to_message.forward_from.id, owner, message.message_id)
            bot.send_message(owner, text)
        except:
            bot.send_message(message.chat.id,
                             'Что-то пошло не так! Бот продолжил свою работу.' + ' Ошибка произошла в блоке кода:\n\n <code>def process_mind(message)</code>',
                             parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, 'Вы не являетесь администратором для выполнения этой команды!')

@bot.message_handler(commands=['id'])
def process_start(message):
    bot.send_message(message.chat.id, "Твой ID: " + str(message.from_user.id), parse_mode='HTML')
    bot.forward_message(owner, message.chat.id, message.message_id)


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, 'Этот бот создан как предложка канала @g_prog, можешь отправить мне смешную картинку или видео.')
    bot.send_message(owner, 'Привет, хозяин! ' + str(message.from_user.first_name) + ' использовал команду /help')
    bot.forward_message(owner, message.chat.id, message.message_id)


@bot.message_handler(content_types=["text"])
def messages(message):
    bot.forward_message(owner, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, str(message.from_user.first_name) + ',' + ' спасибо! :)')

@bot.message_handler(content_types=["photo"])
def photo(message):
    bot.send_photo(owner, message.photo[-1].file_id, message.caption)
    bot.send_message(message.chat.id, str(message.from_user.first_name) + ',' + ' спасибо! :)')

@bot.message_handler(content_types=["document"])
def document(message):
    bot.send_document(owner, message.document.file_id)
    bot.send_message(message.chat.id, str(message.from_user.first_name) + ',' + ' спасибо! :)')


if __name__ == '__main__':
    bot.polling(none_stop=True)



