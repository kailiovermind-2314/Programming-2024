"""
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
请你计算并返回达到楼梯顶部的最低花费。

I see this question too many times... if you memorize the cost to access the previous two and choose
the path that costs the least, you will have an easy answer.
"""
def mincost(cost, goal):
  temp1 = 0
  temp2 = 0
  
  for i in range(goal):
    # Most current optimal cost (what it takes to get there)
    temp0 = cost[i] + min(temp1, temp2)
    print(temp0)

    # Check the past 2 stairs and check for minimum cost
    # Only the past 2 are required because it goes a max of 2 up at a time
    temp2 = temp1
    temp1 = temp0
    print(temp1, temp2)

  # Reaching the top of the stairs, determine the minimum cost to get to the top
  return min(temp1, temp2)

fees = eval(input())
n = len(fees)

print(mincost(fees, n))
