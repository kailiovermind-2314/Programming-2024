"""
给你个整数数组 arr，其中每个元素都 不相同。
请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
每对元素对 [a,b] 如下：
* a , b 均为数组 arr 中的元素
* a < b
* b - a 等于 arr 中任意两个元素的最小绝对差
"""

arr = [4, 2, 1, 3]
l = len(arr)
ans = [] * l

n = float('inf')
for _ in range(l - 1):
    d = abs(arr[_ + 1] - arr[_])
    if d < n:
        n = d
d = 0
for i in range(l - 1):
  for j in range(i, l):
    if abs(arr[j] - arr[i]) == n:
      ans.append([arr[i], arr[j]])
      d += 1

print(sorted(ans))
