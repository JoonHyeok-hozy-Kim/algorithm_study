"""
https://www.acmicpc.net/problem/20301
"""


if __name__ == '__main__':
    N, K, M = map(int, input().split())
    # print(N, K, M)

    circle = [i+1 for i in range(N)]
    # print(circle)

    cnt = 0
    del_target = None
    reverse_flag = False
    while len(circle) > 0:
        if cnt > 0 and cnt % M == 0:
            reverse_flag = not reverse_flag
        # print(reverse_flag)

        if del_target is None:
            del_target = K-1
        else:
            if reverse_flag:
                del_target += len(circle) - K
                del_target %= len(circle)

            else:
                del_target += K-1
                del_target %= len(circle)

        print(circle.pop(del_target))
        cnt += 1

