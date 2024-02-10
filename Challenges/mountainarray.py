"""
给定一个整数数组 arr，如果它是有效的山脉数组就返回 true，否则返回 false。
让我们回顾一下，如果 arr 满足下述条件，那么它是一个山脉数组：
* arr.length >= 3
* 在 0 < i < arr.length - 1 条件下，存在 i 使得：
    * arr[0] < arr[1] < ... arr[i-1] < arr[i] 
    * arr[i] > arr[i+1] > ... > arr[arr.length - 1]
"""
import numpy
arr = eval(input())
asc = arr[:arr.index(max(arr))]
des = arr[arr.index(max(arr)):]
print(True if numpy.all(numpy.diff(numpy.array(asc)) > 0) and numpy.all(numpy.diff(numpy.array(des)) < 0) and (len(arr) >= 3) else False)
