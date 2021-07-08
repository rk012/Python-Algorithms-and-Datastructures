class _Heap:
    def __init__(self, unsorted_array=()):
        self.heap_array = []

        for item in unsorted_array:
            self.insert(item)

    def insert(self, item):
        pass

    def swap(self, index_0, index_1):
        _swap_array = [self.heap_array[index_0], self.heap_array[index_1]]
        self.heap_array[index_0] = _swap_array[1]
        self.heap_array[index_1] = _swap_array[0]


class MaxHeap(_Heap):
    def insert(self, item):
        self.heap_array.append(item)

        current_index = len(self.heap_array) - 1

        while current_index > 0:
            next_index = int((current_index - 1) / 2)
            if self.heap_array[current_index] > self.heap_array[next_index]:
                self.swap(current_index, next_index)
                current_index = next_index
            else:
                break

    def extractMax(self):
        current_index = 0

        max_element = self.heap_array[0]
        self.swap(0, -1)
        del self.heap_array[-1]

        while 2 * current_index + 1 < len(self.heap_array):
            if 2 * current_index + 2 == len(self.heap_array):
                if self.heap_array[2 * current_index + 1] > self.heap_array[current_index]:
                    self.swap(2 * current_index + 1, current_index)

                return max_element

            if self.heap_array[2 * current_index + 1] > self.heap_array[2 * current_index + 2]:
                if self.heap_array[2 * current_index + 1] > self.heap_array[current_index]:
                    self.swap(2 * current_index + 1, current_index)
                    current_index = 2 * current_index + 1

                else:
                    return max_element

            else:
                if self.heap_array[2 * current_index + 2] > self.heap_array[current_index]:
                    self.swap(2 * current_index + 2, current_index)
                    current_index = 2 * current_index + 2

                else:
                    return max_element

        return max_element


class MinHeap(_Heap):
    def insert(self, item):
        self.heap_array.append(item)

        current_index = len(self.heap_array) - 1

        while current_index > 0:
            next_index = int((current_index - 1) / 2)
            if self.heap_array[current_index] < self.heap_array[next_index]:
                self.swap(current_index, next_index)
                current_index = next_index
            else:
                break

    def extractMin(self):
        current_index = 0

        min_element = self.heap_array[0]
        self.swap(0, -1)
        del self.heap_array[-1]

        while 2 * current_index + 1 < len(self.heap_array):
            if 2 * current_index + 2 == len(self.heap_array):
                if self.heap_array[2 * current_index + 1] < self.heap_array[current_index]:
                    self.swap(2 * current_index + 1, current_index)

                return min_element

            if self.heap_array[2 * current_index + 1] < self.heap_array[2 * current_index + 2]:
                if self.heap_array[2 * current_index + 1] < self.heap_array[current_index]:
                    self.swap(2 * current_index + 1, current_index)
                    current_index = 2 * current_index + 1

                else:
                    return min_element

            else:
                if self.heap_array[2 * current_index + 2] < self.heap_array[current_index]:
                    self.swap(2 * current_index + 2, current_index)
                    current_index = 2 * current_index + 2

                else:
                    return min_element

        return min_element
