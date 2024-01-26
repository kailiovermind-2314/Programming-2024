"""
现有一个列表，请写出函数，求出列表里元素最小的绝对值之差（取正数）,不存在则返回None。
"""
from itertools import pairwise

nums = sorted(abs(num) for num in [1, 3, 5, -7, 9, -9])
print(min(i[1] - i[0] for i in pairwise(nums)))
