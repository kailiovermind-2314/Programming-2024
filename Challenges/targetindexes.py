"""
It's asking for two numbers in a list that add up to a target total.
"""
import numpy as np

def targetnumbers(arr, target):
  targetindex = []
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      if ((target - arr[i]) == arr[j]) and arr[i] != arr[j]:
        targetindex.append([i, j])
  return targetindex

print(np.matrix(targetnumbers([2, 7, 3, 6], 9)))
