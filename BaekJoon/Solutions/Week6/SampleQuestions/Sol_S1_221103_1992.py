"""
https://www.acmicpc.net/problem/1992
"""


def merge_solution(B, N, i1=None, i2=None, j1=None, j2=None):
    if i1 is None:
        i1, i2 = 0, N-1
        j1, j2 = 0, N-1
    if N == 1:
        # print('At {} {}, val : {}'.format(i1, j1, B[i1][j1]))
        return B[i1][j1]

    imid = (i1+i2)//2
    jmid = (j1+j2)//2
    P1 = merge_solution(B, N//2, i1, imid, j1, jmid)
    P2 = merge_solution(B, N//2, i1, imid, jmid+1, j2)
    P3 = merge_solution(B, N//2, imid+1, i2, j1, jmid)
    P4 = merge_solution(B, N//2, imid+1, i2, jmid+1, j2)

    if len(P1) == 1 and P1 == P2 == P3 == P4:
        return P1
    else:
        result = ['(']
        result.append(P1)
        result.append(P2)
        result.append(P3)
        result.append(P4)
        result.append(')')
        return ''.join(result)


if __name__ == '__main__':
    N = int(input())
    board = [input() for _ in range(N)]

    # print(board)
    result = merge_solution(board, N)
    print(result)