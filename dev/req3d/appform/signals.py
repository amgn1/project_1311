from bot.management.commands.bot import Command
from django.db.models.signals import post_save
from django.dispatch import receiver
from appform.models import Articles
from bot.models import TgUser


@receiver(post_save, sender=Articles)
def send_notification(sender, instance, **kwargs):
    print(instance.number)
    if kwargs.get('created', False):
        print('debug1')
        # Если заказ только что создан, то уведомление не отправляем
        return
    if instance.status_changed == 0:
        print('debug2')
        # Если статус заказа не изменился, то уведомление не отправляем
        return
    # Получаем список пользователей, которым нужно отправить уведомление
    try:
        users = TgUser.objects.filter(number=str(instance.number), order='Да')
        print('debug3')
        for user in users:
            print(user.user)
            # Отправляем уведомление пользователю
            a = Command.send_message(user.user_id, f'Статус заказа №{instance.number} изменен на: {instance.status}')
            print(a)
    except Exception as e:
        print(e)



@receiver(post_save, sender=Articles)
def mymodel_post_save(sender, instance, created, **kwargs):
    if created:
        print('adsfg')
        Command.send_message('385988250', f'Появился новый заказ №{instance.number}')