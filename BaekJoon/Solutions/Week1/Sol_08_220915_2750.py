"""
2750. 수 정렬하기

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다.
수는 중복되지 않는다.
"""

from random import randint
def inplace_quick_sort(S, a=0, b=None):
    if b is None:
        b = len(S)-1
    if a >= b: return

    p = randint(a, b)
    S[p], S[b] = S[b], S[p]

    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1

    S[left], S[b] = S[b], S[left]
    inplace_quick_sort(S, a, left-1)
    inplace_quick_sort(S, left+1, b)


if __name__ == '__main__':
    N = int(input())
    num_list = []
    for i in range(N):
        num_list.append(int(input()))
    inplace_quick_sort(num_list)
    for i in num_list:
        print(i)