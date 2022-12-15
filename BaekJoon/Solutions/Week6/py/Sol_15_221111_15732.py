"""
https://www.acmicpc.net/problem/15732
"""


def determine_count(R, i):
    cnt = 0
    for r in R:
        # if i - r[0] >= 0 and (i-r[0]) % r[2] == 0:
        if i - r[0] >= 0:
            max_val = (r[1]-r[0])//r[2] + 1
            diff = i - r[0]
            cnt += min(max_val, diff//r[2] + 1)
    return cnt


def binary_search_solution(N, D, R):
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if determine_count(R, mid) >= D:
            end = mid-1
        else:
            start = mid + 1
    return start


if __name__ == '__main__':
    N, K, D = map(int, input().split())
    rules = [list(map(int, input().split())) for _ in range(K)]
    # print(rules)

    # print(determine_count(rules, 100))
    # print(determine_count(rules, 101))
    # print(determine_count(rules, 109))
    # print(determine_count(rules, 110))
    # print(determine_count(rules, 120))
    # print(determine_count(rules, 125))

    result = binary_search_solution(N, D, rules)
    print(result)