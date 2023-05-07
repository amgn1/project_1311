from django.db import models
from .managers import KeycloakUserOAuth2Manager

# Create your models here.

class KeycloakUser(models.Model):
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
    objects = KeycloakUserOAuth2Manager()
  
    sub = models.CharField(primary_key=True, verbose_name='Идентификатор', unique=True, max_length=200)
    full_name = models.CharField(max_length=100, unique=True, verbose_name='Пользователь')
    avatar = models.URLField(null=True, verbose_name='Аватар')
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField()
    last_login = models.DateTimeField(null=True, verbose_name='Последний раз заходил')
    # access_token = models.CharField(unique=True, max_length=2000, null=True)
    # refresh_token = models.CharField(unique=True, max_length=2000, null=True)


    is_active = models.BooleanField(default=True, verbose_name='Пользователь активирован')
    is_admin = models.BooleanField(default=False, verbose_name='Администратор')
    is_anonymous = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['sub']
    USERNAME_FIELD = 'full_name'

    def __str__(self):
        return self.full_name
    
    def get_username(self):
        return self.full_name 
    
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
  
  
  