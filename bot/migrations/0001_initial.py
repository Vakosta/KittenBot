# Generated by Django 2.1.7 on 2019-02-27 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
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
                ('delay', models.TimeField(blank=True, null=True, verbose_name='задержка')),
                ('date_of_begin', models.DateTimeField(blank=True, null=True, verbose_name='время начала')),
                ('choices',
                 models.ManyToManyField(related_name='_step_choices_+', to='bot.Step', verbose_name='исходы')),
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
    ]