import telebot
import const

bot = telebot.TeleBot(const.token)
print(bot.get_me())


def log_auth(message, answer):
    from datetime import datetime
    print('\n=================================')
    print(datetime.now())
    print('Сообщение от {0} {1}. (id = {2}) \nТекст сообщения = {3}'.format(message.from_user.first_name,
                                                                            message.from_user.last_name,
                                                                            str(message.from_user.id),
                                                                            message.text))
    print('Ответ = ', answer)
    print('FIRST_NAME = ', message.from_user.first_name)
    print('LAST_NAME = ',  message.from_user.last_name)


def log(message, answer):
    from datetime import datetime
    print('\n=================================')
    print(datetime.now())
    print('Сообщение от {0} {1}. (id = {2}) \nТекст сообщения = {3}'.format(message.from_user.first_name,
                                                                            message.from_user.last_name,
                                                                            str(message.from_user.id),
                                                                            message.text))
    print('Ответ = ', answer)


@bot.message_handler(command=['start'])
def repeat_start(message):
        answer = 'Привет, я простой бот который умеет только одно, авторизировать пользователей. ' \
                 'Пожалуйста пройди авторизацию.'
        bot.send_message(message.chat.id, answer)
        log(message, answer)


@bot.message_handler(command=['help'])
def repeat_help(message):
    answer = 'Отправь команду /auth для авторизации и мы продолжим работу.'
    bot.send_message(message.chat.id, answer)
    log(message, answer)


@bot.message_handler(command=['auth'])
def repeat_auth(message):
    if const.first_name == message.from_user.first_name and const.last_name == message.from_user.last_name:
        bot.send_message(message.chat.id, const.ans_flag)
        log(message, const.ans_flag)
    else:
        bot.send_message(message.chat.id,  const.ans_no_flag)
        log(message, const.ans_no_flag)


@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    answer = 'Я бы с удовольствием с тобой по общался, но не запрограммирован на это.\n' \
             'Пожалуйста пройди авторизацию, не делай мне больно.'
    bot.send_message(message.chat.id, answer)
    log(message, answer)


bot.polling(none_stop=True, interval=0)
