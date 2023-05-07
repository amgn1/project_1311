# Generated by Django 4.1.6 on 2023-04-28 03:40

from django.db import migrations, models
import oauth.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeycloakUser',
            fields=[
                ('sub', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Идентификатор')),
                ('full_name', models.CharField(max_length=100, unique=True, verbose_name='Пользователь')),
                ('avatar', models.URLField(null=True, verbose_name='Аватар')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('email_verified', models.BooleanField()),
                ('last_login', models.DateTimeField(null=True, verbose_name='Последний раз заходил')),
                ('is_active', models.BooleanField(default=True, verbose_name='Пользователь активирован')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор')),
                ('is_anonymous', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Пользователя',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', oauth.managers.KeycloakUserOAuth2Manager()),
            ],
        ),
    ]
