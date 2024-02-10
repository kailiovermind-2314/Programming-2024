import numpy

arr = eval(input())
asc = arr[:arr.index(max(arr))]
des = arr[arr.index(max(arr)):]
print(True if numpy.all(numpy.diff(numpy.array(asc)) > 0) and numpy.all(numpy.diff(numpy.array(des)) < 0) and (len(arr) >= 3) else False)
