import pytest
from function import open_json, get_filtered_data, get_formatted_data, get_last_values


def test_open_json():
    data = open_json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_filtered_data(item):
    assert get_filtered_data(item) == [{

        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 11776614605963066702"
        }
    ]
    assert get_filtered_data(item, filter_empty_from=True) == [{

        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]


def test_get_last_values(item2):
    data = get_last_values(item2, 3)
    dates = [x['date'] for x in data]
    assert dates == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572']


def test_get_formatted_data(item2):
    assert get_formatted_data(item2) == ['03.07.2019 Перевод организации\nMasterCard 7158 30** ****6758 -> Счет ''**5560\n8221.37 USD',
                                         '26.08.2019 Перевод организации\nMaestro 1596 83** ''****5199 -> Счет **9589\n31957.58 руб.',
                                         '30.06.2018 ''Перевод ''организации\n  -> Счет **6702\n9824.07 USD']
