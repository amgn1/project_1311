import telegram
from telegram.ext import Updater, CommandHandler
from appform.models import Articles

bot = telegram.Bot(token='6173981128:AAGVhJFSY6hDIUAYmjSYsI1uN2sPBNuAa6s')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Приветствую! Я бот для уведомления о статусе заказа.\n\n"
                                                                    "Пожалуйста, введите Ваш номер заказа ")

def order_status(update, context):
    number = context.args[0]
    try:
        order = Articles.objects.get(name=number)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Статус заказа {number}: {order.status}")
    except Articles.DoesNotExist:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Заказ {number} не найден.")

def main():
    updater = Updater(token='6173981128:AAGVhJFSY6hDIUAYmjSYsI1uN2sPBNuAa6s')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    # dispatcher.add_handler(CommandHandler('order_status', order_status))
    updater.start_polling()

if __name__ == '__main__':
    main()