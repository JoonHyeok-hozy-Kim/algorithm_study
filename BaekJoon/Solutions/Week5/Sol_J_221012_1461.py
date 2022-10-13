"""
1461. 도서관
https://www.acmicpc.net/problem/1461
"""


if __name__ == '__main__':
    N, M = map(int, input().split())
    books = list(map(int, input().split()))
    books.sort()
    print(books)
    neg_start = 0
    pos_start = 0
    while pos_start < N and books[pos_start] < 0:
        pos_start += 1

    result = 0
    if abs(books[0]) > abs(books[N-1]):
        result += abs(books[0])
        if pos_start >= M:
            neg_start += M
        neg = books[neg_start:pos_start]
        pos = books[pos_start:]

    else:
        result += abs(books[-1])
        if N - pos_start >= M:
            for _ in range(M):
                books.pop()

    if len(books) > 0:
        idx = 0
        while books[idx] < 0:
