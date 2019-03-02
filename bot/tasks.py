import datetime
import time

from bot import models


def get_seconds(t):
    return int(datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds())


def step_condition_checker():
    while True:
        for player in models.Player.objects.filter(is_await=True):
            step = player.step
            time_player_last_step = player.time_of_last_step
            time_now = datetime.datetime.now(datetime.timezone.utc)

            delay_step = get_seconds(step.delay)
            difference_time = int((time_now - time_player_last_step).total_seconds())
            print(difference_time)
            print(delay_step)

            if difference_time >= delay_step and \
                    step.date_of_begin >= time_now:
                print('YEAH!!!')  # TODO: Do something here
        time.sleep(3)
