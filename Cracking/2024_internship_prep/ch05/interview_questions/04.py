'''
1111000 -> 10000111 -> 10001011 -> 10001101 -> 10001110 -> 100101100

10111000

1011

111 
1011 1101 1110
10011 10101 10110 11001 11010 11100
100011 100101 100110 101001 101010 101100
'''

def get_next(N: int) -> int:
    one_cnt = 0
    walk = 1
    while walk & N == 0:
        walk <<= 1
    
    while walk & N != 0:
        one_cnt += 1
        walk <<= 1

    result = N | walk
    mask = walk

    while walk < N:
        walk <<= 1
        mask |= walk
    
    result &= mask
    result |= (1<<(one_cnt-1)) - 1
    
    return result


def get_prev(N: int) -> int:
    one_cnt = 0
    zero_cnt = 0
    walk = 1
    while walk & N != 0:
        one_cnt += 1
        walk <<= 1
    
    while walk & N == 0:
        zero_cnt += 1
        walk <<= 1
    
    if walk > N:
        return None
    
    mask = 0
    while walk < N:
        walk <<= 1
        mask += walk
    result = N & mask
    result |= ((1<<(one_cnt+1))-1)<<(zero_cnt-1)

    return result


if __name__ == '__main__':
    n = 0b111
    print("Get Next")
    for i in range(10):
        n = get_next(n)
        print(bin(n))
    
    print("\nGet Prev")
    for i in range(10):
        n = get_prev(n)
        print(bin(n))