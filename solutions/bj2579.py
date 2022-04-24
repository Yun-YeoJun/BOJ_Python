from sys import stdin

n = int(stdin.readline())

score = [0] * n

for i in range(n):
    score[i] = int(stdin.readline())

result = [[-1 for i in range(2)] for j in range(n+1)]

if n >= 3:
    for i in range(2):
        result[n][i] = score[n - 1]
        result[n - 1][i] = score[n - 2] + result[n][0]
        result[n - 2][i] = score[n - 3] + result[n][0]

    def maxScoreSum(result, k, tf):
        if result[k] == [-1,-1]:
            if k > 0:
                result[k][0] = max(maxScoreSum(result, k + 1, 1),maxScoreSum(result, k + 2, 0)) + score[k - 1]
                result[k][1] = maxScoreSum(result, k + 2, 0) + score[k - 1]
                return result[k][tf]
            else:
                result[k] = max(maxScoreSum(result, k + 1, 0),maxScoreSum(result, k + 2, 0))
                return result[k]
        else:
            if tf == 0:
                return max(result[k][0], result[k][1])
            else:
                return result[k][1]

    maxScoreSum(result, 0, 0)

    print(result[0])

else:
    print(sum(score))