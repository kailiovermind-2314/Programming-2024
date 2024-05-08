"""
给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。
请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。
请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。
"""
s = list(input())
nums = [c for c in s if c.isdigit()]
strs = [c for c in s if c.isalpha()]

def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    return([l1[0], l2[0]] + merge(l1[1:], l2[1:]))

n = len(strs) - len(nums)
if (abs(n) > 1):
    print('')
    exit()
elif (n == 1 or n == 0):
    print(''.join(merge(strs, nums)))
elif (n == -1):
    print(''.join(merge(nums, strs)))
