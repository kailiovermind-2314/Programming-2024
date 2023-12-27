"""
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

Easy problem, easy solution.
"""
binary = list(map(int, bin(int(input()))[2:]))
i = 0
try:
  while (binary[i] + binary[i + 1]) == 1:
    i += 1
except IndexError:
  if (len(binary) - 1) == i):
    print('true')
  else:
    print('false')
