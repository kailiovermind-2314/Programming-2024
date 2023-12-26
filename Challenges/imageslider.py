"""
图像平滑器是大小为 3 x 3 的过滤器，用于对图像的每个单元格平滑处理，平滑处理后单元格的值为该单元格的平均灰度。
每个单元格的  平均灰度 定义为：该单元格自身及其周围的 8 个单元格的平均值，结果需向下取整。（即，需要计算蓝色平滑器中 9 个单元格的平均值）。
对于位于边缘的像素，则计算平均灰度时不考虑缺失的单元格，只计算有效单元格平均即可。

This is not a very good solution. It is lengthy and repetitive. My "goofy ahh" was too lazy to find a better method.
However, this is the most obvious solution, and it works for all array sizes. Please raise an issue if you find a
better solution.
"""

import math

imagemap = eval(input())

vbound = len(imagemap)
hbound = len(imagemap[0])

def inBounds(i, j):
  if (i >= 0 and i < vbound) and (j >= 0 and j < hbound):
    return True
  else:
    return False

def averageSlider(imageArray):
  for i in range(vbound):
    for j in range(hbound):
      counter = []
      if inBounds(i, j): # Origin
        counter.append(imageArray[i][j])
      if inBounds(i - 1, j): # Up
        counter.append(imageArray[i - 1][j])
      if inBounds(i + 1, j): # Down
        counter.append(imageArray[i + 1][j])
      if inBounds(i, j - 1): # Left
        counter.append(imageArray[i][j - 1])
      if inBounds(i, j + 1): # Right
        counter.append(imageArray[i][j + 1])
      if inBounds(i - 1, j - 1): # Upleft
        counter.append(imageArray[i - 1][j - 1])
      if inBounds(i - 1, j + 1): # Upright
        counter.append(imageArray[i - 1][j + 1])
      if inBounds(i + 1, j - 1): # Downleft
        counter.append(imageArray[i + 1][j - 1])
      if inBounds(i + 1, j + 1): # Downright
        counter.append(imageArray[i + 1][j + 1])

      imageArray[i][j] = math.floor(sum(counter) / len(counter))
  return imageArray

print(averageSlider(imagemap))
