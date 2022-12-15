"""
11050. 이항 계수 1
https://www.acmicpc.net/problem/11050
"""

def loop_binary_sol(n, k):
    rep = min(k, n-k)
    l = 1
    result = 1
    for i in range(rep):
        result *= n
        result //= l
        n -= 1
        l += 1
    return result


def recursive_binary_sol(n, k):
    if k == 0 or k == n:
        return 1
    elif k == 1 or k == n-1:
        return n
    else:
        return recursive_binary_sol(n-1, k-1) + recursive_binary_sol(n-1, k)


if __name__ == '__main__':
    N, K = map(int, input().split())

    # print(loop_binary_sol(N, K))
    print(recursive_binary_sol(N, K))