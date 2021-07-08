def bubble_sort(_input):
    while True:
        _sorted = True

        for i in range(0, len(_input) - 1):
            _bubble = [_input[i], _input[i + 1]]
            if _bubble[0] >= _bubble[1]:
                _sorted = False
                _input[i] = _bubble[1]
                _input[i + 1] = _bubble[0]

        if _sorted:
            break

    return _input
