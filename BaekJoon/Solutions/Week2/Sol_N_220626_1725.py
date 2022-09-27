"""
1725. 히스토그램
https://www.acmicpc.net/problem/1725
"""
from collections import deque

if __name__ == '__main__':
    result_list = deque()
    N = int(input())
    num = int(input())
    result_list.append([num, 1])
    max_size = 0
    for _ in range(N-1):
        num = int(input())
        for _ in range(len(result_list)):
            s = result_list.popleft()
            if s[0] > num:
                max_size = max(max_size, s[0]*s[1])
            else:
                s[1] += 1
                result_list.append(s)
            print(max_size, result_list)
        result_list.append([num, 1])
        print(max_size, result_list)
    while len(result_list) > 0:
        s = result_list.popleft()
        max_size = max(max_size, s[0] * s[1])
    print(max_size)


