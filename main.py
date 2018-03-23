import telebot
import const

bot = telebot.TeleBot(const.token)
print(bot.get_me())


def log(message, answer):
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


@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    if const.first_name == message.from_user.first_name and const.last_name == message.from_user.last_name:
        bot.send_message(message.chat.id, const.ans_flag)
        log(message,  const.ans_flag)
    else:
        bot.send_message(message.chat.id,  const.ans_noflag)
        log(message,  const.ans_noflag)


bot.polling(none_stop=True, interval=0)
