from django.db.models.signals import post_save
from django.dispatch import receiver
from appform.models import Articles
from bot.management.commands.bot import Command
from bot.models import TgUser


@receiver(post_save, sender=Articles)
def order_status_changed(sender, instance, **kwargs):
    if instance.status:
        n = instance.number
        my_queryset = TgUser.objects.filter(number=n)
        user = my_queryset.user

    Command.send_telegram_message(chat_id=user, message=f'Заказ {instance.status}')