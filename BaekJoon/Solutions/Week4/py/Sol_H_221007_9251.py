"""
9251. LCS
https://www.acmicpc.net/problem/9251
"""


if __name__ == '__main__':
    S1 = input()
    S2 = input()

    l, m = len(S1), len(S2)
    path = [[0] * (m+1) for _ in range(l+1)]

    for i in range(l):
        for j in range(m):
            if S1[i] == S2[j]:
                path[i+1][j+1] = path[i][j] + 1
            else:
                path[i+1][j+1] = max(path[i+1][j], path[i][j+1])

    print(path[l][m])
    # i, j = l, m
    # result = []
    # while path[i][j] > 0:
    #     if S1[i-1] == S2[j-1]:
    #         result.append(S1[i-1])
    #         i -= 1
    #         j -= 1
    #     elif path[i-1][j] >= path[i][j-1]:
    #         i -= 1
    #     else:
    #         j -= 1
    # print(''.join(reversed(result)))