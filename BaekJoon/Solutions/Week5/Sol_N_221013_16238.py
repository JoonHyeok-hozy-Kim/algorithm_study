"""
16238. 독수리
https://www.acmicpc.net/problem/16238
"""


if __name__ == '__main__':
    N = int(input())
    field = []
    cnt = 0
    for i in map(int, input().split()):
        field.append([i, cnt])
        cnt += 1
    print(field)

    N-1