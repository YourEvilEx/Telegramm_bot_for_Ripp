import telebot
import const

bot = telebot.TeleBot(const.token)
print(bot.get_me())

command_flag = False
flag_to_const = False
flag_1 = 0
flag_2 = 0
flag_3 = 0


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


def log_answer(message, answer, question, true_answer):
    from datetime import datetime
    print('\n=================================')
    print(datetime.now())
    print('Сообщение от {0} {1}. (id = {2}) \nОтвет пользователя = {3}'.format(message.from_user.first_name,
                                                                               message.from_user.last_name,
                                                                               str(message.from_user.id),
                                                                               message.text))
    print('Вопрос = ', question)
    print('Правильный ответ = ', true_answer)
    print('Ответ бота = ', answer)


def log(message, answer):
    from datetime import datetime
    print('\n=================================')
    print(datetime.now())
    print('Сообщение от {0} {1}. (id = {2}) \nТекст сообщения = {3}'.format(message.from_user.first_name,
                                                                            message.from_user.last_name,
                                                                            str(message.from_user.id),
                                                                            message.text))
    print('Ответ = ', answer)


@bot.message_handler(commands=['start'])
def repeat_start(message_st):
    global flag_to_const
    global command_flag
    global flag_1
    global flag_2
    global flag_3
    answer = 'Привет, я простой бот который умеет только одно, авторизировать пользователей. ' \
             'Пожалуйста пройди авторизацию.'
    bot.send_message(message_st.chat.id, answer)
    log(message_st, answer)
    flag_to_const = False
    command_flag = False
    flag_1 = 0
    flag_2 = 0
    flag_3 = 0


@bot.message_handler(commands=['help'])
def repeat_help(message_hl):
    answer = 'Отправь команду /auth для авторизации и мы продолжим работу.'
    bot.send_message(message_hl.chat.id, answer)
    log(message_hl, answer)


@bot.message_handler(commands=['auth'])
def repeat_auth(message_au):
    global flag_to_const
    global command_flag
    global flag_1
    global flag_2
    global flag_3
    command_flag = False
    flag_to_const = False

    if const.first_name == message_au.from_user.first_name and const.last_name == message_au.from_user.last_name:
        bot.send_message(message_au.chat.id, 'Вижу доступ у тебя есть, но на всякий случай парочка '
                                             'контрольных вопросов. Для продолжения отправь \'+\'')
        log_auth(message_au, 'Вижу доступ у тебя есть, но на всякий случай ответь на пару контрольных вопросов.'
                             'Для продолжения отправь \'+\'')
        flag_to_const = True
        flag_1 = 2
    else:
        bot.send_message(message_au.chat.id,  const.ans_no_flag)
        log_auth(message_au, const.ans_no_flag)


@bot.message_handler(commands=['flag'])
def repeat_start(message):
        global command_flag

        if command_flag:
            bot.send_message(message.chat.id, const.ans_flag)
            log(message, const.ans_flag)
        else:
            bot.send_message(message.chat.id, 'Извините, у вас нет доступа к данной команде')
            log(message, 'Извините, у вас нет доступа к данной команде')


@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    global flag_to_const
    global flag_1
    global flag_2
    global flag_3
    global command_flag

    if flag_to_const and flag_1 == 2 and message.text == '+':
        bot.send_message(message.chat.id, 'Дата твоего рождения <дд.мм.гггг>?')
        log(message, 'Дата твоего рождения <дд.мм.гггг>?')
        flag_1 = 1
        flag_2 = 0
        flag_3 = 0

    elif flag_to_const and flag_1 == 1 and message.text.lower() == const.date_of_birth:
        bot.send_message(message.chat.id, 'Все верно, едем дальше.')
        log_answer(message, 'Все верно, едем дальше.', 'Дата твоего рождения <дд.мм.гггг>?', const.date_of_birth)
        flag_2 = 2
        flag_1 = 0
        flag_3 = 0

    elif flag_to_const and flag_1 == 1 and message.text.lower() != const.date_of_birth:
        bot.send_message(message.chat.id, 'Неа')
        log_answer(message, message.text, 'Дата твоего рождения <дд.мм.гггг>?', const.date_of_birth)

    if flag_to_const and flag_2 == 2:
        bot.send_message(message.chat.id, 'Твоя любимая песня <группа - песня>?')
        log(message, 'Твоя любимая песня <группа песня>?')
        flag_2 = 1

    elif flag_to_const and flag_2 == 1 and message.text.lower() == const.true_song:
        bot.send_message(message.chat.id, 'Все верно, едем дальше.')
        log_answer(message, 'Все верно, едем дальше.', 'Твоя любимая песня <группа - песня>?', const.true_song)
        flag_3 = 2
        flag_1 = 0
        flag_2 = 0

    elif flag_to_const and flag_2 == 1 and message.text.lower() != const.true_song:
        bot.send_message(message.chat.id, 'Неа')
        log_answer(message, 'Неа', 'Твоя любимая песня <группа - песня>?', const.true_song)

    if flag_to_const and flag_3 == 2:
        bot.send_message(message.chat.id, 'Дата регистрации в ВК <дд.мм.гггг>?')
        log(message, 'Дата регистрации в ВК <дд.мм.гггг>?')
        flag_3 = 1

    elif flag_to_const and flag_3 == 1 and message.text.lower() == const.date_of_registration:
        bot.send_message(message.chat.id, 'Спасибо что прошли аутентификацию, теперь вы '
                                          'можете воспользоваться командой /flag')
        log_answer(message, 'Спасибо, что прошли аутентификацию, теперь вы можете воспользоваться командой /flag',
                   'Дата регистрации в ВК <дд.мм.гггг>?', const.date_of_registration)
        command_flag = True

    elif flag_to_const and flag_3 == 1 and message.text.lower() != const.date_of_registration:
        bot.send_message(message.chat.id, 'Неа')
        log_answer(message, 'Неа', 'Дата регистрации в ВК <дд.мм.гггг>?', const.date_of_registration)

    elif not flag_to_const:
        answer = 'Я бы с удовольствием с тобой пообщался, но не запрограммирован на это.\n' \
             'Пожалуйста, пройди авторизацию, не делай мне больно.'
        bot.send_message(message.chat.id, answer)
        log(message, answer)


bot.polling(none_stop=True, interval=0)
