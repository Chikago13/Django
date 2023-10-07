from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    data = models.DateTimeField(verbose_name='Возраст')
    country = models.CharField(max_length=100, verbose_name='Страна')

    def __str__(self):
        return f'id-{self.id}, {self.name}'


class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    data = models.DateTimeField(verbose_name='Возраст')
    country = models.CharField(max_length=100, verbose_name='Страна')
    number_main_roles = models.IntegerField(verbose_name='Количество главных ролей')

    def __str__(self):
        return f'id-{self.id}, {self.name}'

