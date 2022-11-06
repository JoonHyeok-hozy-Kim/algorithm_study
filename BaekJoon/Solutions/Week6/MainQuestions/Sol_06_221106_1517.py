"""
https://www.acmicpc.net/problem/1517
"""


def binary_search(C, n):
    start, end = 0, len(C)-1
    while end >= start:
        mid = (start + end) // 2
        if C[mid][0] >= n:
            end = mid - 1
        else:
            start = mid + 1
    return start


if __name__ == '__main__':
    N = int(input())
    L = []
    result = 0
    for i in map(int, input().split()):
        if len(L) == 0:
            L.append([i, 1])
        else:
            if i > L[-1][0]:
                for j in L:
                    j[1] += 1
                L.append([i, 1])
            else:
                target_idx = binary_search(L, i)
                if L[target_idx][0] == i:
                    result += L[target_idx][1]
                    L[target_idx][1] += 1
                else:
                    result += L[target_idx+1][1]
                    L.insert(target_idx, [i, L[target_idx+1][1]+1])
        print(result, L)

    print(result)


"""
5
1 2 1 3 2
"""
