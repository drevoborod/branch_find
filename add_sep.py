def add_sep(iterable, sep, result=None):
    if not result:
        result = []
    result.append(iterable[0])
    iterable = iterable[1:]
    if iterable:
        result.append(sep)
        add_sep(iterable, sep, result)
    else:
        return result
    return result