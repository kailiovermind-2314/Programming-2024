N = int(input())
road = []
for _ in range(2):
    road.append(list(map(int, input().split())))

counter1 = 0
counteradj = 0
for i in range(2):
    for j in range(N):
        if (road[i][j] == 1):
            counter1 += 1
            # Check right
            if (j + 1 < N and road[i][j + 1] == 1):
                counteradj += 1
            # Check down
            if (i + 1 < 2 and road[i + 1][j] == 1 and j % 2 == 0):
                counteradj += 1

# My very special algorithm
print(counter1 * 3 - counteradj * 2)
