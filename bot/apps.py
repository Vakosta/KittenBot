import os
import threading

import psutil as psutil
from django.apps import AppConfig

from bot import bot_vk


class BotConfig(AppConfig):
    name = 'bot'

    def ready(self):
        from bot import tasks
        startScheduler = True

        # check WEB_CONCURRENCY exists and is more than 1
        web_concurrency = os.environ.get("WEB_CONCURRENCY")
        if web_concurrency:
            mypid = os.getpid()
            print("[%s] WEB_CONCURRENCY exists and is set to %s" % (mypid, web_concurrency))
            gunicorn_workers = int(web_concurrency)
            if gunicorn_workers > 1:
                maxPid = self.getMaxRunningGunicornPid()
                if maxPid == mypid:
                    startScheduler = True
                else:
                    startScheduler = False

        if startScheduler:
            threading.Thread(target=bot_vk.longpoll_task,
                             name='LongPoll',
                             daemon=True).start()
            threading.Thread(target=tasks.step_condition_checker,
                             name='StepConditionChecker',
                             daemon=True).start()
        else:
            threading.Thread(target=bot_vk.longpoll_task,
                             name='LongPoll',
                             daemon=True).start()
            threading.Thread(target=tasks.step_condition_checker,
                             name='StepConditionChecker',
                             daemon=True).start()

    def getMaxRunningGunicornPid(self):
        running_pids = psutil.pids()
        maxPid = -1
        for pid in running_pids:
            proc = psutil.Process(pid)
            proc_name = proc.name()
            if proc_name == "gunicorn":
                if maxPid < pid:
                    maxPid = pid
        print("Max Gunicorn PID: %s", maxPid)
        return maxPid
