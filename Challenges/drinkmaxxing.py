"""
超市正在促销，你可以用 numExchange 个空水瓶从超市兑换一瓶水。最开始，你一共购入了 numBottles 瓶水。
如果喝掉了水瓶中的水，那么水瓶就会变成空的。
给你两个整数 numBottles 和 numExchange ，返回你 最多 可以喝到多少瓶水。
"""
numBottles = 15
numExchange = 4

def drinkmaxx(n, m):
  if (n < m):
    return n
    
  new = n // m
  remaining = n % m
  return n - remaining + drinkmaxx(new + remaining, m)

print(drinkmaxx(numBottles, numExchange))
