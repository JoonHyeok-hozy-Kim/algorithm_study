"""
https://www.acmicpc.net/problem/10971
"""


def dfs(C, journey=[], total_cost=None):
    if len(journey) == len(C):
        if C[journey[-1]][journey[0]] != 0:
            # print('LAST JOURNEY HOME, journey : {}, total_cost : {}'.format(journey, total_cost + C[journey[-1]][journey[0]]))
            return True, total_cost + C[journey[-1]][journey[0]]
        else:
            return False, None

    temp_min = None
    if len(journey) == 0:
        for i in range(len(C)):
            go_on, temp_cost = dfs(C, [i], 0)
            if go_on:
                # print('FIRST, temp_cost : {}'.format(temp_cost))
                temp_min = min(temp_min, temp_cost) if temp_min is not None else temp_cost
        # print('FIRST FINAL : {}'.format(temp_min))

    else:
        for i in range(len(C)):
            if i not in journey and C[journey[-1]][i] != 0:
                total_cost += C[journey[-1]][i]
                journey.append(i)
                go_on, temp_cost = dfs(C, journey, total_cost)
                if go_on:
                    # print('DURING, journey : {}, temp_cost : {}'.format(journey, temp_cost))
                    temp_min = min(temp_min, temp_cost) if temp_min is not None else temp_cost
                journey.pop()
                total_cost -= C[journey[-1]][i]

    if temp_min is None:
        return False, None
    else:
        return True, temp_min


if __name__ == '__main__':
    N = int(input())
    cities = [list(map(int, input().split())) for _ in range(N)]

    finale, result = dfs(cities)
    if finale:
        print(result)