def find_duplicates(L):
    bit_set = 0
    for i, v in enumerate(L):
        curr = 1<<v
        if bit_set & curr:
            print(v)
        else:
            bit_set |= curr


if __name__ == '__main__':
    L = [1,1,1,3,4,5,6,3,1111,1112,1113,1112]
    find_duplicates(L)