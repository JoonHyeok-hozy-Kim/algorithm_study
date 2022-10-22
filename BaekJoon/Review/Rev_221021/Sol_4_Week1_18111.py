"""
https://www.acmicpc.net/problem/18111
"""


if __name__ == '__main__':
    N, M, B = map(int, input().split())
    field = []
    for i in range(N):
        field.extend(list(map(int, input().split())))
    operation_plan = [None] * (N * M)
    # print(field)
    # print(operation_plan)

    max_height = None
    min_height = None
    for f in field:
        max_height = max(max_height, f) if max_height is not None else f
        min_height = min(min_height, f) if min_height is not None else f
    # print(max_height)

    for i in range(N*M):
        operation_plan[i] = max_height - field[i]

    # print(operation_plan)

    target_height = max_height
    result_list = []
    while target_height >= min_height:
        need_fillings = 0
        need_diggings = 0
        for f in field:
            if target_height > f:
                need_fillings += target_height - f
            else:
                need_diggings += f - target_height
        if need_fillings <= B + need_diggings:
            result_list.append([need_fillings + 2*need_diggings, target_height])

        target_height -= 1

    # print(result_list)
    result = None
    for r in result_list:
        if result is None or result[0] > r[0]:
            result = r
    print(*result, sep=" ")