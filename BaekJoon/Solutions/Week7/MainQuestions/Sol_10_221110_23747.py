"""
https://www.acmicpc.net/problem/23747
"""
from collections import deque


def activity_W(R, C, I, V, curr):
    if V[curr[0]-1][curr[1]-1] == '.':
        return curr

    Q = deque()
    Q.append(curr)
    alpha = I[curr[0]-1][curr[1]-1]
    target_area = set()
    target_area.add((curr[0], curr[1]))
    while Q:
        popped = Q.popleft()
        for i in range(4):
            target = [popped[0], popped[1]]
            if i%4 == 0:
                target[0] += 1
            elif i%4 == 1:
                target[0] -= 1
            elif i%4 == 2:
                target[1] += 1
            else:
                target[1] -= 1

            if 0 <= target[0]-1 < R and 0 <= target[1]-1 < C and I[target[0]-1][target[1]-1] == alpha:
                if (target[0], target[1]) not in target_area:
                    target_area.add((target[0], target[1]))
                    Q.append(target)

    for warded in target_area:
        V[warded[0]-1][warded[1]-1] = '.'
        # show_map(R, V)

    return curr


def add_current_vision(R, C, V, curr):
    for i in range(5):
        target = [curr[0], curr[1]]
        if i%5 == 0:
            target[0] += 1
        elif i%5 == 1:
            target[0] -= 1
        elif i%5 == 2:
            target[1] += 1
        elif i%5 == 3:
            target[1] -= 1
        else:
            None

        if 0 <= target[0]-1 < R and 0 <= target[1]-1 < C:
            V[target[0]-1][target[1]-1] = '.'


def show_map(R, V):
    for i in range(R):
        print(''.join(V[i]))
    # print()


if __name__ == '__main__':
    R, C = map(int, input().split())
    isekye = [input() for _ in range(R)]
    curr_position = list(map(int, input().split()))
    journey = input()

    # print(R, C)
    # print(isekye)
    # print(curr_position)
    # print(journey)

    vision_map = [['#'] * C for _ in range(R)]
    # vision_map[curr_position[0]-1][curr_position[1]-1] = '.'

    for activity in journey:
        if activity == 'W':
            curr_position = activity_W(R, C, isekye, vision_map, curr_position)
        elif activity == 'U':
            curr_position[0] -= 1
        elif activity == 'D':
            curr_position[0] += 1
        elif activity == 'L':
            curr_position[1] -= 1
        elif activity == 'R':
            curr_position[1] += 1

    add_current_vision(R, C, vision_map, curr_position)
    show_map(R, vision_map)