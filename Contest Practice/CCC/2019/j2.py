N = int(input())
code = []
for i in range(N):
    c, s = input().split()
    code.append((s, int(c)))

for j in code:
    print(j[0] * j[1])