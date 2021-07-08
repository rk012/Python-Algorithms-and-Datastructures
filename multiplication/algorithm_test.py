import time

import sys
sys.path.append("../")

from multiplication import *

num1 = 34767645
num2 = 98452365

start_time = time.time()

for i in range(0, 10000):
    foo = RecIntMult.mult(num1, num2)

print(f"RecIntMult: {time.time() - start_time}")

start_time = time.time()

for i in range(0, 10000):
    foo = Karatsuba.karatsuba_mult(num1, num2)

print(f"Karatsuba: {time.time() - start_time}")
