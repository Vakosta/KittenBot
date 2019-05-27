import datetime

from bot.decorators import await_players_task


def get_seconds(t):
    return int(datetime.timedelta(hours=t.hour,
                                  minutes=t.minute,
                                  seconds=t.second)
               .total_seconds())


@await_players_task
def step_condition_checker(player):
    step = player.step
    time_player_last_step = player.time_of_last_step
    time_now = datetime.datetime.now(datetime.timezone.utc)

    try:
        delay_step = get_seconds(step.delay)
    except Exception:
        delay_step = 0
    try:
        difference_time = int((time_now - time_player_last_step).total_seconds())
    except Exception:
        difference_time = 0

    if difference_time >= delay_step \
            and (step.date_of_begin is None
                 or (step.date_of_begin is not None and step.date_of_begin <= time_now)):
        player.send_answer()
