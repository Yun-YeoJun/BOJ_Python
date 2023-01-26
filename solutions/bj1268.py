import sys
input = sys.stdin.readline

n = int(input())

class_info = [[] for i in range(n)]

for i in range(n):
    class_info[i] = list(map(int,input().split()))

student_info_of_same_class = [[] for i in range(n)]

num_of_same_class = [0 for i in range(n)]

for i in range(5):
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if class_info[j][i] == class_info[k][i]:
                if k in student_info_of_same_class[j] or j in student_info_of_same_class[k]:
                    continue
                else:
                    student_info_of_same_class[j].append(k)
                    student_info_of_same_class[k].append(j)
                    num_of_same_class[j] += 1
                    num_of_same_class[k] += 1


print(num_of_same_class.index(max(num_of_same_class)) + 1)
