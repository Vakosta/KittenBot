import time

from bot import models


def step_condition_checker():
    while True:
        for player in models.Player.objects.filter(is_await=True):
            print('kek')
        time.sleep(3)
