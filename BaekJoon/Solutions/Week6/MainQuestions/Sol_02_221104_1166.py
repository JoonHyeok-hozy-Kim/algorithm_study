"""
https://www.acmicpc.net/problem/1166
"""


def binary_search_solution(N, L, W, H):
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


def get_real_number(N, L, W, H, I):
    power = .5
    for i in range(10):
        print(power, L/(I+power), W/(I+power), H/(I+power), L/(I+power) * W/(I+power) * H/(I+power))
        print(L//(I+power), W//(I+power), H//(I+power))
        if L/(I+power) * W/(I+power) * H/(I+power) < N:
            I += power
        power /= 2
        print(I)
    return I



if __name__ == '__main__':
    N, L, W, H = map(int, input().split())
    # print(N, L, W, H)

    int_result = binary_search_solution(N, L, W, H)
    final = get_real_number(N, L, W, H, int_result)
    print(final)