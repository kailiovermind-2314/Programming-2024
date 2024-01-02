"""
There is a squad of n people, each with a weight, attempting to cross a river. 
There is one boat with a maximum weight limit. What is the least number of times 
the boat has to cross the river so the people all get across the river?

The algorithm works like this.

1. Select a substring made of the smallest numbers that get as close as possible to the limit.
2. Bring that substring over to the other side.
3. Bring the smallest weight back to the first side.
4. Repeat.

This solution does not work perfectly yet. The knapsack algorithm is not optimal for selecting the substring.
This solution only works if there is a small-weight substring that perfectly adds to 80. (eg. 20, 30, 30, 70, 80)

Credits to StackOverFlow for teaching me how to subtract a list from another using collections. Credits to a
friend of mine at UofW for helping me implement the modified knapsack algorithm.
"""
from collections import Counter

# For selecting the substring we use the knapsack algorithm
def knapsack(weights, limit):
  n = len(weights)
  dp = [[0] * (limit + 1) for _ in range(n + 1)]

  for i in range(1, n + 1):
    for w in range(limit + 1):
      if weights[i - 1] > w:
        dp[i][w] = dp[i - 1][w]
      else:
        dp[i][w] = max(dp[i - 1][w], weights[i - 1] + dp[i - 1][w - weights[i - 1]])

  # Backtrack to find the selected weights
  selected_weights = []
  i, w = n, limit
  while (i > 0 and w > 0):
    if dp[i][w] != dp[i - 1][w]:
      selected_weights.append(weights[i - 1])
      w -= weights[i - 1]
    i -= 1

  return selected_weights

side1 = [20, 30, 30, 70, 80]
side2 = []
limit = 80
counter = 0

while True:
  key = knapsack(side1, limit)
  side1 = list((Counter(side1) - Counter(key)).elements())
  side2.extend(key)

  counter += 1

  if len(side1) == 0:
    break

  key = min(side2)
  side2.remove(key)
  side1.append(key)

  counter += 1

print(counter)
