"""
1461. 도서관
https://www.acmicpc.net/problem/1461
"""


if __name__ == '__main__':
    N, M = map(int, input().split())
    books = list(map(int, input().split()))
    books.sort()
    # print(books)

    result = 0
    if abs(books[0]) > abs(books[-1]):
        pop_cnt = 0
        for i in range(M):
            if i < N and books[i] < 0:
                pop_cnt += 1
            else:
                break
        result -= books.pop(0)
        for _ in range(pop_cnt-1):
            books.pop(0)

    else:
        pop_cnt = 0
        for i in range(M):
            if N-1-i > 0 and books[N-1-i] > 0:
                pop_cnt += 1
            else:
                break
        result += books.pop()
        for _ in range(pop_cnt-1):
            books.pop()

    # print(result, books)
    if len(books) > 0:
        neg_cnt = 0
        for i in range(len(books)):
            if books[i] < 0:
                neg_cnt += 1
            else:
                break
        pos_cnt = len(books) - neg_cnt

        for j in range(neg_cnt):
            if j%M == 0:
                # print(books[j])
                result -= books[j] * 2

        for k in range(pos_cnt):
            if (neg_cnt+k)%M == (neg_cnt+pos_cnt-1)%M:
                # print(books[neg_cnt+k])
                result += books[neg_cnt+k] * 2

    print(result)

