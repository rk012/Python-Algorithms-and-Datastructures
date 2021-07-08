from data_structures.heap import MinHeap


def heap_sort(_input):
    _heap = MinHeap(_input)
    _output = []
    for x in _input:
        _output.append(_heap.extractMin())

    return _output
