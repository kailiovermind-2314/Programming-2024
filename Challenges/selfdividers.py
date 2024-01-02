"""
自除数 是指可以被它包含的每一位数整除的数。
例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
自除数 不允许包含 0 。
给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数 。

Easy problem and easy solution.
"""
left = 1
right = 22

selfdividers = []
for i in range(left, right + 1):
    c = 0
    for digit in list(map(int, str(i))):
        try:
            if ((i % digit) == 0):
                c += 1
        except ZeroDivisionError:
            break
    if c == len(str(i)):
        selfdividers.append(i)
       
print(selfdividers)
