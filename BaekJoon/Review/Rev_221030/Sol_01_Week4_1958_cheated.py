"""
https://www.acmicpc.net/problem/1958
"""


def LCS(X, Y):
    n, m = len(X), len(Y)
    l = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            if X[i] == Y[j]:
                l[i+1][j+1] = l[i][j] + 1
            else:
                l[i+1][j+1] = max(l[i+1][j], l[i][j+1])

    # for i in range(n):
    #     print(*l[i], sep=" ")

    return l


def LCS_solution(X, Y):
    l = LCS(X, Y)
    j, k = len(X), len(Y)
    solution = []

    while l[j][k] > 0:
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif l[j-1][k] > l[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(solution)


def LCS3(X, Y, Z):
    n, m, l = len(X), len(Y), len(Z)
    L = [[[0] * (l+1) for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            for k in range(l):
                if X[i] == Y[j] == Z[k]:
                    L[i+1][j+1][k+1] = L[i][j][k] + 1
                else:
                    L[i + 1][j + 1][k + 1] = max(L[i+1][j][k],
                                                 L[i][j+1][k],
                                                 L[i][j][k+1],
                                                 L[i+1][j+1][k],
                                                 L[i][j+1][k+1],
                                                 L[i+1][j][k+1],)

    # for i in range(n):
    #     for j in range(m):
    #         print(*L[i][j], sep=" ")
    #     print()


    return L


def LCS3_solution(X, Y, Z):
    i, j, k = len(X), len(Y), len(Z)
    L = LCS3(X, Y, Z)
    solution = []

    while L[i][j][k] > 0:
        if X[i-1] == Y[j-1] == Z[k-1]:
            solution.append(X[i-1])
            i -= 1
            j -= 1
            k -= 1
        elif L[i-1][j][k] == max(L[i-1][j-1][k],
                                 L[i-1][j][k-1],
                                 L[i][j-1][k-1],
                                 L[i][j-1][k],
                                 L[i][j][k-1],
                                 L[i-1][j][k]):
            i -= 1
        elif L[i][j-1][k] == max(L[i-1][j-1][k],
                                 L[i-1][j][k-1],
                                 L[i][j-1][k-1],
                                 L[i][j-1][k],
                                 L[i][j][k-1],
                                 L[i-1][j][k]):
            j -= 1
        else:
            k -= 1

    return ''.join(reversed(solution))



if __name__ == '__main__':
    texts = [input() for _ in range(3)]
    # print(texts)

    result = LCS3_solution(texts[0], texts[1], texts[2])
    # print(result)
    print(len(result))
