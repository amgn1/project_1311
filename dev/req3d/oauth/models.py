from django.db import models
from .managers import DiscordUserOAuth2Manager

# Create your models here.

class DiscordUser(models.Model):
  class Meta:
    db_table = 'auth_user'
  objects = DiscordUserOAuth2Manager()
  
  id = models.BigIntegerField(primary_key=True)
  discord_tag = models.CharField(max_length=100, unique=True)
  avatar = models.CharField(max_length=100, null=True)
  public_flags = models.IntegerField()
  flags = models.IntegerField()
  locale = models.CharField(max_length=100)
  mfa_enabled = models.BooleanField()
  last_login = models.DateTimeField(null=True)

  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
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
  
  
  