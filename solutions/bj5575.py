from sys import stdin

a_start_h, a_start_m, a_start_s, a_finish_h, a_finish_m, a_finish_s = map(int, stdin.readline().split())
b_start_h, b_start_m, b_start_s, b_finish_h, b_finish_m, b_finish_s = map(int, stdin.readline().split())
c_start_h, c_start_m, c_start_s, c_finish_h, c_finish_m, c_finish_s = map(int, stdin.readline().split())

a_start = 3600 * a_start_h + 60 * a_start_m + a_start_s
b_start = 3600 * b_start_h + 60 * b_start_m + b_start_s
c_start = 3600 * c_start_h + 60 * c_start_m + c_start_s

a_finish = 3600 * a_finish_h + 60 * a_finish_m + a_finish_s
b_finish = 3600 * b_finish_h + 60 * b_finish_m + b_finish_s
c_finish = 3600 * c_finish_h + 60 * c_finish_m + c_finish_s

a_sec = a_finish - a_start
b_sec = b_finish - b_start
c_sec = c_finish - c_start

a_result_h = a_sec // 3600
a_sec = a_sec % 3600
a_result_m = a_sec // 60
a_sec = a_sec % 60
a_result_s = a_sec

print(a_result_h, a_result_m, a_result_s)

b_result_h = b_sec // 3600
b_sec = b_sec % 3600
b_result_m = b_sec // 60
b_sec = b_sec % 60
b_result_s = b_sec

print(b_result_h, b_result_m, b_result_s)

c_result_h = c_sec // 3600
c_sec = c_sec % 3600
c_result_m = c_sec // 60
c_sec = c_sec % 60
c_result_s = c_sec

print(c_result_h, c_result_m, c_result_s)