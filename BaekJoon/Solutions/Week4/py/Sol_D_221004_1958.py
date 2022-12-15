"""
1958. LCS 3
https://www.acmicpc.net/problem/1958
"""

def LCS2(X, Y):
    n, m = len(X), len(Y)
    L = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                L[i+1][j+1] = 1 + L[i][j]
            else:
                L[i+1][j+1] = max(L[i+1][j], L[i][j+1])

    return L


def LCS2_get_result(X, Y):
    solution = []
    i, j = len(X), len(Y)
    L = LCS2(X, Y)
    while L[i][j] > 0:
        if X[i-1] == Y[j-1]:
            solution.append(X[i-1])
            i -= 1
            j -= 1
        elif L[i-1][j] >= L[i][j-1]:
            i -= 1
        else:
            j -= 1
    # print(solution)
    return ''.join(reversed(solution))



def LCS3(X, Y, Z):
    n, m, l = len(X), len(Y), len(Z)
    L = [[[0]*(l+1) for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            for k in range(l):
                if X[i] == Y[j] == Z[k]:
                    L[i+1][j+1][k+1] = 1 + L[i][j][k]
                else:
                    L[i+1][j+1][k+1] = max(L[i+1][j][k],
                                           L[i][j+1][k],
                                           L[i][j][k+1],
                                           L[i][j+1][k+1],
                                           L[i+1][j][k+1],
                                           L[i+1][j+1][k])

    return L


# def LCS_solution(X, Y, Z):
#     solution = []
#     i, j, k = len(X), len(Y), len(Z)
#     L = LCS(X, Y, Z)
#     while L[i][j][k] > 0:
#         if X[i-1] == Y[j-1]:



if __name__ == '__main__':
    X = input()
    Y = input()
    Z = input()

    # L = LCS2(X, Y)
    # for i in range(len(L)):
    #     print(*L[i], sep=" ")
    # result = LCS2_get_result(X, Y)
    # print(result)


    L = LCS3(X, Y, Z)
    # for i in range(len(L)):
    #     print('========')
    #     for j in range(len(L[i])):
    #         print(*L[i][j], sep=" ")
    #     print('========')

    result = None
    for i in range(len(L)):
        for j in range(len(L[i])):
            result = max(result, max(L[i][j])) if result is not None else max(L[i][j])

    print(result)
