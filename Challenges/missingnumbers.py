"""
给你一个 严格升序排列 的正整数数组 arr 和一个整数 k 。
请你找到这个数组里第 k 个缺失的正整数。
"""
arr = [100, 101, 102]
k = 104

i = 0
while (k > 0):
  if (i not in arr):
    k -= 1
    print(k)
  i += 1
print(i)
