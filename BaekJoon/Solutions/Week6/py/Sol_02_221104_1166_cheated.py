"""
https://www.acmicpc.net/problem/1166
"""


def int_binary_search_solution(N, L, W, H):
    start, end = 0, min(L, W, H)+1
    result = []
    while end - start >= 1:
        # print(start, end)
        mid = (start + end) // 2
        l, w, h = L//mid, W//mid, H//mid
        # print('l*w*h : {}'.format(l*w*h))
        if l*w*h < N:
            end = mid
        else:
            result.append(mid)
            start = mid+1

    # print(result)
    return max(result)


def real_binary_search_solution(N, L, W, H):
    start, end = 0, min(L, W, H)
    for i in range(10000):
        mid = (start + end) / 2
        l, w, h = L // mid, W // mid, H // mid
        # print(mid, l*w*h)
        if l*w*h < N:
            end = mid
        else:
            start = mid

    return mid



if __name__ == '__main__':
    N, L, W, H = map(int, input().split())
    # print(N, L, W, H)

    # int_result = int_binary_search_solution(N, L, W, H)

    real_result = real_binary_search_solution(N, L, W, H)
    print('{:.10f}'.format(real_result))