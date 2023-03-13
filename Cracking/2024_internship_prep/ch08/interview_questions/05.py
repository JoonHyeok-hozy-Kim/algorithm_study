def recursive_multiply(a, b):
    if b == 1:
        return a
    
    temp = recursive_multiply(a, b>>1) << 1
    if b & 1:
        temp += a
    
    return temp


if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, 10):
            print('{} X {} = {}'.format(i, j, recursive_multiply(i, j)))


# 146
        