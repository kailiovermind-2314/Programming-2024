"""
给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。
更正式地，检查是否存在两个下标 i 和 j 满足：
* i != j
* 0 <= i, j < arr.length
* arr[i] == 2 * arr[j]
"""
arr = [3, 1, 7, 11]

print(any((i / 2) in arr for i in arr))
