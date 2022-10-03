

if __name__ == '__main__':
    N = int(input())
    cnt = 0
    temp = 1
    while temp <= N:
        temp *= 3
        cnt += 1
        print(temp)
    while temp <= N:
        temp *= 2
        cnt += 1
        print(temp)
    while temp < N:
        temp += 1
        cnt + 1
        print(temp)

    print(cnt)


1 : 1
2 : (3) 1
3 : (1) 1
4 : (3,1) 2
5 : (3,3,1) 3 (3, 2, 2)
6 : (1, 3) 2
7 : (3, 1, 3)
8 : (3, 3, 1, 3) (2, 3, 1)
9 : (1, 1)

11 : (10, 5, 4, 2, 1)  (10, 9, 3, 1)