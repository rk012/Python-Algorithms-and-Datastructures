def splitnum(_number):
    _number = str(_number)
    length = len(_number)

    return [int(_number[0:int(length / 2)]), int(_number[int(length / 2):length])]


def mult(_num1, _num2):
    n = min([len(str(_num1)), len(str(_num2))])

    if n == 1:
        return _num1 * _num2
    else:
        _num1_split = splitnum(_num1)
        _num2_split = splitnum(_num2)

        ac = mult(_num1_split[0], _num2_split[0])
        ad = mult(_num1_split[0], _num2_split[1])
        bc = mult(_num1_split[1], _num2_split[0])
        bd = mult(_num1_split[1], _num2_split[1])

        return 10 ** n * ac + 10 ** (n / 2) * (ad + bc) + bd
