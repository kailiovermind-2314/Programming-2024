"""
给你一个整数数组 nums ，其中总是存在 唯一的 一个最大整数 。
请你找出数组中的最大元素并检查它是否 至少是数组中每个其他数字的两倍 。如果是，则返回 最大元素的下标 ，否则返回 -1 。

这道题简直是一个玩笑。只需要检查最大数是不是第二最大数的两倍
This question is an absolute joke. You only have to check if the largest number is larger than the 
second-largest number multiplied by 2.
"""
nums = eval(input())
print(nums.index(max(nums))) if (max(nums) >= sorted(nums)[-2] * 2) else print(-1)
