"""
给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。
你从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。
如果路径在任何位置上与自身相交，也就是走到之前已经走过的位置，请返回 true ；否则，返回 false 。
"""
path = "NESWW"
paths = []

x = 0
y = 0
for i in path:
  paths.append((x, y))
  if (i == "N"):
    y += 1
  elif (i == "S"):
    y -= 1
  elif (i == "E"):
    x += 1
  elif (i == "W"):
    x -= 1
  if (x, y) in paths:
    print(True)
    exit()
print(False)
