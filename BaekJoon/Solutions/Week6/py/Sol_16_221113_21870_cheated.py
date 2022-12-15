"""
https://www.acmicpc.net/problem/21870
"""


def calculate_beauty(S, temp=0):
    # print('In calculate_beauty, S : {}, temp : {}'.format(S, temp))
    if len(S) == 1:
        return temp + S[0]

    elif len(S) == 2:
        return temp + sum(S)

    left_temp, left_remaining = do_left(S)
    left_result = calculate_beauty(left_remaining, temp+left_temp)

    right_temp, right_remaining = do_right(S)
    right_result = calculate_beauty(right_remaining, temp+right_temp)

    if left_result > right_result:
        return left_result
    else:
        return right_result


def do_left(S):
    if len(S) == 1:
        return S[0], None
    return get_gcd(S[:len(S)//2]), S[len(S)//2:]


def do_right(S):
    if len(S) == 1:
        return S[0], None
    return get_gcd(S[len(S)//2:]), S[:len(S)//2]


def get_gcd(S):
    if len(S) == 1:
        return S[0]

    mid = len(S)//2
    S1 = S[:mid]
    S2 = S[mid:]

    gcd1 = get_gcd(S1)
    gcd2 = get_gcd(S2)

    return euclidean_gcd(gcd1, gcd2)


def calculate_gcd(n1, n2):
    if n1 >= n2 and n1 % n2 == 0:
        return n2
    elif n1 < n2 and n2 % n1 == 0:
        return n1

    d1 = get_divisors(n1)
    d2 = get_divisors(n2)

    common_divisors = d1.intersection(d2)
    return max(common_divisors)


def get_divisors(n):
    if n == 1:
        return {1}

    temp1 = [1]
    temp2 = [n]
    divisor = 2
    while divisor < temp2[-1]:
        # print(temp)
        if n % divisor == 0:
            temp1.append(divisor)
            temp2.append(n//divisor)
        divisor += 1

    temp1.extend(temp2)
    return set(temp1)


def euclidean_gcd(x, y):
    while y:
        x, y = y, x % y
    return x



if __name__ == '__main__':
    N = int(input())
    series = list(map(int, input().split()))
    # print(series)

    # n = 144
    # print(get_divisors(n))
    # print(calculate_gcd(12, 42))

    # a = [36, 48, 84]
    # print(get_gcd(a))

    result = calculate_beauty(series)
    print(result)
