def binary_search(_list, _item):
    _start = 0
    _end = len(_list)
    _notfound = True

    while True:
        if _end - _start == 1:
            if _item == _list[_start] or _item == _list[_end]:
                return True
            else:
                return False
        if _list[int((_start + _end) / 2)] != _item:
            if _list[int((_start + _end) / 2)] > _item:
                _end = int((_start + _end) / 2)
            else:
                _start = int((_start + _end) / 2)

        else:
            return True
