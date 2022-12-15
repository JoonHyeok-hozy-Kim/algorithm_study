"""
https://www.acmicpc.net/problem/9694
"""
from heapq import heappop, heappush
from copy import deepcopy


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, M = map(int, input().split())
        politicians = [None] * M
        for _ in range(N):
            x, y, z = map(int, input().split())

            if politicians[x] is None:
                politicians[x] = {}
            politicians[x][y] = z

            if politicians[y] is None:
                politicians[y] = {}
            politicians[y][x] = z

        acquainted = [None] * M
        acquainted[0] = 0
        heap = []
        heappush(heap, (0, 0, [0]))
        min_score = None
        min_line = []
        while heap:
            popped_score, popped, popped_line = heappop(heap)
            if popped == M-1:
                if min_score is None or min_score > popped_score:
                    min_score = popped_score
                    min_line = popped_line

            if min_score is None or min_score > popped_score:
                if politicians[popped] is not None:
                    for linked in politicians[popped]:
                        additional_score = politicians[popped][linked]
                        if min_score is None or min_score >= popped_score + additional_score:
                            if acquainted[linked] is None or acquainted[linked] > popped_score + additional_score:
                                new_line = deepcopy(popped_line)
                                new_line.append(linked)
                                acquainted[linked] = popped_score + additional_score
                                heappush(heap, (popped_score + additional_score, linked, new_line))

        print('Case #{}:'.format(t+1), end=" ")
        if min_score is None:
            print(-1)
        else:
            print(*min_line, sep=" ")