"""
3078. 좋은 친구

https://www.acmicpc.net/problem/3078
"""
from collections import deque

if __name__ == '__main__':
    N, K = map(int, input().split())
    students = deque()
    group = deque()
    result = 0
    for i in range(N):
        students.append(len(input()))

    first = students.popleft()
    for i in range(K):
        if len(students) == 0:
            break
        group.append(students.popleft())

    while len(group) > 0:
        for student in group:
            if first == student:
                result += 1
        first = group.popleft()
        if len(students) > 0:
            group.append(students.popleft())


    print(result)