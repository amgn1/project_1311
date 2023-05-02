from django.db import models
from django.utils.crypto import get_random_string
import oauth.models as users
from .validators import *

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


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'