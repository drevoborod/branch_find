#!/usr/bin/env python3

"""
Утилита для поиска нужной ветки в JSON и составления пути до него.
"""


EXAMPLE = [
    {
        "location": {
            "title": "Monaco",
            "coordinates": [
                60.334,
                30.678
            ]
        },
        "date": "2010-01-01"
    },
    {
        "title": "Event without date",
        "location": {
            "title": "Monaco",
            "coordinates": [
              60.334,
              30.678
            ]
          },
        "races": [
            {
              "title": "Qualifying",
              "begin_ts": 1494777600,
              "cars": [
                {
                  "title": "DEV Bot 1",
                  "model_id": "dev-bot-1",
                  "id": 1
                }
              ]
            }
          ]
    },
    {
        "title": "Event without location 3",
        "date": "2010-01-01",
        "races": [
            {
                "title": "Qualifying",
                "begin_ts": 1494777600,
                "cars": []
            }
        ]
    }
]


def parse_dict(data, to_find, result):
    for key in data:
        result.append(key)
        parse(data[key], to_find, result)


def parse_list(data, to_find, result):
    for number, item in enumerate(data):
        result.append(str(number))
        parse(item, to_find, result)


def parse(data,  to_find, result=None):
    if not result:
        result = []
    if type(data) is list:
        parse_list(data, to_find, result)
    elif type(data) is dict:
        if to_find in data:
            return result.append(to_find)
        else:
            parse_dict(data, to_find, result)
    return result


res = ".".join(parse(EXAMPLE, "begin_ts"))
print(res)