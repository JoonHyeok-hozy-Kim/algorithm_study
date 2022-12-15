"""
1463. 1로 만들기
https://www.acmicpc.net/problem/1463
"""

def making_one(N):
    M = []
    M.append(0)
    M.append(0)
    curr = 2
    while curr <= N:
        # print(curr)
        if curr % 3 == 0:
            temp = min(M[curr//3], M[curr-1])
            if curr % 2 == 0:
                temp = min(temp, M[curr//2])
            M.append(temp+1)

        else:
            if curr % 2 == 0:
                M.append(min(M[curr-1], M[curr//2])+1)
            else:
                temp = min(M[(curr - 1) // 2], M[curr - 2])
                if (curr-1) % 3 == 0:
                    temp = min(temp, M[(curr-1)//3])
                M.append(temp+2)

        curr += 1

    # for i in range(N):
    #      print(i+1, M[i+1])

    return M[-1]


if __name__ == '__main__':
    N = int(input())
    result = making_one(N)
    print(result)


