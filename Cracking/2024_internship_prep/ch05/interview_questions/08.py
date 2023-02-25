def draw_line(screen: list, width: int, x1: int, x2: int, y: int):
    line = ((1<<(x2-x1+1)) - 1) << (width - x2 - 1)
    S[y] |= line
    return


if __name__ == '__main__':
    from random import randint
    S = []
    ceiling = (1<<16) - 1
    print(bin(ceiling))

    for i in range(16):
        S.append(0)
        print(bin(S[i]))
    
    draw_line(S, 16, 3, 5, 3)

    for i in range(16):
        print("{}".format(bin(S[i])))

