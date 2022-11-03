"""
https://www.acmicpc.net/problem/2098
"""


def dfs(R, x, visited):
    if visited == (1 << len(R)) -1:
        return






if __name__ == '__main__':
    N = int(input())
    routes = [list(map(int, input().split())) for _ in range(N)]
    # print(routes)

