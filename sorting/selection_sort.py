def selection_sort(_input):
    _output = []

    while len(_input) != 0:
        _min = _input[0]

        for x in _input:
            if x < _min:
                _min = x

        _output.append(_min)
        del _input[_input.index(_min)]

    return _output
