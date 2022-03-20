a, b = map(int, input().split())

c = int(input())

d = b + c

print("%d %d" %((a + d // 60)%24, d%60))
