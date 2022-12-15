"""
1256. 사전
https://www.acmicpc.net/problem/1256
"""


def get_binary(n, r):
    m = min(n-r, r)
    x = 1
    result = 1
    for _ in range(m):
        result *= n
        result //= x
        n -= 1
        x += 1
    return result


def get_total_cnt(N, M):
    return get_binary(N+M, M)


def binary_treatment(K, M):
    cnt = 0
    while True:
        b = get_binary(M+cnt, cnt)
        # print('In binary_treatment loop, K : {}, b : {}'.format(K, b))
        if K > b:
            K -= b
            cnt += 1
        else:
            break
    # print('In binary_treatment, K : {}, cnt : {}'.format(K, cnt))
    return K, cnt


if __name__ == '__main__':
    N, M, K = map(int, input().split())

    T = get_total_cnt(N, M)

    if K > T:
        print(-1)
    else:
        while N > 0 and M > 0:
            M -= 1
            K, push = binary_treatment(K, M)
            # print('In loop, N : {}, K : {}, push : {}'.format(N, K, push))
            n_used_cnt = 0
            for _ in range(N-push):
                n_used_cnt += 1
                print('a', end="")
            print('z', end="")
            N -= n_used_cnt

        for _ in range(N):
            print('a', end="")

        for _ in range(M):
            print('z', end="")
