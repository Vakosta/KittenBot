from django.db import models
from django.utils.timezone import now

from bot import bot_vk


class Choice(models.Model):
    command = models.CharField(verbose_name='команда',
                               max_length=100,
                               null=False,
                               blank=False)

    next_step = models.ForeignKey(to='Step',
                                  on_delete=models.CASCADE,
                                  verbose_name='следующий шаг',
                                  null=False,
                                  blank=False)

    class Meta:
        verbose_name = 'исход'
        verbose_name_plural = 'исходы'

    def __str__(self):
        return self.command


class Step(models.Model):
    title = models.CharField(verbose_name='заголовок',
                             max_length=100,
                             null=True)
    message = models.TextField(verbose_name='сообщение',
                               max_length=5000,
                               null=False)
    next_step = models.ForeignKey(verbose_name='следующий шаг',
                                  help_text='Если указано, то сразу осуществляется переход к следующему шагу.',
                                  to='self',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True)
    choices = models.ManyToManyField(verbose_name='исходы',
                                     to=Choice,
                                     blank=True)

    when_online = models.BooleanField(verbose_name='когда онлайн',
                                      default=False,
                                      null=False,
                                      blank=False)
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
    is_await = models.BooleanField(verbose_name='в ожидании',
                                   default=False,
                                   null=False,
                                   blank=False)
    time_of_last_step = models.DateTimeField(verbose_name='время последнего действия',
                                             default=now,
                                             null=False,
                                             blank=False)

    class Meta:
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'

    def __str__(self):
        return self.name

    def send_answer(self):
        self.is_await = False
        bot_vk.send_message(self.vk_id, self.step.message)
        if self.step.next_step is not None:
            self.next_step()
        self.save()

    def activate_step(self, step):
        if step.delay is not None or \
                step.date_of_begin is not None:
            self.step = step
            self.is_await = True
            self.save()
        else:
            self.step = step
            self.send_answer()

    def next_step(self, command=None):
        if self.step.next_step is not None:
            self.activate_step(self.step.next_step)
        elif command is not None:
            for choice in self.step.choices.all():
                if command == choice.command:
                    self.activate_step(choice.next_step)
