"""
1182. 부분수열의 합
https://www.acmicpc.net/problem/1182
"""

def subset_sum(idx, sub_sum, cnt=0):
    if idx >= n:
        return cnt

    sub_sum += arr[idx]

    if sub_sum == s:
        cnt += 1

    cnt = subset_sum(idx+1, sub_sum, cnt)
    cnt = subset_sum(idx+1, sub_sum - arr[idx], cnt)
    return cnt


if __name__ == '__main__':
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    print(subset_sum(0, 0))