"""
9252. LCS 2
https://www.acmicpc.net/problem/9252
"""

def _LCS_get_path(S1, S2):
    n, m = len(S1), len(S2)
    path = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            if S1[i] == S2[j]:
                path[i+1][j+1] = path[i][j] + 1
            else:
                path[i+1][j+1] = max(path[i+1][j], path[i][j+1])

    return path


def LCS(S1, S2):
    n, m = len(S1), len(S2)
    path = _LCS_get_path(S1, S2)
    solution = []
    print(path[n][m])

    i, j = n, m
    while path[i][j] > 0:
        if S1[i-1] == S2[j-1]:
            solution.append(S1[i-1])
            i -= 1
            j -= 1
        elif path[i-1][j] >= path[i][j-1]:
            i -= 1
        else:
            j -= 1

    result = ''.join(reversed(solution)) if len(solution) > 0 else ''
    return result


if __name__ == '__main__':
    s1 = input()
    s2 = input()

    result = LCS(s1, s2)
    print(result)
