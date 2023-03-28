from random import randint

def sorted_matrix_generator(m, n):
    r = 5
    result = [[None for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                result[0][0] = randint(0, r)
            elif i == 0:
                result[i][j] = result[i][j-1] + randint(1, r)
            elif j == 0:
                result[i][j] = result[i-1][j] + randint(1, r)
            else:
                result[i][j] = max(result[i][j-1], result[i-1][j]) + randint(1, r)

    return result

def sorted_matrix_search(M, target):
    r, c = 0, len(M[0])-1
    while r < len(M) and c >= 0:
        if M[r][c] == target:
            return r, c, target
        elif M[r][c] > target:
            c -= 1
        else:
            r += 1
    return None


if __name__ == '__main__':
    x = sorted_matrix_generator(10, 8)
    for i, m in enumerate(x):
        for j, n in enumerate(m):
            print('{}'.format(n), end=" ")
        print()
    
    print(sorted_matrix_search(x, 30))