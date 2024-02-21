"""
Zecookiez's Work

His solution helped me understand how to solve this problem! Thanks!
This is NOT my work.
"""
s1, k1 = input().split()
s2, k2 = input().split()
s3, k3 = input().split()

S, I, F = input().split()
S = int(S)

tested = set()
def DFS(step, current, seq):
    if (step == 0) and (current == F):
        return seq
    
    if (step == 0):
        return False
    
    state = step, current

    if (state in tested):
        return False
    tested.add(state)

    for rule, (lock, key) in enumerate([(s1, k1), (s2, k2), (s3, k3)], 1):
        position = -1
        l = len(lock)
        while True:
            position = current.find(lock, position + 1)

            if (position == -1):
                break

            replaced = current[:position] + key + current[position + l:]
            output = DFS(step - 1, replaced[:], seq + [(rule, position, replaced)])
            
            if output: # Using boolean property of lists
                return output
    return False

for i, j, k in DFS(S, I, []):
    print(i, j + 1, k)
