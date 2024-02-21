from itertools import groupby

N = int(input())
msg = []
for _ in range(N):
    msg.append(list(input()))

for i in msg:
    temp = ''
    for j in [''.join(group) for _, group in groupby(i)]:
        temp += str(len(j)) + ' ' + j[0] + ' '
    print(temp.rstrip())