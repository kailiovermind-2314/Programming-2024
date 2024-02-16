N = int(input())
avalibility = []
for i in range(N):
    avalibility.append(list(input()))

avalibility = list(map(list, zip(*avalibility)))
answer = ""
best = max([day.count('Y') for day in avalibility])
for i, day in enumerate(avalibility, 1):
    if day.count('Y') == best:
        answer += (str(i) + ',')
print(answer.removesuffix(','))