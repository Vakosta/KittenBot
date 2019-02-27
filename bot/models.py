from django.db import models


class Step(models.Model):
    title = models.CharField(verbose_name='заголовок',
                             max_length=100,
                             null=True)
    message = models.TextField(verbose_name='сообщение',
                               max_length=3000,
                               null=False)


class Player(models.Model):
    name = models.CharField(verbose_name='имя',
                            max_length=100,
                            null=True)
    step = models.ForeignKey(verbose_name='шаг',
                             to=Step,
                             on_delete=models.SET_NULL,
                             null=True)
