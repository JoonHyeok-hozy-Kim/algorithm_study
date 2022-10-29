"""
https://www.acmicpc.net/problem/1932
"""


if __name__ == "__main__":
    N = int(input())
    tree = [list(map(int, input().split())) for _ in range(N)]
    # print(tree)

    for i in range(N-1):
        for j in range(len(tree[N-2-i])):
            tree[N - 2 - i][j] = tree[N - 2 - i][j] + max(tree[N - 1 - i][j], tree[N - 1 - i][j+1])
        # print(tree)

    print(tree[0][0])