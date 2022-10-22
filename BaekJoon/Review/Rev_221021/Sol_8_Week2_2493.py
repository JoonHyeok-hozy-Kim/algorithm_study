"""
https://www.acmicpc.net/problem/2493
"""

from collections import deque


if __name__ == '__main__':
    N = int(input())
    towers = list(map(int, input().split()))

    # from random import randint
    # N = 10
    # towers = [randint(1, 10) for _ in range(N)]


    result = [0]
    temp_skyscrapers = deque()
    temp_skyscrapers.append([towers[0], 0])

    for i in range(N-1):
        if towers[i] < towers[i+1]:
            appended = False
            new_temp = deque()
            new_temp.append([towers[i+1], i+1])
            for j in range(len(temp_skyscrapers)):
                if temp_skyscrapers[j][0] >= towers[i+1]:
                    if len(new_temp) == 1:
                        result.append(temp_skyscrapers[j][1]+1)
                        appended = True
                    if temp_skyscrapers[j][0] > towers[i+1]:
                        new_temp.append(temp_skyscrapers[j])
            temp_skyscrapers = new_temp


            if not appended:
                result.append(0)

        else:
            if towers[i] == towers[i+1]:
                temp_skyscrapers.popleft()
            temp_skyscrapers.appendleft([towers[i+1], i+1])
            result.append(i+1)

        # print('temp : {}'.format(temp_skyscrapers))

    # print(*towers, sep=" ")
    print(*result, sep=" ")