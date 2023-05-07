from bot.management.commands.bot import Command
from django.db.models.signals import post_save
from django.dispatch import receiver
from appform.models import Articles
from bot.models import TgUser


@receiver(post_save, sender=Articles)
def send_notification(sender, instance, **kwargs):
    if kwargs.get('created', False):
        # Если заказ только что создан, то уведомление не отправляем
        return
    if instance.status_changed:
        # Если статус заказа не изменился, то уведомление не отправляем
        return
    # Получаем список пользователей, которым нужно отправить уведомление
    users = TgUser.objects.filter(number=instance.number, order='да')
    for user in users:
        # Отправляем уведомление пользователю
        Command.send_message(user.user, f'Статус заказа {instance.number} изменен на {instance.status}')