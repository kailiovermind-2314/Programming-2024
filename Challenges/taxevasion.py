"""
农夫约翰的农场上有 N 个山峰，每座山的高度都是整数。在冬天，约翰经常在这些山上举办滑雪训练营。

不幸的是，从明年开始，国家将实行一个关于滑雪场的新税法。

如果滑雪场的最高峰与最低峰的高度差大于17，国家就要收税。

为了避免纳税，约翰决定对这些山峰的高度进行修整。

已知，增加或减少一座山峰 x 单位的高度，需要花费 x^2 的金钱。

约翰只愿意改变整数单位的高度，且每座山峰只能修改一次。

请问，约翰最少需要花费多少钱，才能够使得最高峰与最低峰的高度差不大于17。
"""

n = int(input())
mountains = []
for i in range(n * 2):
    mountains.append(input())
mountains = list(map(int, filter(None, mountains)))
l = min(mountains)
r = max(mountains)
res = float('inf')

while r - l > 1:
    mid = (l + r) // 2  # Use integer division
    tr, tl = mid + 1, mid - 1
    cm, cr, cl = 0, 0, 0
    
    for height in mountains:
        if height < mid:
            cm += (mid - height) ** 2
        elif height > mid + 17:
            cm += (height - mid - 17) ** 2
            
        if height < tl:
            cl += (tl - height) ** 2
        elif height > tl + 17:
            cl += (height - tl - 17) ** 2
            
        if height < tr:
            cr += (tr - height) ** 2
        elif height > tr + 17:
            cr += (height - tr - 17) ** 2
    
    res = min(res, cm, cr, cl)
    if (cm < cr):
        r = mid
    else:
        l = mid

# Final check of remaining candidates
for candidate in [l, r, (l + r) // 2]:
    cost = 0
    for height in mountains:
        if (height < candidate):
            cost += (candidate - height) ** 2
        elif (height > candidate + 17):
            cost += (height - candidate - 17) ** 2
    res = min(res, cost)

print(height - 17, height)
print(int(res)) # Output as integer
