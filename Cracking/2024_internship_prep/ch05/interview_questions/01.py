
def insert(N: int, M: int, j: int, i: int) -> int:
    mask = (1 << (j-i+1)) - 1
    mask <<= i
    return (N & (~mask)) | (M << i)

if __name__ == '__main__':
    n = 0b10000000000
    m = 0b10011
    i = 2
    j = 6

    print(bin(insert(n, m, j, i)))