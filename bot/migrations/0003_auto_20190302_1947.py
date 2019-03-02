# Generated by Django 2.1.7 on 2019-03-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bot', '0002_auto_20190302_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_await',
            field=models.BooleanField(default=False, verbose_name='в ожидании'),
        ),
        migrations.AddField(
            model_name='step',
            name='second_message',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='второе сообщение'),
        ),
        migrations.AlterField(
            model_name='step',
            name='message',
            field=models.TextField(max_length=5000, verbose_name='сообщение'),
        ),
    ]