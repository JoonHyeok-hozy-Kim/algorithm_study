def pairwise_swap(N: int) -> int:
    mask = 1
    cnt = 0
    while mask <= N:
        mask <<= 1
        if cnt % 2 != 0:
            mask += 1
        cnt += 1
    
    mask >>= 1
    if cnt % 2 != 0:
        mask >>= 1

    # print(bin(mask), bin(mask>>1))
    # print(bin((N & mask)>>1), bin((N & (mask>>1))<<1))
    return ((N & mask)>>1) + ((N & (mask>>1))<<1)


if __name__ == '__main__':
    n = 0b1111000
    print(bin(n), bin(pairwise_swap(n)))
    n = 0b101110110111
    print(bin(n), bin(pairwise_swap(n)))