from sys import stdin

n = int(stdin.readline()) # number of stairs

l = [0] * n # score of each stair

for i in range(n):
    l[i] = int(stdin.readline())

result = [-1] * (n) # reset to -1
cnt = [0] * (n)
cur = 0

l = list(reversed(l))

result[0] = l[0] + l[1]
result[1] = l[0] + l[2]

cnt[0] += 1

for i in range(2, n-1):
    tcnt = cnt[i - 1]
    r1 = result[i - 1]
    r2 = result[i - 2]
    if tcnt == 1:
        result[i] = r2 + l[i + 1]
    elif r1 > r2:
        result[i] = r1 + l[i + 1]
        cnt[i] = cnt[i - 1] + 1
    elif r1 < r2:
        result[i] = r2 + l[i + 1]
    else:
        result[i] = r2 + l[i + 1]

print(result[n-1])