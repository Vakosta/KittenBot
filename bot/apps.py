import threading

from django.apps import AppConfig

from bot import bot_vk


class BotConfig(AppConfig):
    name = 'bot'

    def ready(self):
        from bot import tasks
        threading.Thread(target=bot_vk.longpoll_task,
                         name='LongPoll',
                         daemon=True).start()
        threading.Thread(target=tasks.step_condition_checker,
                         name='StepConditionChecker',
                         daemon=True).start()
