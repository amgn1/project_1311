# Generated by Django 4.1.6 on 2023-03-15 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_alter_discorduser_avatar_alter_discorduser_id'),
        ('appform', '0003_alter_articles_comment_alter_articles_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oauth.discorduser'),
            preserve_default=False,
        ),
    ]
