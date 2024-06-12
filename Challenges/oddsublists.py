"""
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。
子数组 定义为原数组中的一个连续子序列。
请你返回 arr 中 所有奇数长度子数组的和 。
"""
arr = [1, 4, 6, 9, 3, 4, 5, 7, 8, 2]
n = len(arr)
s = 0

for i in range(n):
  c = i
  while (c < n):
    print(arr[i : c + 1])
    s += sum(arr[i : c + 1])
    c += 2
print(s)
