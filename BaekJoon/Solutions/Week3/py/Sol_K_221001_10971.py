"""
10971. 외판원 순회 2
https://www.acmicpc.net/problem/10971
"""
from collections import deque

def accessible(C, dept, dest):
    if dept == dest:
        return False
    if C[dept][dest] == 0:
        return False
    return True


def recursive_travel(N, C, J=None, cnt=0, cost=0, destinations=None):
    # print('In recursive_travel, cnt : {}, J : {}, cost : {}'.format(cnt, J, cost))

    if cnt == 0:
        J = [None] * N
        destinations = deque([i for i in range(N)])

    if cnt == N:
        if accessible(C, J[-1], J[0]):
            # print('-> Done. cost : {}'.format(cost + C[J[-1]][J[0]]))
            return True, cost + C[J[-1]][J[0]]
        else:
            return False, cost

    min_cost = None
    len_dest = len(destinations)
    for k in range(len_dest):
        d = destinations.popleft()
        if cnt == 0 or accessible(C, J[cnt-1], d):
            J[cnt] = d
            copy_cost = cost
            if cnt > 0:
                copy_cost += C[J[cnt-1]][d]
            go_on, temp_cost = recursive_travel(N, C, J, cnt+1, copy_cost, destinations)
            if go_on:
                min_cost = min(min_cost, temp_cost) if min_cost is not None else temp_cost
            J[cnt] = None
        destinations.append(d)

    if min_cost is not None:
        return True, min_cost
    else:
        return False, cost



if __name__ == '__main__':
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    # print(costs)

    finale, cost = recursive_travel(N, costs)
    print(cost)
