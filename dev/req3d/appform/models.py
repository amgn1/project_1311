from django.db import models
from django.utils.crypto import get_random_string
import oauth.models as users

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
    )

    GROUPS = (
        ('ИВТ','ИВТ'),
        ('ИТСС','ИТСС'),
        ('КБ','КБ'),
        ('ПМ','ПМ'),
        ('ИБ','ИБ'),
        ('Другое','Другое'),
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
    user = models.ForeignKey(users.DiscordUser, on_delete=models.PROTECT)
    mail = models.EmailField('Электронная почта', max_length=100)
    name = models.CharField('ФИО', max_length=50)
    op = models.CharField('ОП', max_length=6, choices=GROUPS)
    course = models.CharField('Курс', max_length=25, choices=COURSES)
    project_name = models.CharField('Название проекта или КР/ВКР', max_length=50)
    teach_name = models.CharField('ФИО Научного руководителя', max_length=50)
    phone = models.CharField('Телефон', max_length=12)
    dmodel = models.FileField('3D модель', upload_to='3dmodels/', blank=False)
    note = models.FileField('Скан служебной записки', upload_to='notes/')
    comment = models.CharField('Комментарий к заявке', max_length=500)
    status = models.CharField('Статус заказа', max_length=30, choices=STATUS, default='На рассмотрении', blank=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'