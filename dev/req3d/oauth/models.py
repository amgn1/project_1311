from django.db import models
from .managers import DiscordUserOAuth2Manager

# Create your models here.

class DiscordUser(models.Model):
  class Meta:
    db_table = 'auth_user'
    verbose_name = 'Пользователя'
    verbose_name_plural = 'Пользователи'
  objects = DiscordUserOAuth2Manager()
  
  id = models.BigIntegerField(primary_key=True, verbose_name='Идентификатор')
  discord_tag = models.CharField(max_length=100, unique=True, verbose_name='Пользователь')
  avatar = models.CharField(max_length=100, null=True, verbose_name='Аватар')
  public_flags = models.IntegerField()
  flags = models.IntegerField()
  locale = models.CharField(max_length=100)
  mfa_enabled = models.BooleanField()
  last_login = models.DateTimeField(null=True, verbose_name='Последний раз заходил')


  is_active = models.BooleanField(default=True, verbose_name='Пользователь активирован')
  is_admin = models.BooleanField(default=False, verbose_name='Администратор')
  is_anonymous = models.BooleanField(default=False)

  REQUIRED_FIELDS = ['id']
  USERNAME_FIELD = 'discord_tag'

  def __str__(self):
    return self.discord_tag
  
  def get_username(self):
    return self.discord_tag 
  
  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True
  
  @property
  def is_authenticated(self):
    return True
  @property
  def is_staff(self):
    return self.is_admin
  
  
  