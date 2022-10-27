"""
https://www.acmicpc.net/problem/11277
"""


def loop_sol(N, C):
    for i in range(1<<(N+1)):
        true_flag = True
        for j in range(len(C)):
            sign_zero = 1 if i & (1<<abs(C[j][0])) else -1
            sign_one = 1 if i & (1<<abs(C[j][1])) else -1
            if sign_zero * C[j][0] < 0 and sign_one * C[j][1] < 0:
                true_flag = False
                break

        if true_flag:
            return True

    return False


if __name__ == '__main__':
    N, M = map(int, input().split())
    clauses = []

    for i in range(M):
        clauses.append(list(map(int, input().split())))

    if loop_sol(N, clauses):
        print(1)
    else:
        print(0)