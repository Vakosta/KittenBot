import json

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

session = vk_api.VkApi(token='edda600957094d3d1560eec984903083ffb4556744a329048434baf7cc7b88197367db1da75a94f82ff69')
api = session.get_api()

MESSAGE_START = 'Привет!'

COMMAND_TODAY = [
    'расписание',
]

KEYBOARD_EMPTY = {'one_time': False, 'buttons': []}
KEYBOARD_MAIN = json.dumps({'one_time': False,
                            'buttons': [
                                [
                                    {'action': {'type': 'text', 'label': COMMAND_TODAY[0].capitalize()},
                                     'color': 'primary'},
                                    {'action': {'type': 'text', 'label': 'kek'},
                                     'color': 'primary'},
                                ],
                                [
                                    {'action': {'type': 'text', 'label': 'kek'},
                                     'color': 'default'},
                                ],
                            ]}, ensure_ascii=False)

KEYBOARD_SETTINGS = json.dumps({'one_time': True,
                                'buttons': [
                                    [
                                        {'action': {'type': 'text', 'label': 'Отключить уведомления'},
                                         'color': 'primary'},
                                        {'action': {'type': 'text', 'label': 'Назад'},
                                         'color': 'default'},
                                    ]
                                ]}, ensure_ascii=False)


def send_message(peer_id, message, keyboard=None):
    if keyboard is None:
        keyboard = KEYBOARD_EMPTY
    api.messages.send(v='5.84',
                      peer_id=peer_id,
                      message=message,
                      keyboard=json.dumps(keyboard, ensure_ascii=False))


def handle_user_message(user_id, message):
    if message == 'начать':
        send_message(user_id, message)


def handle_incoming_message(data):
    user_id = int(data['object']['from_id'])
    peer_id = int(data['object']['peer_id'])
    message = data['object']['text'].lower()

    if user_id == 297582804:
        handle_user_message(user_id, message)


def get_online(user_id):
    return api.users.get(v='5.84', user_ids=user_id, fields='online,last_seen')[0]['online']


def longpoll_task():
    from bot import models
    longpoll = VkLongPoll(session)
    while True:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.from_user:
                    try:
                        player = models.Player.objects.get(vk_id=event.user_id)
                        for choice in player.step.choices.all():
                            if choice.command == event.text:
                                player.step = choice.next_step
                                player.save()
                                player.send_answer()
                    except Exception:
                        pass
