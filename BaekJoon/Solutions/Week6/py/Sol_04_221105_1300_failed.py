"""
https://www.acmicpc.net/problem/1300
"""


def get_number(N, k):
    start, end = 1, N**2+1
    while end - start >= 1:
        mid = (start + end) // 2
        idx_cnt = 0
        for i in range(1, N+1):
            if mid > N*i:
                idx_cnt += N
            elif mid == N*i:
                idx_cnt += N-1
            else:
                idx_cnt += mid // i
                if mid % i == 0:
                    idx_cnt -= 1
        print('mid : {}, idx_cnt : {}'.format(mid, idx_cnt))
        if idx_cnt > k:
            end = mid
        elif idx_cnt == k:
            return mid
        else:
            start = mid+1

    print('UNDEFINED, mid : {}, idx_cnt : {}'.format(mid, idx_cnt))

if __name__ == '__main__':
    N = int(input())
    k = int(input())

    get_number(N, k)

    vl = []
    for i in range(N):
        for j in range(N):
            print((i+1)*(j+1), end=" ")
            vl.append((i+1)*(j+1))
        print()
    vl.sort()
    print(vl)