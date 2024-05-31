"""
给你一个数字数组 arr 。
如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。
如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 
"""
arr = [3, 5, 1]
arr.sort()
print(all((arr[i + 1] - arr[i]) == (arr[1] - arr[0]) for i in range(len(arr) - 1)))
