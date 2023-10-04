# Generated by Django 4.1.3 on 2023-10-04 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_create_model_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('rating', models.FloatField(verbose_name='Рейтинг')),
                ('duration', models.IntegerField(verbose_name='Продолжительность')),
                ('actors', models.ManyToManyField(to='actors.actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actors.director')),
            ],
        ),
    ]
