import random


def quicksort(_input):
    if len(_input) < 2:
        return _input

    _pivot = random.choice(_input)

    del _input[_input.index(_pivot)]
    _input.insert(0, _pivot)

    i = 1
    j = 1

    for x in range(1, len(_input)):
        if _input[i] <= _pivot:
            _input.insert(j, _input[i])
            del _input[i + 1]
            j += 1
        i += 1

    del _input[0]
    _input.insert(j - 1, _pivot)

    return quicksort(_input[0:j - 1]) + [_pivot] + quicksort(_input[j:i])
