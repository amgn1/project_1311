# Generated by Django 4.1.6 on 2023-05-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('order', models.CharField(default='Нет', max_length=3)),
                ('user_id', models.CharField(max_length=300)),
            ],
        ),
    ]
