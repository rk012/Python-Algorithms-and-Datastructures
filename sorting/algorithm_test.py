import random
import time

import sys
sys.path.append("../")

from sorting import *

scrambled_list = [random.randint(0, 1000000) for i in range(0, 16384)]
scrambled_list_1 = [random.randint(0, 1000000) for i in range(0, 16384)]
scrambled_list_2 = [random.randint(0, 1000000) for i in range(0, 16384)]

# Bubble sort is ommited due to very long runtimes.

# start_time = time.time()
# bubble_sort.bubble_sort(scrambled_list)
# print(f"Bubble Sort: {time.time() - start_time}")

start_time = time.time()
selection_sort.selection_sort(scrambled_list_1)
print(f"Selection Sort: {time.time() - start_time}")

start_time = time.time()
insertion_sort.insertion_sort(scrambled_list)
print(f"Insertion Sort: {time.time() - start_time}")

start_time = time.time()
merge_sort.sort(scrambled_list)
print(f"Merge Sort: {time.time() - start_time}")

start_time = time.time()
quicksort.quicksort(scrambled_list_2)
print(f"Quick Sort: {time.time() - start_time}")

start_time = time.time()
heap_sort.heap_sort(scrambled_list)
print(f"Heap Sort: {time.time() - start_time}")
