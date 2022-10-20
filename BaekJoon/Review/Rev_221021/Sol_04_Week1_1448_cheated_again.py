"""
https://www.acmicpc.net/problem/1448
"""


def greedy_sol(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if j+1 < len(L) and L[i] < L[j] + L[j+1]:
                return L[i] + L[j] + L[j+1]
    return -1


if __name__ == '__main__':
    N = int(input())
    lines = [int(input()) for _ in range(N)]
    # print(lines)

    lines.sort(reverse=True)

    print(greedy_sol(lines))
