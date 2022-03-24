from sys import stdin

n = int(stdin.readline())

l1 = []
l2 = []

def a(n, l1):
    for j in range(n):
        for i in range(n):
            l1.append("@")
        for i in range(n * 3):
            l1.append(" ")
        for i in range(n):
            l1.append("@")
        l1.append("\n")
def b(n, l2):
    for i in range(n):
        for j in range(n * 5):
            l2.append("@")
        l2.append("\n")

a(n, l1)
b(n, l2)

l1 = ''.join(_ for _ in l1)
l2 = ''.join(_ for _ in l2)

print(l1+l2+l1+l2+l1)