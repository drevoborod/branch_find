#!/usr/bin/env python3


def parse(data, query, current_path=None, result=None):
    if not result:
        result = []
    if not current_path:
        current_path = []
    if isinstance(data, dict):
        return parse_dict(data, query, current_path, result)
    elif isinstance(data, list):
        return parse_list(data, query, current_path, result)
    return result


def parse_dict(data, query, current_path, result):
    for key, value in data.items():
        path = current_path.copy()
        path.append(key)
        if key == query:
            result.append(path)
        result = parse(value, query, path, result)
    return result


def parse_list(data, query, current_path, result):
    for number, item in enumerate(data):
        path = current_path.copy()
        path.append(number)
        if item == query:
            result.append(path)
        else:
            result = parse(item, query, path, result)
    return result


def _prepare_int(item):
    if type(item) is int:
        return f'[{item}]'
    elif item.isdigit():
        return f"['{item}']"
    return item


def locate(array):
    result = []
    for subarray in array:
        res = []
        for key in subarray:
            if type(key) is int:
                template = '[{}]'
            else:
                template = "['{}']"
            res.append(template.format(key))
        result.append(''.join(res))
    return result


def locate_with_dots(array):
    """Prepares results only for structures which support dot notations."""
    return [('.' + '.'.join(map(_prepare_int, x))).replace('.[', '[') for x in array]


if __name__ == '__main__':

    ### Usage examples ###

    # Not necessary, added just for demonstration purposes. Regular dicts/lists can be used.
    # https://github.com/drevoborod/altcollections/blob/master/collections.py
    from alt import RecursiveConverter

    # By default, RecursiveConverter converts all dicts inside the structure into ExtendedDict.
    # ExtendedDict behaves just like normal dict but supports dot notations.
    EXAMPLE = RecursiveConverter([
        {
            "location": {
                "title": "Monaco",
                "coordinates": [
                    60.334,
                    30.678,
                    'begin_ts'
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
                    "begin_ts": 1111111,
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
                    "begin_ts": 2222222222,
                    "cars": []
                },
                {
                    "title": "Qualifying",
                    "begin_ts": {
                        1: {
                            "title": "Qualifying",
                            "begin_ts": 3333333,
                            "cars": ['a', 'b', 1, {"begin_ts": 44444}]
                        },
                        '1': {
                            "title": "Qualifying",
                            "begin_ts": 5555555555,
                            "cars": ['a', 'b', 1, {"begin_ts": 6666666}]
                        }
                    },
                    "cars": [
                        {
                            "title": "Qualifying",
                            "begin": 1494777600,
                            "cars": []
                        },
                        {
                            "title": "Qualifying",
                            "begin_ts": 7777777777,
                            "cars": []
                        }
                    ]
                }
            ]
        }
    ])
    EXAMPLE1 = RecursiveConverter({
        'key1': [
            {
                "location": {
                    "title": "Monaco",
                    "coordinates": [
                        60.334,
                        30.678,
                        'begin_ts'
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
                        "begin_ts": 1111111,
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
                        "begin_ts": 2222222222,
                        "cars": []
                    },
                    {
                        "title": "Qualifying",
                        "begin_ts": {
                            1: {
                                "title": "Qualifying",
                                "begin_ts": 3333333,
                                "cars": ['a', 'b', 1, {"begin_ts": 44444}]
                            },
                            '1': {
                                "title": "Qualifying",
                                "begin_ts": 5555555555,
                                "cars": ['a', 'b', 1, {"begin_ts": 6666666}]
                            }
                        },
                        "cars": [
                            {
                                "title": "Qualifying",
                                "begin": 1494777600,
                                "cars": []
                            },
                            {
                                "title": "Qualifying",
                                "begin_ts": 7777777777,
                                "cars": []
                            }
                        ]
                    }
                ]
            }
        ]
    })

    for example in (EXAMPLE, EXAMPLE1):
        for item in locate(parse(example, "begin_ts")):
            print(item)
            print(eval(f'example{item}'))
            print()

    print('#' * 50)

    # only for mappings which support dot notations (ExtendedDicts):
    for example in (EXAMPLE, EXAMPLE1):
        for item in locate_with_dots(parse(example, "begin_ts")):
            print(item)
            print(eval(f'example{item}'))
            print()
