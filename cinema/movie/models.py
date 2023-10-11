from django.db import models
from actors.models import Director, Actor


class Film(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    rating = models.FloatField(verbose_name='Рейтинг')
    duration = models.IntegerField(verbose_name='Продолжительность')
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f'id-{self.id}, {self.title,} {self.rating}'
