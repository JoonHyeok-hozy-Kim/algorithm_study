# Faster power operation!


def recursive_power(i, n):
    print('R')
    if n == 1:
        return i

    half = recursive_power(i, n//2)
    remaining = i if n%2 == 1 else 1

    return half * half * remaining


if __name__ == '__main__':
    print(recursive_power(2, 1000000))