"""
https://www.acmicpc.net/problem/2210
"""


def generate_map(B, M, i, j, depth=0):
    if depth == 6:
        return

    target = B[i][j]
    if target not in M:
        M[target] = {}

    if i > 0:
        generate_map(B, M[target], i-1, j, depth+1)
    if j > 0:
        generate_map(B, M[target], i, j-1, depth+1)
    if i < 4:
        generate_map(B, M[target], i+1, j, depth+1)
    if j < 4:
        generate_map(B, M[target], i, j+1, depth+1)


def count_nums_from_map(M):
    if len(M) == 0:
        return 1

    cnt = 0
    for n in M:
        cnt += count_nums_from_map(M[n])

    return cnt


if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(5)]
    num_map = {}

    for i in range(5):
        for j in range(5):
            generate_map(board, num_map, i, j)
            # print(num_map)

    result = count_nums_from_map(num_map)
    print(result)