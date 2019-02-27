import json

import vk

session = vk.InteractiveSession('6bc146a313e1d99201ffc48d4958f79065ffba48e08329c905724891e06d30cbc0cbfefa2e9f5ffe406e3')
api = vk.API(session)

MESSAGE_START = 'Привет!✋'

COMMAND_TODAY = [
    'расписание',
    'расписание на сегодня',
    'оценки за сегодня',
    'сводка за сегодня',
    'сегодня',
    'оценки',
]

KEYBOARD_EMPTY = json.dumps({'one_time': True,
                             'buttons': []}, ensure_ascii=False)
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
        keyboard = KEYBOARD_MAIN
    api.messages.send(v='5.84', peer_id=peer_id, message=message, keyboard=keyboard)


def handle_user_message(user_id, message):
    pass


def handle_incoming_message(data):
    user_id = int(data['object']['from_id'])
    peer_id = int(data['object']['peer_id'])
    message = data['object']['text'].lower()

    if user_id == '123':
        handle_user_message(user_id, message)
