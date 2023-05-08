from django.db import models
import appform.models as n


class TgUser(models.Model):
    number = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    order = models.CharField(default='Нет', max_length=3)
    user_id = models.CharField(max_length=300)
