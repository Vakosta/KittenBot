import threading

from django.apps import AppConfig

from bot import tasks


class BotConfig(AppConfig):
    name = 'bot'

    def ready(self):
        threading.Thread(target=tasks.step_condition_checker,
                         name='StepConditionChecker',
                         daemon=True).start()
