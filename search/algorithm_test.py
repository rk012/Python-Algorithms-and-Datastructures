import random
import time

import sys
sys.path.append("../")

from search import *

sequence = [2 * x for x in range(0, 50000001)]
item = random.randint(0, 100000000)

start_time = time.time()
linear_search.linear_search(sequence, item)
print(f"Linear Search: {time.time() - start_time}")

start_time = time.time()
binary_search.binary_search(sequence, item)
print(f"Binary Search: {time.time() - start_time}")
