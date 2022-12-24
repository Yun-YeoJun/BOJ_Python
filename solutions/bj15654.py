# import sys
# import itertools
# input = sys.stdin.readline

# n, m = map(int,input().split())

# l = list(map(int,input().split()))

# l.sort()

# result = list(itertools.permutations(l,m))

# for i in result:
#     for j in i:
#         print(j,end=" ")
#     print()

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
numbers = [int(x) for x in input().split()]

numbers.sort()

def backtracking(depth):
    if depth == m:
        print(' '.join(map(str,box)))
        return
    
    for i in range(n):
        if numbers[i] in box:
            continue
        box.append(numbers[i])
        backtracking(depth + 1)
        box.pop()

box = []
backtracking(0)