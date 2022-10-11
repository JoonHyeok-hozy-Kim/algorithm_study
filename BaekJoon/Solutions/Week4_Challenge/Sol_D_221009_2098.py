"""
2098. 외판원 순회
https://www.acmicpc.net/problem/2098
"""
from itertools import permutations


def travel(C, i, j):
    return C[i][j]


def simple_solution(C, N):
    min_total_cost = None
    for route in permutations([i for i in range(N)]):
        total_cost = 0
        for j in range(N):
            total_cost += travel(C, route[j], route[(j+1)%N])
        min_total_cost = min(min_total_cost, total_cost) if min_total_cost is not None else total_cost
    return min_total_cost


if __name__ == '__main__':
    N = int(input())
    cost_graph = [list(map(int, input().split())) for _ in range(N)]
    # print(cost_graph)

    print(simple_solution(cost_graph, N))

