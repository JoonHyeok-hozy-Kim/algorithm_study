"""
1182. 부분수열의 합

N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을
작성하시오.
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