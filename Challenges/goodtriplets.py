"""
给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。
如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。
* 0 <= i < j < k < arr.length
* |arr[i] - arr[j]| <= a
* |arr[j] - arr[k]| <= b
* |arr[i] - arr[k]| <= c
其中 |x| 表示 x 的绝对值。
返回 好三元组的数量 。
"""
arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
n = len(arr)
g = []

for i in range(n):
  for j in range(i + 1, n):
    for k in range(j + 1, n):
      triplet = (arr[i], arr[j], arr[k])
      if (abs(triplet[0] - triplet[1]) < a and 
        abs(triplet[1] - triplet[2]) < b and
        abs(triplet[0] - triplet[2]) < c):
        g.append(triplet)

*y, = map(list,{*map(tuple,g)})
print(len(y))
