"""
给你一个整数数组 nums ，该数组具有以下属性：
* nums.length == 2 * n.
* nums 包含 n + 1 个 不同的 元素
* nums 中恰有一个元素重复 n 次
找出并返回重复了 n 次的那个元素。
"""
nums = [5,1,5,2,5,3,5,4]
for i in set(nums):
  if nums.count(i) == len(set(nums)) - 1:
    print(i)
