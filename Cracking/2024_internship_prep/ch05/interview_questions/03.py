def flip_bit_to_win(N: int) -> int:
    result = 0
    right = 0
    left = 0

    while N > 0:
        if N & 1:
            left += 1
        else:
            result = max(result, right + left + 1)
            right = left
            left = 0
        N >>= 1
    
    return result

if __name__ == '__main__':
    print(flip_bit_to_win(1775))
    print(flip_bit_to_win(0b11101111011101001111100))