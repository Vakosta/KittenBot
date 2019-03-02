import threading

from django.apps import AppConfig


class BotConfig(AppConfig):
    name = 'bot'

    def ready(self):
        from bot import tasks
        threading.Thread(target=tasks.step_condition_checker,
                         name='StepConditionChecker',
                         daemon=True).start()
