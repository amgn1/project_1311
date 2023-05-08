from django.db import models
from django.utils.crypto import get_random_string
import oauth.models as users
from .validators import *
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import Signal
import os

dmodel_deleted = Signal()
note_deleted = Signal()

# Create your models here.

def func():
    nm = Articles.objects.all()
    nm1 = 0
    for i1 in nm:
        if i1.id > nm1:
            nm1 = i1.id
    nm1 = nm1 + 1
    nn = '{:05}'.format(nm1)
    return nn


class Articles(models.Model):

    COURSES = (
    ('1 курс','1 курс'),
    ('2 курс','2 курс'),
    ('3 курс','3 курс'),
    ('4 курс','4 курс'),
    ('1 курс (магистратура)','1 курс (магистратура)'),
    ('2 курс (магистратура)','2 курс (магистратура)'),
    ('Аспирантура','Аспирантура'),
    ('Сотрудник','Сотрудник'),
    (None,'Принадлежность не выбрана'),
    
    )

    GROUPS = (
        ('ИВТ','ИВТ'),
        ('ИТСС','ИТСС'),
        ('КБ','КБ'),
        ('ПМ','ПМ'),
        ('ИБ','ИБ'),
        ('Другое','Другое'),
        (None,'Направление подготовки не выбрано'),
    )

    STATUS = (
        ('На рассмотрении','На рассмотрении'),
        ('В обработке','В обработке'),
        ('В работе','В работе'),
        ('Ожидает получения','Ожидает получения'),
        ('Отклонен','Отклонен'),
        ('Выполнен','Выполнен')
    )

    number = models.CharField(max_length=20, unique=True, default=func, verbose_name='Номер заявки')
    user = models.ForeignKey(users.KeycloakUser, on_delete=models.PROTECT, verbose_name='Пользователь')
    mail = models.EmailField('Электронная почта', max_length=100, validators=[validate_mail])
    name = models.CharField('ФИО', max_length=50, validators=[validate_name])
    op = models.CharField('ОП', max_length=6, choices=GROUPS, validators=[validate_op])
    course = models.CharField('Курс', max_length=25, choices=COURSES, validators=[validate_course])
    project_name = models.CharField('Название проекта или КР/ВКР', max_length=50, validators=[validate_project_name])
    teach_name = models.CharField('ФИО Научного руководителя', max_length=50, validators=[validate_teach_name])
    phone = models.CharField('Телефон', max_length=20, validators=[validate_phone])
    dmodel = models.FileField('3D модель', upload_to='3dmodels/', validators=[validate_dmodel])
    note = models.FileField('Скан служебной записки', upload_to='notes/', validators=[validate_note])
    comment = models.CharField('Комментарий к заявке', max_length=500, validators=[], blank=True, null=True)
    status = models.CharField('Статус заказа', max_length=30, choices=STATUS, default='На рассмотрении')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    status_changed = models.BooleanField(default=False)


    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if self.pk:
            # Если заказ уже существует, то проверяем, изменился ли статус
            old_status = Articles.objects.get(pk=self.pk).status
            if old_status != self.status:
                self.status_changed = True
        super().save(*args, **kwargs)
  
    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'
        
     


@receiver(pre_delete, sender=Articles)
def delete_file(sender, instance, **kwargs):
    instance.dmodel.delete(False)
    instance.note.delete(False)

@receiver(pre_save, sender=Articles)
def delete_old_file(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_dmodel = sender.objects.get(pk=instance.pk).dmodel
        old_note = sender.objects.get(pk=instance.pk).note
    except sender.DoesNotExist:
        return False

    new_dmodel = instance.dmodel
    new_note = instance.note
    if old_dmodel != new_dmodel and old_note != new_note:
        if os.path.isfile(old_dmodel.path) and os.path.isfile(old_note.path):
            os.remove(old_dmodel.path)
            os.remove(old_note.path)
            dmodel_deleted.send(sender=sender, path=old_dmodel.path)
            note_deleted.send(sender=sender, path=old_note.path)

    return True

@receiver(pre_save, sender=Articles)
def delete_model_file(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_dmodel = sender.objects.get(pk=instance.pk).dmodel
    except sender.DoesNotExist:
        return False

    new_dmodel = instance.dmodel
    if old_dmodel != new_dmodel:
        if os.path.isfile(old_dmodel.path):
            os.remove(old_dmodel.path)
            dmodel_deleted.send(sender=sender, path=old_dmodel.path)


@receiver(pre_save, sender=Articles)
def delete_note_file(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_note = sender.objects.get(pk=instance.pk).note
    except sender.DoesNotExist:
        return False

    new_note = instance.note
    if old_note != new_note and new_note != None:
        if os.path.isfile(old_note.path):
            os.remove(old_note.path)
            note_deleted.send(sender=sender, path=old_note.path)
