from random import randint

def sorted_merge(A, B):
    ai = 0
    while A[ai]:
        ai += 1
    ai -= 1

    bi = len(B) - 1
    back = len(A) - 1

    while ai >= 0 or bi >= 0:
        if bi < 0 or (ai >= 0 and A[ai] >= B[bi]):
            A[back] = A[ai]
            ai -= 1
        else:
            A[back] = B[bi]
            bi -= 1
        back -= 1


if __name__ == '__main__':
    an = 5
    bn = 4
    a = [randint(1, 100) for i in range(an)]
    a.sort()
    a.extend([None for i in range(bn)])
    b = [randint(1, 100) for i in range(bn)]
    b.sort()

    print(a, b)
    sorted_merge(a, b)
    print(a, b)