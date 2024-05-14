"""
给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。
"""
nums = ''.join(map(str, eval(input())))
k = int(input())
d = 0

for i in filter(None, list(nums.split('1'))):
  if (len(i) < k):
    print(False)
    exit()
print(True)
