# Generated by Django 2.1.7 on 2019-03-02 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=100, verbose_name='команда')),
            ],
            options={
                'verbose_name': 'выбор',
                'verbose_name_plural': 'выборы',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='имя')),
                ('vk_id', models.IntegerField(verbose_name='вк id')),
            ],
            options={
                'verbose_name': 'игрок',
                'verbose_name_plural': 'игроки',
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='заголовок')),
                ('message', models.TextField(max_length=3000, verbose_name='сообщение')),
                ('when_online', models.BooleanField(default=False, verbose_name='когда онлайн')),
                ('delay', models.TimeField(blank=True, null=True, verbose_name='задержка')),
                ('date_of_begin', models.DateTimeField(blank=True, null=True, verbose_name='время начала')),
                ('choices', models.ManyToManyField(blank=True, to='bot.Choice', verbose_name='исходы')),
            ],
            options={
                'verbose_name': 'шаг',
                'verbose_name_plural': 'шаги',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.Step',
                                    verbose_name='шаг'),
        ),
        migrations.AddField(
            model_name='choice',
            name='next_step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.Step',
                                    verbose_name='следующий шаг'),
        ),
    ]
