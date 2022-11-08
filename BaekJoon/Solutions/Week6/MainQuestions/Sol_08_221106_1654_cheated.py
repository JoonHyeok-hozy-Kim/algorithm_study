"""
https://www.acmicpc.net/problem/1654
"""


if __name__ == '__main__':
    K, N = map(int, input().split())
    max_val = None
    lines = [None] * K
    for i in range(K):
        lines[i] = int(input())
        max_val = max(max_val, lines[i]) if max_val is not None else lines[i]
    # print(max_val, lines)

    low, high = 1, max(lines)
    result = None
    while low <= high:
        mid = (low + high) // 2

        temp = 0
        for i in range(K):
            temp += lines[i] // mid
            if temp >= N:
                break
        if temp >= N:
            if result is None or result < mid:
                result = mid
            low = mid + 1
        else:
            high = mid - 1

    print(result)
