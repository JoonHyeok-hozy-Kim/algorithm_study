"""
https://www.acmicpc.net/problem/1300
"""

def set_and_binary_search_solution(N, k):
    s = set()
    for i in range(1, N+1):
        for j in range(1, i+1):
            s.add(i*j)

    L = list(s)
    L.sort()

    start, end = 0, len(L)
    while end - start > 1:
        mid = (start + end) // 2
        idx_cnt = 0
        for i in range(1, N+1):
            if L[mid] > i*N:
                idx_cnt += N
            elif L[mid] == i*N:
                idx_cnt += N-1
            else:
                idx_cnt += L[mid]//i
                if L[mid]%i == 0:
                    idx_cnt -= 1

        # print('idx_cnt : {}, mid : {}, start : {}, end : {}'.format(idx_cnt, mid, start, end))
        if idx_cnt == k:
            return L[mid]
        elif idx_cnt > k:
            end = mid
        else:
            start = mid

    return L[start]


def sole_binary_solution(N, k):
    start, end = 0, N**2+1
    while end - start >= 1:
        if end - start == 1:
            return start

        mid = (start + end) // 2
        while not validate_mid(mid, N) and start <= mid < end:
            mid -= 1

        idx_cnt = get_idx(mid, N)
        # print('idx_cnt : {}, mid : {}, start : {}, end : {}'.format(idx_cnt, mid, start, end))

        if idx_cnt == k:
            return mid
        elif idx_cnt > k:
            end = mid
        else:
            next = mid+1
            while not validate_mid(next, N) and next < end:
                next += 1
            next_idx_cnt = get_idx(next, N)
            if k < next_idx_cnt:
                # print('GOT NEXT')
                return mid
            else:
                start = mid+1


def validate_mid(m, N):
    for i in range(1, (N**2//2)+1):
        if m%i == 0 and m//i <= N:
            return True
    return False


def get_idx(n, N):
    target_idx = 0
    for i in range(1, N+1):
        if n > N*i:
            target_idx += N
        elif n == N*i:
            target_idx += N-1
        else:
            target_idx += n//i
            if n%i == 0:
                target_idx -= 1
    return target_idx


if __name__ == '__main__':
    N = int(input())
    k = int(input())
    # print(N, k)

    # print(set_and_binary_search_solution(N, k))
    print(sole_binary_solution(N, k))
