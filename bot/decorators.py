import time

from bot import models


def await_players_task(func):
    def wrapper():
        while True:
            for player in models.Player.objects.filter(is_await=True):
                try:
                    func(player)
                except Exception:
                    pass
            time.sleep(3)

    return wrapper
