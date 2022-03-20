from sys import stdin

n = int(stdin.readline())

for i in range(n):
    l1 = stdin.readline().rstrip()
    l2 = stdin.readline().rstrip()

    result1 = [0 for j in range(26)]
    result2 = [0 for j in range(26)]
    result = 0
    for j in list(l1):
        result1[ord(j) - 97] += 1
    for j in list(l2):
        result2[ord(j) - 97] += 1

    for j in range(26):
        result += abs(result1[j] - result2[j])

    print('Case #%d: %d' % (i + 1, result))