from django.db import models


class Step(models.Model):
    title = models.CharField(verbose_name='заголовок',
                             max_length=100,
                             null=True)
    message = models.TextField(verbose_name='сообщение',
                               max_length=3000,
                               null=False)
    choices = models.ManyToManyField(verbose_name='исходы',
                                     to='self',
                                     blank=True)
    delay = models.TimeField(verbose_name='задержка',
                             null=True,
                             blank=True)
    date_of_begin = models.DateTimeField(verbose_name='время начала',
                                         null=True,
                                         blank=True)

    class Meta:
        verbose_name = 'шаг'
        verbose_name_plural = 'шаги'

    def __str__(self):
        return self.title


class Player(models.Model):
    name = models.CharField(verbose_name='имя',
                            max_length=100,
                            null=True)
    vk_id = models.IntegerField(verbose_name='вк id',
                                null=False)
    step = models.ForeignKey(verbose_name='шаг',
                             to=Step,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)

    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'

    def __str__(self):
        return self.name
