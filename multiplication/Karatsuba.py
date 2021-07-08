# noinspection PyUnresolvedReferences
from RecIntMult import splitnum


def karatsuba_mult(_num1, _num2):
    n = min([len(str(_num1)), len(str(_num2))])

    if n == 1:
        return _num1 * _num2
    else:
        _num1_split = splitnum(_num1)
        _num2_split = splitnum(_num2)

        ac = karatsuba_mult(_num1_split[0], _num2_split[0])
        bd = karatsuba_mult(_num1_split[1], _num2_split[1])

        p = _num1_split[0] + _num1_split[1]
        q = _num2_split[0] + _num2_split[1]
        pq = karatsuba_mult(p, q)

        adbc = pq - ac - bd

        return 10 ** n * ac + 10 ** (n / 2) * adbc + bd
