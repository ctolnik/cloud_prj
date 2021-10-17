from django.contrib.auth import get_user_model
from django.db import models
from taggit.managers import TaggableManager


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name="Логин")
    password = models.CharField(max_length=50, verbose_name="Пароль")
    shared = models.ForeignKey('File', on_delete=models.PROTECT, blank=True, null=True ,verbose_name="Доступные файлы", related_name='shared')
    # phone = 
    # mail

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

class File(models.Model):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.CharField(max_length=250, verbose_name="Описание", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user', verbose_name="Владелец")
    file = models.FileField(upload_to='uloads/', verbose_name="Файл")
    tags = TaggableManager() 

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
        ordering = ['-created']
