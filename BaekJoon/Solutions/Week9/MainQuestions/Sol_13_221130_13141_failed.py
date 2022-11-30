"""
https://www.acmicpc.net/problem/13141
"""
from heapq import heappop, heappush
input = __import__('sys').stdin.readline


def set_fire(N, M, E, V, i):
    # print('\nset_fire, starter : {}'.format(i))
    visited_edges = [False] * M
    visited_vertices = [None] * (N+1)
    visited_vertices[i] = 0
    visited_edge_cnt = 0

    heap = []
    # for j in V[i]:
    for j in range(len(V[i])):
        for edge in V[i][j]:
            heappush(heap, (E[edge], 0, i, j, edge))

    timer = 0
    while heap and visited_edge_cnt < M:
        added_time, prev_time, popped_from, popped_to, popped_edge = heappop(heap)

        if visited_edges[popped_edge]:
            continue
        else:
            visited_edges[popped_edge] = True
            visited_edge_cnt += 1

        first_visit = False
        if popped_from == popped_to:
            curr_time = prev_time + E[popped_edge] / 2
        elif visited_vertices[popped_to] is None:
            curr_time = added_time
            visited_vertices[popped_to] = curr_time
            first_visit = True
        else:
            if added_time < visited_vertices[popped_to]:
                visited_vertices[popped_to] = added_time
                curr_time = added_time
                first_visit = True

            else:
                left_over = added_time - visited_vertices[popped_to]
                # print('added_time : {}, visited_vertices[popped_to] : {}'.format(added_time, visited_vertices[popped_to]))
                # print('left_over : {}'.format(left_over))
                curr_time = added_time - left_over / 2

        timer = max(timer, curr_time)
        # print('  [{}->{}] time : {}->{}, timer : {}'.format(popped_from, popped_to, prev_time, curr_time, timer))

        if first_visit:
            # for next_to in V[popped_to]:
            for next_to in range(len(V[popped_to])):
                for next_edge in V[popped_to][next_to]:
                    heappush(heap, (curr_time+E[next_edge], curr_time, popped_to, next_to, next_edge))

    # print('Final : {}'.format(timer))
    return timer


if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = [None] * M
    # vertices = [None] * (N+1)
    # for m in range(M):
    #     s, e, l = map(int, input().split())
    #     if vertices[s] is None:
    #         vertices[s] = {}
    #     if e not in vertices[s]:
    #         vertices[s][e] = []
    #     vertices[s][e].append(m)
    #
    #     if vertices[e] is None:
    #         vertices[e] = {}
    #     if s not in vertices[e]:
    #         vertices[e][s] = []
    #     vertices[e][s].append(m)
    #
    #     edges[m] = l

    vertices = [[[] for _ in range(N+1)] for _ in range(N+1)]
    for m in range(M):
        s, e, l = map(int, input().split())
        vertices[s][e].append(m)
        vertices[e][s] = vertices[s][e]
        edges[m] = l

    # print('vertices : {}'.format(vertices))
    # print('edges : {}'.format(edges))

    final_result = None
    for starter in range(1, N+1):
        temp = set_fire(N, M, edges, vertices, starter)
        final_result = min(final_result, temp) if final_result is not None else temp

    print(final_result)