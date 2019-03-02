import json

import vk

session = vk.InteractiveSession('edda600957094d3d1560eec984903083ffb4556744a329048434baf7cc7b88197367db1da75a94f82ff69')
api = vk.API(session)

MESSAGE_START = 'Привет!✋'

COMMAND_TODAY = [
    'расписание',
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
        keyboard = KEYBOARD_EMPTY
    api.messages.send(v='5.92', peer_id=peer_id, message=message, keyboard=keyboard)


def handle_user_message(user_id, message):
    if message == 'начать':
        send_message(user_id, message)


def handle_incoming_message(data):
    user_id = int(data['object']['from_id'])
    peer_id = int(data['object']['peer_id'])
    message = data['object']['text'].lower()

    if user_id == 297582804:
        handle_user_message(user_id, message)
