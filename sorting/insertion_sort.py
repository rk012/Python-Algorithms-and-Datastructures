def insertion_sort(_input):
    _output = [_input[0]]
    for i in range(1, len(_input)):
        if _input[i] >= _output[-1]:
            _output.append(_input[i])
        else:
            for j in range(0, len(_output)):
                if _input[i] < _output[j]:
                    _output.insert(j, _input[i])
                    break

    return _output
