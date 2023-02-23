def flip_cnt(A: int, B: int) -> int:
    walk = 1
    result = 0
    while walk < A or walk < B:
        if (A & walk) != (B & walk):
            result += 1
        walk <<= 1

    return result


if __name__ == '__main__':
    print(flip_cnt(0b11101, 0b01111))
    print(flip_cnt(0b1111101, 0b01111))