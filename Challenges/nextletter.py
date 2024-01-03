"""
给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。
返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。

This question is too easy.
"""
target = input()
letters = input().split(' ')

key = [c for c in letters if ord(c) >= ord(target)]
print(sorted(key)[0] if key else letters[0])
