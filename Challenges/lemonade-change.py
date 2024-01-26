"""
下午好同学们，今天以题会友开始啦， 题目如下：
【练习题 柠檬水找零】

在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
"""

bills = [5, 5, 5, 5, 5]
total = []

for bill in bills:
  if bill == 5:
    total.append(bill)
  else:
    valid_change = next((x for x in total if x <= bill - 5 and (bill - 5) % x == 0), None)
    if valid_change is not None:
      total.remove(valid_change)
      total.append(bill)
    else:
      print("false")
      exit()
print("true")
