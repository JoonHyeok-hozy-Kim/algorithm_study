"""
16238. 독수리
https://www.acmicpc.net/problem/16238
"""


if __name__ == '__main__':
    N = int(input())
    field = list(map(int, input().split()))
    result = 0

    for i in range(N):
        max_val = max(field)
        max_idx = field.index(max_val)
        result += max(max_val - i, 0)
        field[max_idx] = 0

    print(result)