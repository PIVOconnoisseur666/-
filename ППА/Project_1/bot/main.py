import telebot

from auth_data import token, happy_birthday_type, holidays, new_year_type


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def send_text(message):
        bot.send_message(message.chat.id, "Кого поздравляем?")
        bot.register_next_step_handler(message, user_name)
    def user_name(message):
        global name
        name = message.text
        bot.register_next_step_handler(message, send_text_pick_holiday)
    @bot.message_handler(content_types=['text'])
    def send_text_pick_holiday(message):
        bot.send_message(message.chat.id, "Выберете праздник:  День рождения, Новый год, ")
        bot.register_next_step_handler(message, send_text_chose_holiday)
    def send_text_chose_holiday(message):
        if message.text.lower() == holidays[0]:
            try:
                bot.send_message(message.chat.id,"Выберете шаблон: Счастья здоровья, На ПСЖ не улететь, С прошедшим")
                if message.text.lower() == happy_birthday_type[0]:
                    bot.send_message(message.chat.id,f"Счастья здоровья тебе {name}!!!")
                    bot.send_message(message.chat.id, "Готово")
                elif message.text.lower() == happy_birthday_type[1]:
                    bot.send_message(message.chat.id, f"Ну давай на ПСЖ не улетай {name}")
                    bot.send_message(message.chat.id, "Готово")
                elif message.text.lower() == happy_birthday_type[2]:
                    bot.send_message(message.chat.id,f"Это самое, я заработался, забыл, поэтому с прошедшим тебя{name}")
                    bot.send_message(message.chat.id, "Готово")
            except Exception as ex:
                print(ex)
        elif message.text.lower() == holidays[1]:
            try:
                bot.send_message(message.chat.id,"Выберете шаблон: Минимум, Оригинально")
                if message.text.lower() == new_year_type[0]:
                    bot.send_message(message.chat.id, f"С нг,{name}")
                    bot.send_message(message.chat.id, "Готово")
                elif message.text.lower() == new_year_type[1]:
                    bot.send_message(message.chat.id, "Ребят, я хочу пожелать вам счастливого наступающего нового года. Сейчас много скопированных поздравлений, которые люди просто отправляют своим знакомым, даже не читая их. Это печально. Я бы хотел написать о том, чего я сильно желаю и что лежит глубоко в сердце. Наши друзья, самые близкие и самые удаленные, очень важны для нас, и эту дружбу нельзя выразить простым сообщением, скопированным у другого человека. Хочу сказать всем огромное спасибо. Вы лучшая хоккейная команда, с которой я когда-либо играл. Всех обнимаю")
                    bot.send_message(message.chat.id, "Готово")






            except Exception as ex:
                print(ex)
                bot.send_message( message.chat.id,"Что-то пошло не так")

    bot.polling()

if __name__ == '__main__':
    telegram_bot(token)