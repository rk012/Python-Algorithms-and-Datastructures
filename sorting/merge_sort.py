def _merge(_seq1, _seq2):
    i = 0
    j = 0
    _output = []
    for x in range(0, len(_seq1) + len(_seq2)):
        if _seq1[i] > _seq2[j]:
            _output.append(_seq2[j])
            j += 1
        else:
            _output.append(_seq1[i])
            i += 1

        if i == len(_seq1):
            for y in range(j, len(_seq2)):
                _output.append(_seq2[y])
            break
        elif j == len(_seq2):
            for y in range(i, len(_seq1)):
                _output.append(_seq1[y])
            break

    return _output


def sort(_input):
    length = len(_input)

    if length == 2:
        return [_input[1], _input[0]] if _input[0] > _input[1] else _input

    _input_1 = _input[0:int(length/2)]
    _input_2 = _input[int(length/2):length]

    return _merge(sort(_input_1), sort(_input_2))
