from operator import xor
from functools import reduce

input()
xs = list(map(int, input().strip().split()))
print(reduce(xor, xs) ^ reduce(xor, range(1, len(xs) + 2)))
