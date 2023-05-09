import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from telebot import TeleBot
from telebot import types
from appform.models import Articles
from bot.models import TgUser
import json


# Объявление переменной бота
bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()								# Загрузка обработчиков
        bot.infinity_polling()
    # Бесконечный цикл бота

    def send_message(chat_id, text):
        url = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/sendMessage'
        data = {'chat_id': chat_id, 'text': text}
        print('Эта хуйня',chat_id)
        response = requests.post(url, data=data)
        return response.json()


    @bot.message_handler(commands=['start'])
    def start_handler(message):

        btn1 = types.InlineKeyboardButton("Отправить номер", callback_data='button1')
        markup = types.InlineKeyboardMarkup([[btn1]])
        bot.send_message(message.chat.id,
                         text="Приветствую, {0.first_name}! Я бот, отправляю уведомления о статусе Вашего заказа\n\nВы можете отправить номер Вашего заказа и я буду уведомлять о изменениях".format(
                             message.from_user), reply_markup=markup)

    @bot.callback_query_handler(func=lambda c: c.data == 'button1')
    def process_callback_button1(callback_query: types.CallbackQuery):
        bot.answer_callback_query(callback_query.id)
        bot.send_message(callback_query.from_user.id, 'Перед отправкой сообщения, проверьте правильность написания номера на наличие возможных опечаток.')

    @bot.message_handler(commands=['cancellation'])
    def start_handler(message):

        orders = TgUser.objects.filter(user=message.from_user.username)
        if orders:
            order_numbers = [order.number for order in orders]
            buttons = []
            for i in order_numbers:
                b = types.InlineKeyboardButton(i, callback_data=f'button7{i}')
                buttons.append([b])  # добавляем кнопку в отдельный список
            markup = types.InlineKeyboardMarkup(buttons)  # создаем разметку с кнопками
            bot.send_message(message.chat.id,
                                 text=f"У вас есть следующие заказы:", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, text="У вас нет активных заказов.")

    @bot.callback_query_handler(func=lambda c: c.data[0:7] == 'button7')
    def process_callback_button1(callback_query: types.CallbackQuery):
        try:
            button_text = callback_query.data[7:]
            print(f'{button_text} button text')
            my_object = TgUser.objects.get(number=button_text, user = callback_query.from_user.username)
        # Изменяем значение поля
            my_object.order = 'Нет'
        # Сохраняем изменения в базе данных
            my_object.save()
            bot.answer_callback_query(callback_query.id)
            bot.send_message(callback_query.from_user.id, f"Уведомление заказа {button_text} отменено")
        except:
            print('Ошибка')

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        if message.text.isdigit():
            print(message.text)
            number = message.text  # номер заказа, который нужно найти
            print(f'{number} initial number')
            data = {"b": "3", "n": number, "u": message.from_user.username, "id": message.from_user.id}
            x = json.dumps(data)
            print(x)
            btn1 = types.InlineKeyboardButton("Да", callback_data=x)
            btn2 = types.InlineKeyboardButton("Нет", callback_data='button4')
            markup1 = types.InlineKeyboardMarkup([[btn1, btn2]])
            btn3 = types.InlineKeyboardButton("Отправить номер", callback_data='button1')
            markup2 = types.InlineKeyboardMarkup([[btn3]])
            try:
                order = Articles.objects.get(number=number)  # получаем заказ по номеру
                status = order.status  # получаем статус заказа
                print('s',status)
                print(order.number, 'order number 1')
                try:
                    order = TgUser.objects.get(number=number, user=message.from_user.username)
                    status1 = order.order
                    print(order.number, 'order number 2')
                    print('sss',status1)
                    if status1 == 'Да':
                        bot.send_message(message.from_user.id,f'Cтатус заказа: {status}')
                    else:
                        bot.send_message(message.from_user.id, f'Cтатус заказа: {status}\n\nЖелаете, чтобы отправлял Вам уведомления тогда, когда статус заказа изменится?', reply_markup=markup1)
                except:
                    bot.send_message(message.from_user.id,
                                     f'Cтатус заказа: {status}\n\nЖелаете, чтобы отправлял Вам уведомления тогда, когда статус заказа изменится?',
                                     reply_markup=markup1)
            except Exception as e:
                print(e)
                bot.send_message(message.from_user.id,
                                 f'Заказ № {number} не найден\n\nПроверьте и отправьте еще раз',
                                 reply_markup=markup2)
        
        # Если пользователь отправил слово/фразу, на которое(ую) нет ответа
        else:
            bot.send_message(message.from_user.id, "Извините, я Вас не понимаю")
        
        @bot.callback_query_handler(func=lambda c: c.data in ['button4'])
        def process_callback_button2(callback_query: types.CallbackQuery):
            bot.answer_callback_query(callback_query.id)
            if callback_query.data == "button4":
                bot.send_message(callback_query.from_user.id, 'Хорошо! Вы всегда можете написать мне и узнать статус')

        @bot.callback_query_handler(func=lambda c: json.loads(c.data)["b"] in ['3'])
        def process_callback_button1(callback_query: types.CallbackQuery):
            bot.answer_callback_query(callback_query.id)
            data = json.loads(callback_query.data)
            if data["b"] == "3":
                print(message.text)
                number = data["n"]
                username = data["u"]
                id = data["id"]
                print(number)
                if TgUser.objects.filter(number=number, user=username).exists():
                    print('debug')
                    my_object = TgUser.objects.get(number=number, user=username)
                    print(my_object.number)
                    my_object.order = 'Да'
                    my_object.save()
                else:
                    user = TgUser(number=number, user=username, order='Да', user_id = id)
                    user.save()
                bot.send_message(callback_query.from_user.id, 'Отлично! Как изменится статус, Вы тут же об этом узнаете.'
                                                              '\n\nВы можете отменить уведомления, набрав команду /cancellation')
            



